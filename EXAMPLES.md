# Usage Examples - WTH UMR2 Integration

## Entity Overview

After setup, you'll have access to 60+ sensor entities organized by category.

## Entity Naming Convention

All entities follow this pattern:
```
sensor.wth_umr2_regulator_[sensor_name]
```

Example entities:
- `sensor.wth_umr2_regulator_main_state`
- `sensor.wth_umr2_regulator_thermostat_1_temperature`
- `sensor.wth_umr2_regulator_valve_3`

## Dashboard Examples

### Example 1: Main Status Card

```yaml
type: entities
title: WTH UMR2 Main Status
entities:
  - entity: sensor.wth_umr2_regulator_main_state
    name: System State
  - entity: sensor.wth_umr2_regulator_operating_mode
    name: Mode
  - entity: sensor.wth_umr2_regulator_display
    name: Display
  - entity: sensor.wth_umr2_regulator_heat_factor
    name: Heat Factor
  - entity: sensor.wth_umr2_regulator_pump_speed
    name: Pump Speed
```

### Example 2: Thermostats Overview

```yaml
type: grid
cards:
  - type: tile
    entity: sensor.wth_umr2_regulator_thermostat_1_temperature
    name: Living Room
    icon: mdi:sofa
  - type: tile
    entity: sensor.wth_umr2_regulator_thermostat_2_temperature
    name: Bedroom
    icon: mdi:bed
  - type: tile
    entity: sensor.wth_umr2_regulator_thermostat_3_temperature
    name: Kitchen
    icon: mdi:chef-hat
  - type: tile
    entity: sensor.wth_umr2_regulator_thermostat_4_temperature
    name: Bathroom
    icon: mdi:shower
columns: 2
```

### Example 3: Heating System Status

```yaml
type: vertical-stack
cards:
  - type: gauge
    entity: sensor.wth_umr2_regulator_heater_output
    name: Heater Power
    min: 0
    max: 100
    severity:
      green: 0
      yellow: 50
      red: 80
  - type: gauge
    entity: sensor.wth_umr2_regulator_pump_speed
    name: Pump Speed
    min: 0
    max: 100
  - type: entities
    title: Output Status
    entities:
      - sensor.wth_umr2_regulator_heater_output
      - sensor.wth_umr2_regulator_cooler_output
      - sensor.wth_umr2_regulator_pump_speed
```

### Example 4: Valve Positions

```yaml
type: horizontal-stack
cards:
  - type: gauge
    entity: sensor.wth_umr2_regulator_valve_1
    name: Zone 1
    min: 0
    max: 100
  - type: gauge
    entity: sensor.wth_umr2_regulator_valve_2
    name: Zone 2
    min: 0
    max: 100
  - type: gauge
    entity: sensor.wth_umr2_regulator_valve_3
    name: Zone 3
    min: 0
    max: 100
  - type: gauge
    entity: sensor.wth_umr2_regulator_valve_4
    name: Zone 4
    min: 0
    max: 100
```

### Example 5: Complete Overview Dashboard

