# Changelog

All notable changes to the WTH UMR2 integration will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2026-05-17

### Added
- **HA 2026.3+ Brand System** - Official brand folder support for logos
- **brand/ Folder** - Icons and logos in `custom_components/wth_umr2/brand/`
- **brand.json** - Brand metadata file for integration
- **HD Logo Images** - logo@2x.png (512×512) for high-DPI displays
- **Complete Dutch Support** - All strings translated to Nederlands

### Changed
- **Logo Serving** - Now uses official `/api/brands/integration/wth_umr2/` endpoint
- **Removed Custom HTTP** - No longer serving logos via custom endpoint
- **Simplified Code** - Removed ~50 lines of custom logo serving logic
- **Config Flow** - Removed custom logo URL (HA handles it now)

### Removed
- ❌ Custom `/api/wth_umr2/logo/` HTTP endpoint
- ❌ WTHLogoView class (no longer needed)
- ❌ Logo copying to `www/wth_umr2/` directory
- ❌ Logo URL placeholder in config flow

### Fixed
- Logo display in Home Assistant UI (now uses official HA API)
- Language support now works correctly (EN + NL)
- Cleaner code structure
- Better security via official HA endpoints

### Performance
- Faster image serving via official HA API
- Better caching (handled by HA)
- Reduced integration code complexity
- Lighter memory footprint

## [1.2.0] - 2026-05-14

### Added
- **Home Assistant 2026 Standards**: Full compliance with HA 2026.5+ requirements
- **Type Aliases**: Modern `type` syntax for ConfigEntry (`type WTHConfigEntry = ConfigEntry[WTHCoordinator]`)
- **Runtime Data**: Using `entry.runtime_data` instead of `hass.data` (HA 2025.1+)
- **Device Registry**: Direct device registration in `async_setup_entry`
- **Coordinator Shutdown**: Proper `async_shutdown()` method for cleanup
- **Quality Scale**: Upgraded to Platinum
- **Always Update Flag**: `always_update=False` for better performance
- **Single Config Entry**: Specified in manifest

### Changed
- **BREAKING**: Requires Home Assistant 2025.1.0 or newer
- **BREAKING**: Requires Python 3.12 or newer
- Migrated from `hass.data[DOMAIN]` to `entry.runtime_data`
- Coordinator session is now private (`_session`)
- Improved type validation with `isinstance()` checks
- Changed `asyncio.TimeoutError` to `TimeoutError` (Python 3.11+)
- Device info now registered directly in device registry
- Removed unused imports

### Fixed
- Better exception hierarchy with TimeoutError vs asyncio.TimeoutError
- Proper coordinator cleanup on failed setup
- More robust data validation

### Performance
- `always_update=False` prevents unnecessary updates
- Better resource cleanup with `async_shutdown()`
- Optimized device registry usage

## [1.1.0] - 2026-01-27

### Added
- Modern async patterns with `asyncio.timeout()` (Python 3.11+)
- `async_reload_entry()` function for integration reload support
- Entity category `DIAGNOSTIC` for communication and device status sensors
- Better error handling with specific timeout detection
- `issue_tracker` and `quality_scale` in manifest
- Field descriptions in config flow for better UX
- `ConfigEntryNotReady` exception handling for startup failures

### Changed
- **BREAKING**: Upgraded to Home Assistant 2024+ standards
- Updated coordinator with proper type hints (`dict[str, Any]`)
- Improved coordinator with better error messages and exception chaining
- Replaced `os.path` with `Path` for modern file handling
- Used `web.FileResponse` instead of reading files into memory for better performance
- Changed coordinator naming to be unique per entry
- Enhanced device info to be set once in `__init__` for better performance
- Updated all type hints to use modern Python 3.11+ syntax
- Improved error messages with more context (host, specific errors)

### Fixed
- Proper timeout handling with separate error message
- Better exception handling with `from err` chaining for traceback preservation
- Coordinator now validates response structure before returning
- Logo serving now uses FileResponse for better memory efficiency
- Improved availability check for sensors

### Security
- Changed allowed_files from list to set for better performance and security
- Enhanced file path validation

### Developer
- Added comprehensive type hints throughout
- Improved code documentation
- Better separation of concerns in error handling
- Modernized import statements
- Enhanced logging with more context

## [1.0.0] - 2026-01-27

### Added
- Initial release
- Full support for WTH UMR2 Regulator via JSON API
- GUI-based configuration flow
- 60+ sensor entities covering all device data
- Automatic logo loading via HTTP API and WWW directory
- Multi-language support (English, Dutch)
- Real-time updates every 30 seconds
- Comprehensive documentation

### Features
- Main system status and mode sensors
- 8 thermostat zones with temperature monitoring
- 10 valve position sensors
- Heater, cooler, and pump control monitoring
- 10 temperature sensor inputs
- Communication status (Fanlink, RF, Modbus, Bluetooth, Ethernet)
- Connected device information
- Automatic WWW directory setup for logos
- Logo serving via `/api/wth_umr2/logo/` endpoint
