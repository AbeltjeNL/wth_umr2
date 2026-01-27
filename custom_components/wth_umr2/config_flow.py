"""Config flow for WTH UMR2 Regulator integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST, default="192.168.178.69"): cv.string,
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect."""
    host = data[CONF_HOST]
    url = f"http://{host}/get.json?f=$.status.*"
    
    session = async_get_clientsession(hass)
    
    try:
        async with session.get(url, timeout=10) as response:
            if response.status != 200:
                raise ConnectionError(f"HTTP {response.status}")
            
            json_data = await response.json()
            
            if "status" not in json_data:
                raise ValueError("Invalid response format")
            
            # Extract device ID if available
            device_id = json_data.get("id", "unknown")
            
            return {"title": f"WTH UMR2 ({device_id})", "device_id": device_id}
            
    except Exception as err:
        _LOGGER.error("Error connecting to WTH UMR2: %s", err)
        raise


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for WTH UMR2 Regulator."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
            except ConnectionError:
                errors["base"] = "cannot_connect"
            except ValueError:
                errors["base"] = "invalid_response"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                await self.async_set_unique_id(user_input[CONF_HOST])
                self._abort_if_unique_id_configured()
                
                return self.async_create_entry(
                    title=info["title"],
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )
