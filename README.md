# WTH UMR2 Regulator Integration for Home Assistant

**Version:** 1.3.0  
**Author:** AbeltjeNL  
**License:** MIT  
**Quality:** Platinum ⭐  
**Languages:** English 🇬🇧 | Dutch 🇳🇱

This custom component integrates the WTH UMR2 heating regulator with Home Assistant, allowing you to monitor and control your heating system.

This integration has no affiliation with the company WTH nor do I. 
All uses images and logos are freely available on Google. 
This integration was made using Claude AI. No manual labor on my end. Keep this in mind ;)
The integration works properly and i'm not planning to do maintanace releases. 
If you like it, use it! :)

## ✨ What's New in v1.3.0

- 🏆 **HA 2026.3+ Brand System** - Logos served via official `/api/brands/integration/` endpoint
- 🎯 **Simpler Code** - Removed custom logo serving (HA handles it now)
- 🌐 **Full Language Support** - English + Dutch translations
- 📊 **Platinum Quality** - Highest HA standard
- ⚡ **Better Performance** - Official HA image serving
- 🔒 **Better Security** - Uses HA's secure brand API

See [RELEASE_v1.3.0.md](RELEASE_v1.3.0.md) for full details.

## 🚀 Quick Install

```bash
# 1. Extract package
unzip wth_umr2_v1.3.0.zip

# 2. Copy to Home Assistant
cp -r wth_umr2/custom_components/wth_umr2 /config/custom_components/

# 3. Restart Home Assistant
# Settings → System → Restart

# 4. Add Integration
# Settings → Devices & Services → Add Integration
# Search: "WTH UMR2"
# Enter IP: YOUR.WTH.IP.ADDRESS
```

## 📋 Requirements

- **Home Assistant:** 2025.1.0 or newer (best with 2026.3+)
- **Python:** 3.12 or newer
- **WTH UMR2:** Connected to local network
- **Network:** Local access to device IP

## ✨ Features

### Automatic
- ✅ **Brand Logos** - Automatically displayed via `/api/brands/integration/`
- ✅ **Device Registration** - Automatic device creation
- ✅ **Real-time Updates** - Every 30 seconds
- ✅ **Multi-Language** - English + Dutch support
- ✅ **Entity Categories** - Diagnostic sensors organized

### Monitoring (60+ Sensors)
- System status (state, mode, display, LED)
- Heater, cooler, pump outputs
- 8 thermostat zones with temperature
- 10 valve positions
- 10 temperature sensor inputs
- Communication status (Fanlink, RF, Modbus, Bluetooth, Ethernet)
- Connected device information

## 🌐 Language Support

Select your language in Home Assistant:
```
Settings → System → General → Language
```

**Supported:**
- 🇬🇧 English
- 🇳🇱 Nederlands (Dutch)

All interface text, error messages, and help text are automatically translated.

## 📚 Documentation

- **[START_HERE.md](START_HERE.md)** - Installation & setup guide
- **[RELEASE_v1.3.0.md](RELEASE_v1.3.0.md)** - What's new in v1.3.0
- **[CHANGELOG.md](CHANGELOG.md)** - Complete version history
- **[DASHBOARD_CARDS_WITH_LOGO.md](DASHBOARD_CARDS_WITH_LOGO.md)** - 8 example cards
- **[UPGRADE_GUIDE.md](UPGRADE_GUIDE.md)** - Upgrade instructions

## 🎨 Brand System (HA 2026.3+)

Starting with HA 2026.3, brand images are automatically served from the integration:

```yaml
# In dashboard cards - use the official endpoint:
image: /api/brands/integration/wth_umr2/logo.png
```

Logos are automatically displayed in:
- Integration list
- Device pages
- Configuration flows

## 🔧 Configuration

No manual configuration needed! Just add the integration via the UI:

```
Settings → Devices & Services → Add Integration
↓
Search: "WTH UMR2"
↓
Enter Device IP: YOUR.WTH.IP.ADDRESS
↓
Done!
```

## ✅ Verification

After installation:

1. **Check Integration**
   ```
   Settings → Devices & Services
   Should show: WTH UMR2 Regulator (with logo)
   ```

