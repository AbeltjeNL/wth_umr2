# Quick Start Guide - WTH UMR2 Integration

## Installation (5 minutes)

1. **Copy Integration Files**
   ```
   Copy the 'custom_components/wth_umr2' folder to your Home Assistant config directory
   ```

2. **Restart Home Assistant**
   - Settings → System → Restart

3. **Add Integration**
   - Settings → Devices & Services → Add Integration
   - Search for "WTH UMR2 Regulator"
   - Enter IP address: `192.168.178.69` (or your device's IP)
   - Submit

4. **Done!**
   - You now have 60+ sensors available

## What You Get

### Main Sensors
- ✅ System state and mode
- ✅ Heat/Cool/PWM factors
- ✅ Pump speed
- ✅ Display and LED status

### Zone Control
- ✅ 8 Thermostat sensors (on/off + temperature)
- ✅ 10 Valve position sensors

### Monitoring
- ✅ 10 Temperature sensors
- ✅ Input status (max, return, condens)
- ✅ Communication status (Fanlink, RF, Modbus, Bluetooth, Ethernet)
- ✅ Connected device info

## Quick Dashboard

Add this to your dashboard (YAML mode):

```yaml
type: entities
title: Heating System
entities:
  - sensor.wth_umr2_regulator_main_state
  - sensor.wth_umr2_regulator_operating_mode
  - sensor.wth_umr2_regulator_heater_output
  - sensor.wth_umr2_regulator_pump_speed
  - sensor.wth_umr2_regulator_thermostat_1_temperature
  - sensor.wth_umr2_regulator_thermostat_2_temperature
```

## Quick Automation

Alert on system errors:

```yaml
automation:
  - alias: "Heating System Alert"
    trigger:
      - platform: state
        entity_id: sensor.wth_umr2_regulator_main_state
        to: "Error"
    action:
      - service: notify.mobile_app
        data:
          message: "Heating system error detected!"
```

## Troubleshooting

**Can't find integration?**
- Check files are in `config/custom_components/wth_umr2/`
- Restart Home Assistant again
- Clear browser cache

**Can't connect?**
- Verify IP address is correct
- Test in browser: `http://YOUR_IP/get.json?f=$.status.*`
- Check device is on same network

**Missing sensors?**
- Some sensors only appear when hardware is connected
- Temperature sensors with 0.0°C are hidden
- This is normal behavior

## Need More Help?

- 📖 Full documentation: See README.md
- 🔧 Detailed installation: See INSTALLATION.md
- 💡 Usage examples: See EXAMPLES.md

## File Structure

```
wth_umr2/
├── custom_components/
│   └── wth_umr2/
│       ├── __init__.py          # Main integration logic
│       ├── config_flow.py       # GUI setup
│       ├── const.py             # Constants
│       ├── manifest.json        # Integration metadata
│       ├── sensor.py            # All sensor entities
│       ├── strings.json         # UI strings
│       └── translations/
│           └── en.json          # English translations
├── README.md                    # Main documentation
├── INSTALLATION.md              # Detailed installation guide
├── EXAMPLES.md                  # Usage examples
└── QUICK_START.md              # This file
```

## Entity Naming

All entities follow this pattern:
```
sensor.wth_umr2_regulator_[sensor_name]
```

Examples:
- `sensor.wth_umr2_regulator_heater_output`
- `sensor.wth_umr2_regulator_thermostat_1`
- `sensor.wth_umr2_regulator_valve_3`

## Update Interval

The integration polls your WTH UMR2 every 30 seconds for fresh data.

## Customization

Rename sensors for your zones:
1. Go to entity settings
2. Change "Thermostat 1" → "Living Room"
3. Now it shows as "Living Room" everywhere!

## Support

Having issues? Check the logs:
- Settings → System → Logs
- Search for "wth_umr2"

---

**🎉 You're ready to monitor your heating system!**