```yaml
title: Heating System
views:
  - title: Overview
    cards:
      - type: entities
        title: System Status
        entities:
          - sensor.wth_umr2_regulator_main_state
          - sensor.wth_umr2_regulator_operating_mode
          - sensor.wth_umr2_regulator_heat_factor
          - sensor.wth_umr2_regulator_pump_speed
      
      - type: grid
        title: Zone Temperatures
        columns: 3
        cards:
          - type: sensor
            entity: sensor.wth_umr2_regulator_thermostat_1_temperature
            name: Zone 1
          - type: sensor
            entity: sensor.wth_umr2_regulator_thermostat_2_temperature
            name: Zone 2
          - type: sensor
            entity: sensor.wth_umr2_regulator_thermostat_3_temperature
            name: Zone 3
          - type: sensor
            entity: sensor.wth_umr2_regulator_thermostat_4_temperature
            name: Zone 4
          - type: sensor
            entity: sensor.wth_umr2_regulator_thermostat_5_temperature
            name: Zone 5
          - type: sensor
            entity: sensor.wth_umr2_regulator_thermostat_6_temperature
            name: Zone 6
      
      - type: horizontal-stack
        cards:
          - type: gauge
            entity: sensor.wth_umr2_regulator_heater_output
            name: Heater
            min: 0
            max: 100
          - type: gauge
            entity: sensor.wth_umr2_regulator_cooler_output
            name: Cooler
            min: 0
            max: 100

  - title: Details
    cards:
      - type: entities
        title: All Thermostats
        entities:
          - sensor.wth_umr2_regulator_thermostat_1
          - sensor.wth_umr2_regulator_thermostat_1_temperature
          - sensor.wth_umr2_regulator_thermostat_2
          - sensor.wth_umr2_regulator_thermostat_2_temperature
          - sensor.wth_umr2_regulator_thermostat_3
          - sensor.wth_umr2_regulator_thermostat_3_temperature
          - sensor.wth_umr2_regulator_thermostat_4
          - sensor.wth_umr2_regulator_thermostat_4_temperature
          - sensor.wth_umr2_regulator_thermostat_5
          - sensor.wth_umr2_regulator_thermostat_5_temperature
          - sensor.wth_umr2_regulator_thermostat_6
          - sensor.wth_umr2_regulator_thermostat_6_temperature
          - sensor.wth_umr2_regulator_thermostat_7
          - sensor.wth_umr2_regulator_thermostat_7_temperature
          - sensor.wth_umr2_regulator_thermostat_8
          - sensor.wth_umr2_regulator_thermostat_8_temperature
      
      - type: entities
        title: All Valves
        entities:
          - sensor.wth_umr2_regulator_valve_1
          - sensor.wth_umr2_regulator_valve_2
          - sensor.wth_umr2_regulator_valve_3
          - sensor.wth_umr2_regulator_valve_4
          - sensor.wth_umr2_regulator_valve_5
          - sensor.wth_umr2_regulator_valve_6
          - sensor.wth_umr2_regulator_valve_7
          - sensor.wth_umr2_regulator_valve_8
          - sensor.wth_umr2_regulator_valve_9
          - sensor.wth_umr2_regulator_valve_10
      
      - type: entities
        title: Communications
        entities:
          - sensor.wth_umr2_regulator_fanlink_status
          - sensor.wth_umr2_regulator_rf_status
          - sensor.wth_umr2_regulator_modbus_status
          - sensor.wth_umr2_regulator_bluetooth_status
          - sensor.wth_umr2_regulator_ethernet_status
```

## Automation Examples

### Example 1: Alert on System Error

```yaml
automation:
  - alias: "WTH UMR2 System Alert"
    trigger:
      - platform: state
        entity_id: sensor.wth_umr2_regulator_main_state
        to: "Error"
    action:
      - service: notify.mobile_app
        data:
          title: "Heating System Error"
          message: "WTH UMR2 reports an error condition"
```

### Example 2: Monitor Pump Speed

```yaml
automation:
  - alias: "WTH UMR2 High Pump Speed Alert"
    trigger:
      - platform: numeric_state
        entity_id: sensor.wth_umr2_regulator_pump_speed
        above: 80
        for:
          minutes: 10
    action:
      - service: notify.persistent_notification
        data:
          title: "Pump Running High"
          message: "Heating pump has been running at >80% for 10 minutes"
```

### Example 3: Temperature Drop Alert

```yaml
automation:
  - alias: "Zone Temperature Drop"
    trigger:
      - platform: numeric_state
        entity_id: sensor.wth_umr2_regulator_thermostat_1_temperature
        below: 18
    action:
      - service: notify.mobile_app
        data:
          title: "Low Temperature"
          message: "Living room temperature below 18°C"
```

### Example 4: Connection Monitor

```yaml
automation:
  - alias: "WTH UMR2 Connection Lost"
    trigger:
      - platform: state
        entity_id: sensor.wth_umr2_regulator_main_state
        to: "unavailable"
        for:
          minutes: 5
    action:
      - service: notify.mobile_app
        data:
          title: "Heating System Offline"
          message: "Lost connection to WTH UMR2 regulator"
```

## Template Sensors

### Example 1: Total Active Zones

```yaml
template:
  - sensor:
      - name: "WTH Active Zones"
        state: >
          {% set ns = namespace(count=0) %}
          {% for i in range(1, 9) %}
            {% set entity = 'sensor.wth_umr2_regulator_thermostat_' ~ i %}
            {% if states(entity) == 'on' %}
              {% set ns.count = ns.count + 1 %}
            {% endif %}
          {% endfor %}
          {{ ns.count }}
        unit_of_measurement: "zones"
```