2. **Check Device**
   ```
   Settings → Devices & Services → WTH UMR2 → Device
   Should show: All 60+ sensors
   ```

3. **Check Logs**
   ```
   Settings → System → Logs
   Filter: "wth_umr2"
   Should be: Clean (no errors)
   ```

4. **Check Logo API**
   ```
   Browser: http://YOUR_HA:8123/api/brands/integration/wth_umr2/logo.png
   Should display: WTH logo
   ```

## 🐛 Troubleshooting

### Logo Not Showing
- Verify HA 2026.3+ or 2025.1+ is installed
- Check logs for errors
- Clear browser cache (Ctrl+Shift+R)
- Restart HA if needed

### Can't Find Integration
- Verify `custom_components/wth_umr2/` exists
- Check all files are copied
- Restart Home Assistant
- Clear browser cache

### Can't Connect to Device
- Verify IP address is correct
- Test connection: `ping 192.168.178.69`
- Ensure device is powered on
- Check device is on same network

## 🎯 What Gets Removed

If upgrading from v1.2.0:
- ❌ Custom `/api/wth_umr2/logo/` endpoint (no longer used)
- ❌ `www/wth_umr2/` directory (no longer needed)
- ✅ Logo serving now handled by HA 2026.3+ brand system

## 📊 Comparison

| Feature | v1.2.0 | v1.3.0 |
|---------|--------|--------|
| **HA Version** | 2025.1+ | 2025.1+ |
| **Brand System** | Custom API | HA 2026.3+ official |
| **Logo Serving** | Custom HTTP | `/api/brands/integration/` |
| **Code Size** | ~2,100 lines | ~2,000 lines (simplified) |
| **Language** | English | EN + NL |
| **Quality** | Platinum | Platinum |

## 🆚 Before & After

### Before (Custom Logo API)
```python
# Custom HTTP endpoint
hass.http.register_view(WTHLogoView)

# Manual file serving
class WTHLogoView(HomeAssistantView):
    url = "/api/wth_umr2/logo/{filename}"
    # 50+ lines of code
```

### After (Official Brand System)
```python
# Nothing needed!
# HA 2026.3+ handles everything automatically
```

## 💡 Benefits

✅ **Cleaner Code** - Removed 50+ lines of custom serving logic  
✅ **Better Performance** - Official HA image serving  
✅ **Better Security** - Uses HA's secure API  
✅ **Future-Proof** - Aligns with HA 2026+ standards  
✅ **Less Maintenance** - HA handles image serving  
✅ **Consistent** - Matches other integrations  

## 🆘 Support

- **Documentation:** See included .md files
- **Issues:** https://github.com/AbeltjeNL/wth_umr2/issues
- **Discussions:** https://github.com/AbeltjeNL/wth_umr2/discussions

## 📄 License

MIT License - See [LICENSE](LICENSE) file

---

**Ready to install?** See [START_HERE.md](START_HERE.md) for detailed setup instructions!


## 🎨 Logo Display

**NEW:** The WTH logo now loads automatically from local storage!

When you install the integration, logos are automatically:
- ✅ Served via HTTP API endpoint: `/api/wth_umr2/logo/logo.png`
- ✅ Copied to `/local/wth_umr2/` for easy dashboard access
- ✅ Available immediately after installation (no manual setup needed)

**Quick Start:**
Add this card to your dashboard to see the logo:
```yaml
type: picture
image: /local/wth_umr2/logo.png
```

For more examples, see [DASHBOARD_CARDS_WITH_LOGO.md](DASHBOARD_CARDS_WITH_LOGO.md)

**Technical Details:** See [AUTO_LOGO_LOADING.md](AUTO_LOGO_LOADING.md) for how it works.

