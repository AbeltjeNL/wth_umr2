# Ready-to-Use Dashboard Cards with WTH Logo

Copy and paste these card configurations into your Home Assistant dashboard.

## Card 1: Logo Header with Status

```yaml
type: vertical-stack
cards:
  - type: picture
    image: /local/wth_umr2/logo.png
    tap_action:
      action: none
  - type: entities
    title: WTH UMR2 Status
    entities:
      - entity: sensor.wth_umr2_regulator_main_state
        name: System State
      - entity: sensor.wth_umr2_regulator_operating_mode
        name: Mode
      - entity: sensor.wth_umr2_regulator_heat_factor
        name: Heat Factor
      - entity: sensor.wth_umr2_regulator_pump_speed
        name: Pump Speed
```

## Card 2: Compact Logo Badge

```yaml
type: horizontal-stack
cards:
  - type: picture
    image: /api/wth_umr2/logo/logo.png
  - type: glance
    entities:
      - sensor.wth_umr2_regulator_main_state
      - sensor.wth_umr2_regulator_heat_factor
      - sensor.wth_umr2_regulator_pump_speed
    title: WTH UMR2
```

## Card 3: Logo with Gauges

```yaml
type: vertical-stack
cards:
  - type: picture
    image: /local/wth_umr2/logo.png
    tap_action:
      action: none
  - type: horizontal-stack
    cards:
      - type: gauge
        entity: sensor.wth_umr2_regulator_heat_factor
        name: Heat
        min: 0
        max: 100
      - type: gauge
        entity: sensor.wth_umr2_regulator_pump_speed
        name: Pump
        min: 0
        max: 100
```

## Card 4: Logo Background (Requires custom:button-card)

```yaml
type: custom:button-card
entity: sensor.wth_umr2_regulator_main_state
name: WTH UMR2 Regulator
show_state: true
show_icon: false
styles:
  card:
    - height: 200px
    - background-image: url('/local/wth_umr2/logo.png')
    - background-size: 80%
    - background-repeat: no-repeat
    - background-position: center 20%
  name:
    - margin-top: 120px
    - font-size: 18px
  state:
    - font-size: 14px
```

## Card 5: Markdown Card with Logo

```yaml
type: markdown
content: |
  ![WTH Logo](/local/wth_umr2/logo.png)
  
  # WTH UMR2 System
  
  **Status:** {{ states('sensor.wth_umr2_regulator_main_state') }}
  
  **Mode:** {{ states('sensor.wth_umr2_regulator_operating_mode') }}
  
  **Heat Factor:** {{ states('sensor.wth_umr2_regulator_heat_factor') }}%
  
  **Pump Speed:** {{ states('sensor.wth_umr2_regulator_pump_speed') }}%
```

## Card 6: Picture Elements Dashboard

```yaml
type: picture-elements
image: /local/wth_umr2/logo.png
elements:
  - type: state-label
    entity: sensor.wth_umr2_regulator_main_state
    style:
      top: 85%
      left: 25%
      font-size: 16px
      font-weight: bold
  - type: state-label
    entity: sensor.wth_umr2_regulator_heat_factor
    prefix: 'Heat: '
    suffix: '%'
    style:
      top: 92%
      left: 25%
  - type: state-label
    entity: sensor.wth_umr2_regulator_pump_speed
    prefix: 'Pump: '
    suffix: '%'
    style:
      top: 92%
      left: 75%
```

## Card 7: Mobile-Friendly Quick View

```yaml
type: glance
title: WTH UMR2
show_name: true
show_state: true
columns: 3
entities:
  - entity: sensor.wth_umr2_regulator_main_state
    name: Status
  - entity: sensor.wth_umr2_regulator_operating_mode
    name: Mode
  - entity: sensor.wth_umr2_regulator_heat_factor
    name: Heat
  - entity: sensor.wth_umr2_regulator_pump_speed
    name: Pump
  - entity: sensor.wth_umr2_regulator_thermostat_1_temperature
    name: Zone 1
  - entity: sensor.wth_umr2_regulator_thermostat_2_temperature
    name: Zone 2
```

## Card 8: Detailed Dashboard with Logo Header

```yaml
type: vertical-stack
cards:
  - type: picture
    image: /local/wth_umr2/logo.png
    tap_action:
      action: url
      url_path: http://192.168.178.69
  - type: entities
    title: System Status
    entities:
      - sensor.wth_umr2_regulator_main_state
      - sensor.wth_umr2_regulator_operating_mode
      - sensor.wth_umr2_regulator_display
      - sensor.wth_umr2_regulator_led_status
  - type: entities
    title: Heating
    entities:
      - sensor.wth_umr2_regulator_heat_factor
      - sensor.wth_umr2_regulator_cool_factor
      - sensor.wth_umr2_regulator_pwm_factor
      - sensor.wth_umr2_regulator_heater_output
      - sensor.wth_umr2_regulator_pump_speed
  - type: entities
    title: Zones
    entities:
      - sensor.wth_umr2_regulator_thermostat_1_temperature
      - sensor.wth_umr2_regulator_thermostat_2_temperature
      - sensor.wth_umr2_regulator_thermostat_3_temperature
```

## Logo Access Methods

You can use either path for logos:

**Method 1: WWW Directory (Recommended)**
```yaml
image: /local/wth_umr2/logo.png
```

**Method 2: API Endpoint**
```yaml
image: /api/wth_umr2/logo/logo.png
```

Both work identically!

## Available Logo Files

- `/local/wth_umr2/logo.png` - Main logo (256x256)
- `/local/wth_umr2/icon.png` - Icon (128x128)
- `/local/wth_umr2/icon@2x.png` - HD icon (256x256)
- `/local/wth_umr2/icon.svg` - Vector logo

## Customization Tips

### Adjust Logo Size

```yaml
image: /local/wth_umr2/logo.png
style: |
  img {
    max-width: 200px;
  }
```

### Center Logo

```yaml
image: /local/wth_umr2/logo.png
style: |
  ha-card {
    text-align: center;
  }
```

### Add Padding

```yaml
style: |
  ha-card {
    padding: 20px;
  }
```

## Installation

1. Install WTH UMR2 integration
2. Wait for Home Assistant to restart
3. Logos are automatically available at `/local/wth_umr2/`
4. Copy any card example above
5. Paste into dashboard (Edit Dashboard → Add Card → Manual Card)

## Troubleshooting

**Logo not showing?**

1. Verify integration is loaded:
   ```
   Settings → Devices & Services → WTH UMR2 Regulator
   ```

2. Check logo is accessible:
   ```
   http://YOUR_HA_IP:8123/local/wth_umr2/logo.png
   ```

3. Clear browser cache:
   ```
   Ctrl+Shift+R (Windows/Linux)
   Cmd+Shift+R (Mac)
   ```

4. Restart Home Assistant

**Wrong entity names?**

Replace `sensor.wth_umr2_regulator_*` with your actual entity IDs from:
```
Developer Tools → States → Filter: wth_umr2
```

## Need More Help?

- See: AUTO_LOGO_LOADING.md for technical details
- See: EXAMPLES.md for advanced configurations
- Issues: https://github.com/AbeltjeNL/wth_umr2/issues
