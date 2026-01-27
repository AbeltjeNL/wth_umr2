# WTH UMR2 Regulator Integration for Home Assistant

![WTH Logo](custom_components/wth_umr2/logo.png)

**Version:** 1.0  
**Author:** AbeltjeNL  
**License:** MIT

This custom component integrates the WTH UMR2 heating regulator with Home Assistant, allowing you to monitor and control your heating system.

> [!NOTE]
> This integration has no affiliation whatsoever with the brand or company WTH. All logo's used are publicly available on Google images.

> [!CAUTION]
**Do note that this integration is writen using Claude.ai !**
**No manual coding or manual labor has been put in to this integration**

## 🎨 Logo Display

The WTH logo is included in this integration but requires additional setup to display in Home Assistant. See [ENABLE_LOGO.md](ENABLE_LOGO.md) for detailed instructions on how to make the logo appear in your dashboard and integration list.

**Quick summary:** Custom integrations don't show logos automatically in Home Assistant. You can either:
1. Copy the logo to your `www` folder and use it in dashboard cards (easy, 5 minutes)
2. Submit the integration to Home Assistant Brands repository (for everyone, but requires approval)

For full details, see the [Logo Display Guide](LOGO_DISPLAY_GUIDE.md).

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
4. Enter the IP address of your WTH UMR2 device (e.g., `192.168.178.69`)
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

> [!NOTE]
**Note that this integration works and does what it should do. I'm not planning on expanding or maintaining this integration unless is breaks or throws warnings/errors in the Home Assistant logs.**
