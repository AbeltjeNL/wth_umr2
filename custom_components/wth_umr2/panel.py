"""WTH UMR2 Frontend panel support."""
from homeassistant.components import frontend
from homeassistant.core import HomeAssistant


async def async_setup_frontend(hass: HomeAssistant) -> None:
    """Set up the frontend panel."""
    # Register the static path for logos
    await frontend.async_register_built_in_panel(
        hass,
        component_name="wth_umr2",
        sidebar_title="WTH UMR2",
        sidebar_icon="mdi:radiator",
        frontend_url_path="wth_umr2",
        config={"logo": "/api/wth_umr2/logo/logo.png"},
        require_admin=False,
    )
