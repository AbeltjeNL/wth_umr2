"""Config flow for WTH UMR2 Regulator integration."""
from __future__ import annotations

import asyncio
import logging
from typing import Any

from aiohttp import ClientError
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant, callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST, default="WTH.UMR.IP.ADDRESS"): cv.string,
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect.
    
    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """
    host = data[CONF_HOST]
    url = f"http://{host}/get.json?f=$.status.*"
    
    session = async_get_clientsession(hass)
    
    try:
        async with asyncio.timeout(10):
            async with session.get(url) as response:
                if response.status != 200:
                    raise ConnectionError(f"HTTP {response.status}")
                
                json_data = await response.json()
                
                if "status" not in json_data:
                    raise ValueError("Invalid response format")
                
                # Extract device ID if available
                device_id = json_data.get("id", "unknown")
                device_type = json_data.get("type", "WTH_Regulator")
                
                return {
                    "title": f"WTH UMR2 ({device_id[-8:]})" if len(device_id) > 8 else f"WTH UMR2 ({device_id})",
                    "device_id": device_id,
                    "device_type": device_type,
                }
                
    except TimeoutError as err:
        _LOGGER.error("Timeout connecting to WTH UMR2 at %s", host)
        raise ConnectionError("Timeout") from err
    except ClientError as err:
        _LOGGER.error("Error connecting to WTH UMR2 at %s: %s", host, err)
        raise ConnectionError(str(err)) from err
    except Exception as err:
        _LOGGER.exception("Unexpected error connecting to WTH UMR2 at %s", host)
        raise


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for WTH UMR2 Regulator."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        """Get the options flow for this handler."""
        return OptionsFlowHandler(config_entry)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
            except ConnectionError as err:
                if "Timeout" in str(err):
                    errors["base"] = "timeout"
                else:
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

        # Logo is now handled automatically by HA 2026.3+ via /api/brands/integration/

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for WTH UMR2."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({}),
        )