**Integration List Icon:** The integration list shows `mdi:radiator` 🔥 (Home Assistant limitation for custom integrations). To get the WTH logo in the integration list, submit to [Home Assistant Brands](https://github.com/home-assistant/brands) - files ready in `brands_submission/` folder.

## Features

- **GUI Configuration**: Easy setup through Home Assistant's UI
- **Comprehensive Monitoring**: Access to all data points provided by the WTH UMR2
- **Real-time Updates**: Polls the device every 30 seconds for current status
- **Multiple Sensors**: Over 60 sensor entities covering:
  - Main system state and mode
  - Thermostat states and temperatures (8 zones)
  - Valve positions (10 valves)
  - Heater and cooler outputs
  - Pump speed
  - Temperature sensors (10 sensors)
  - Communication status (Fanlink, RF, Modbus, Bluetooth, Ethernet)
  - Connected devices

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Go to "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add this repository URL and select "Integration" as the category
6. Click "Install"
7. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/wth_umr2` folder to your Home Assistant's `custom_components` directory
2. If the `custom_components` directory doesn't exist, create it in your Home Assistant configuration directory
3. Restart Home Assistant

## Configuration

1. Go to **Settings** → **Devices & Services**
2. Click **+ ADD INTEGRATION**
3. Search for "WTH UMR2 Regulator"
4. Enter the IP address of your WTH UMR2 device (e.g., `YOUR.WTH.IP.ADDRESS`)
5. Click **Submit**

The integration will automatically discover all available sensors and create entities for them.

## Available Sensors

### Main Status
- **Main State**: Overall system state
- **Operating Mode**: Current mode (heating/cooling)
- **Display**: Current display value
- **LED Status**: LED indicator state
- **Heat Factor**: Heating factor percentage
- **Cool Factor**: Cooling factor percentage
- **PWM Factor**: PWM control percentage

### Outputs
- **Heater Output**: Heater power percentage
- **Cooler Output**: Cooler power percentage
- **Pump Speed**: Circulation pump speed percentage
- **Valve 1-10**: Individual valve positions (0-100%)

### Thermostats (8 zones)
- **Thermostat 1-8**: On/off state with temperature and setpoint attributes
- **Thermostat 1-8 Temperature**: Current temperature readings

### Inputs
- **Max Input**: Maximum temperature input status
- **Return Input**: Return temperature input status
- **Condens Input**: Condensation sensor status
- **Temperature Sensor 1-10**: External temperature sensors

### Communications
- **Fanlink Status**: Fanlink communication state
- **RF Status**: RF communication state
- **Modbus Status**: Modbus communication state
- **Bluetooth Status**: Bluetooth communication state
- **Ethernet Status**: Network connection state with IP details
- **Fanlink Device 1-10**: Connected Fanlink devices with serial numbers

## Entity Attributes

Many sensors include additional attributes with detailed information:

- **Thermostat sensors**: Include temperature, setpoint, and on/off states
- **Communication sensors**: Include IP addresses, MAC addresses, and device details
- **Device sensors**: Include serial numbers, last seen timestamps, and device types

## Troubleshooting

### Cannot Connect
- Verify the IP address is correct
- Ensure the WTH UMR2 is powered on and connected to your network
- Check that Home Assistant can reach the device (try pinging it)
- Verify the URL `http://YOUR_IP/get.json?f=$.status.*` returns valid JSON in a browser

### Invalid Response
- Ensure you're connecting to a WTH UMR2 device
- Check that the device firmware is up to date
- Verify the JSON endpoint is accessible

### Missing Sensors
- Some sensors may not appear if the corresponding hardware is not connected
- Temperature sensors with zero values are hidden until they report actual data
- Not all 10 temperature sensors or valves may be in use

## Advanced Configuration

### Polling Interval
The default polling interval is 30 seconds. To change this, modify the `SCAN_INTERVAL` in `__init__.py`:

```python
SCAN_INTERVAL = timedelta(seconds=30)  # Change to your preferred interval
```

### Device Information
The integration automatically extracts:
- Device ID
- Firmware version
- Hardware version
- Model information

## Support

For issues, feature requests, or contributions, please visit the GitHub repository.

## License

This integration is provided as-is for personal use with WTH UMR2 heating regulators.

## Changelog

### Version 1.0
- Initial release
- Full support for all JSON data points
- GUI configuration with logo support
- Comprehensive sensor coverage (60+ sensors)
- Real-time updates every 30 seconds
- English and Dutch language support
- Device information with hardware and firmware versions
- Direct configuration URL to device web interface