### Example 2: Average Zone Temperature

```yaml
template:
  - sensor:
      - name: "WTH Average Temperature"
        unit_of_measurement: "°C"
        device_class: temperature
        state: >
          {% set temps = [
            states('sensor.wth_umr2_regulator_thermostat_1_temperature') | float(0),
            states('sensor.wth_umr2_regulator_thermostat_2_temperature') | float(0),
            states('sensor.wth_umr2_regulator_thermostat_3_temperature') | float(0),
            states('sensor.wth_umr2_regulator_thermostat_4_temperature') | float(0)
          ] %}
          {% set valid_temps = temps | select('>', 0) | list %}
          {% if valid_temps | length > 0 %}
            {{ (valid_temps | sum / (valid_temps | length)) | round(1) }}
          {% else %}
            unknown
          {% endif %}
```

### Example 3: System Efficiency

```yaml
template:
  - sensor:
      - name: "WTH Heating Efficiency"
        unit_of_measurement: "%"
        state: >
          {% set heat = states('sensor.wth_umr2_regulator_heater_output') | float(0) %}
          {% set pump = states('sensor.wth_umr2_regulator_pump_speed') | float(0) %}
          {% if pump > 0 %}
            {{ ((heat / pump) * 100) | round(0) }}
          {% else %}
            0
          {% endif %}
```

## Entity Attribute Access

Many entities have rich attributes. Here's how to access them:

### Thermostat Attributes

```yaml
# In automations or templates
{{ state_attr('sensor.wth_umr2_regulator_thermostat_1', 'setpoint') }}
{{ state_attr('sensor.wth_umr2_regulator_thermostat_1', 'temperature') }}
{{ state_attr('sensor.wth_umr2_regulator_thermostat_1', 'process_state') }}
```

### Ethernet Status Attributes

```yaml
{{ state_attr('sensor.wth_umr2_regulator_ethernet_status', 'ip_address') }}
{{ state_attr('sensor.wth_umr2_regulator_ethernet_status', 'mac_address') }}
{{ state_attr('sensor.wth_umr2_regulator_ethernet_status', 'dhcp') }}
```

### Fanlink Device Attributes

```yaml
{{ state_attr('sensor.wth_umr2_regulator_fanlink_device_1', 'serial_number') }}
{{ state_attr('sensor.wth_umr2_regulator_fanlink_device_1', 'last_seen') }}
```

## History and Statistics

Track heating patterns over time:

```yaml
type: history-graph
entities:
  - sensor.wth_umr2_regulator_thermostat_1_temperature
  - sensor.wth_umr2_regulator_heater_output
  - sensor.wth_umr2_regulator_pump_speed
hours_to_show: 24
```

## Energy Dashboard Integration

While the WTH UMR2 doesn't provide direct energy measurements, you can track efficiency:

```yaml
# Create utility meter for heater runtime
utility_meter:
  heater_daily_runtime:
    source: sensor.wth_umr2_regulator_heater_output
    cycle: daily
```

## Conditional Cards

Show cards only when relevant:

```yaml
type: conditional
conditions:
  - entity: sensor.wth_umr2_regulator_operating_mode
    state: "heating"
card:
  type: gauge
  entity: sensor.wth_umr2_regulator_heater_output
  name: Current Heating Output
```

## Mobile Notifications

Quick glance card for mobile:

```yaml
type: glance
entities:
  - sensor.wth_umr2_regulator_main_state
  - sensor.wth_umr2_regulator_operating_mode
  - sensor.wth_umr2_regulator_heater_output
  - sensor.wth_umr2_regulator_pump_speed
title: Heating Status
```

## Tips

1. **Customize entity names**: Go to entity settings to give meaningful names to thermostats (e.g., "Living Room" instead of "Thermostat 1")

2. **Hide unused entities**: If you're not using all 10 valves or temperature sensors, disable unused entities to keep your interface clean

3. **Create areas**: Assign the WTH UMR2 device to a specific area (e.g., "Utility Room") for better organization

4. **Use groups**: Create groups of related sensors for easier management

5. **Set up alerts**: Configure automations to notify you of important state changes

6. **Monitor trends**: Use the history card to identify patterns in heating behavior

7. **Create scenes**: Although this integration is read-only, you can use the data to trigger other automations or scenes
