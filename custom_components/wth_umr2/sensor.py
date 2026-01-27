"""Sensor platform for WTH UMR2 Regulator."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    PERCENTAGE,
    UnitOfTemperature,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import WTHCoordinator
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up WTH UMR2 sensor based on a config entry."""
    coordinator: WTHCoordinator = hass.data[DOMAIN][entry.entry_id]
    
    entities = []
    
    # Main status sensors
    entities.append(WTHMainStateSensor(coordinator, entry))
    entities.append(WTHModeSensor(coordinator, entry))
    entities.append(WTHDisplaySensor(coordinator, entry))
    entities.append(WTHLEDSensor(coordinator, entry))
    entities.append(WTHHeatFactorSensor(coordinator, entry))
    entities.append(WTHCoolFactorSensor(coordinator, entry))
    entities.append(WTHPWMFactorSensor(coordinator, entry))
    
    # Heater output sensor
    entities.append(WTHHeaterSensor(coordinator, entry))
    
    # Cooler output sensor
    entities.append(WTHCoolerSensor(coordinator, entry))
    
    # Pump speed sensor
    entities.append(WTHPumpSpeedSensor(coordinator, entry))
    
    # Thermostat sensors (8 thermostats)
    for i in range(8):
        entities.append(WTHThermostatSensor(coordinator, entry, i))
        entities.append(WTHThermostatTemperatureSensor(coordinator, entry, i))
    
    # Valve sensors (10 valves)
    for i in range(10):
        entities.append(WTHValveSensor(coordinator, entry, i))
    
    # Input sensors
    entities.append(WTHMaxInputSensor(coordinator, entry))
    entities.append(WTHReturnInputSensor(coordinator, entry))
    entities.append(WTHCondensInputSensor(coordinator, entry))
    
    # Temperature sensors (10 sensors)
    for i in range(10):
        entities.append(WTHTemperatureSensor(coordinator, entry, i))
    
    # Communication status sensors
    entities.append(WTHFanlinkStatusSensor(coordinator, entry))
    entities.append(WTHRFStatusSensor(coordinator, entry))
    entities.append(WTHModbusStatusSensor(coordinator, entry))
    entities.append(WTHBluetoothStatusSensor(coordinator, entry))
    entities.append(WTHEthernetStatusSensor(coordinator, entry))
    
    # Fanlink devices
    for i in range(10):
        entities.append(WTHFanlinkDeviceSensor(coordinator, entry, i))
    
    async_add_entities(entities)


class WTHBaseSensor(CoordinatorEntity, SensorEntity):
    """Base class for WTH UMR2 sensors."""

    def __init__(self, coordinator: WTHCoordinator, entry: ConfigEntry) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._entry = entry
        self._attr_has_entity_name = True

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        device_id = self.coordinator.data.get("id", self._entry.entry_id)
        return DeviceInfo(
            identifiers={(DOMAIN, self._entry.entry_id)},
            name="WTH UMR2 Regulator",
            manufacturer="WTH",
            model="UMR2",
            sw_version=self.coordinator.data.get("version", {}).get("fw", "Unknown"),
            hw_version=self.coordinator.data.get("version", {}).get("hw", "Unknown"),
            configuration_url=f"http://{self.coordinator.host}",
        )


class WTHMainStateSensor(WTHBaseSensor):
    """Sensor for main state."""

    _attr_name = "Main State"
    _attr_icon = "mdi:state-machine"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_main_state"

    @property
    def native_value(self) -> str | None:
        """Return the state."""
        return self.coordinator.data.get("main", {}).get("state")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        main = self.coordinator.data.get("main", {})
        return {
            "message": main.get("message"),
            "kick": main.get("kick"),
            "button": main.get("button"),
            "night_lower_active": main.get("nightLowerActive"),
            "master_umr": main.get("masterUMR"),
            "slave_hc_factor": main.get("slaveHcFactor"),
            "slave_pwm_factor": main.get("slavePwmFactor"),
        }


class WTHModeSensor(WTHBaseSensor):
    """Sensor for operating mode."""

    _attr_name = "Operating Mode"
    _attr_icon = "mdi:thermostat"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_mode"

    @property
    def native_value(self) -> str | None:
        """Return the mode."""
        return self.coordinator.data.get("main", {}).get("mode")


class WTHDisplaySensor(WTHBaseSensor):
    """Sensor for display value."""

    _attr_name = "Display"
    _attr_icon = "mdi:monitor"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_display"

    @property
    def native_value(self) -> str | None:
        """Return the display value."""
        return self.coordinator.data.get("main", {}).get("display")


class WTHLEDSensor(WTHBaseSensor):
    """Sensor for LED status."""

    _attr_name = "LED Status"
    _attr_icon = "mdi:led-on"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_led"

    @property
    def native_value(self) -> str | None:
        """Return the LED status."""
        return self.coordinator.data.get("main", {}).get("led")


class WTHHeatFactorSensor(WTHBaseSensor):
    """Sensor for heat factor."""

    _attr_name = "Heat Factor"
    _attr_icon = "mdi:fire"
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_heat_factor"

    @property
    def native_value(self) -> int | None:
        """Return the heat factor."""
        return self.coordinator.data.get("main", {}).get("heatFactor")


class WTHCoolFactorSensor(WTHBaseSensor):
    """Sensor for cool factor."""

    _attr_name = "Cool Factor"
    _attr_icon = "mdi:snowflake"
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_cool_factor"

    @property
    def native_value(self) -> int | None:
        """Return the cool factor."""
        return self.coordinator.data.get("main", {}).get("coolFactor")


class WTHPWMFactorSensor(WTHBaseSensor):
    """Sensor for PWM factor."""

    _attr_name = "PWM Factor"
    _attr_icon = "mdi:sine-wave"
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_pwm_factor"

    @property
    def native_value(self) -> int | None:
        """Return the PWM factor."""
        return self.coordinator.data.get("main", {}).get("pwmFactor")


class WTHHeaterSensor(WTHBaseSensor):
    """Sensor for heater output."""

    _attr_name = "Heater Output"
    _attr_icon = "mdi:radiator"
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_heater_output"

    @property
    def native_value(self) -> int | None:
        """Return the heater factor."""
        return self.coordinator.data.get("outputs", {}).get("heater", {}).get("factor")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        heater = self.coordinator.data.get("outputs", {}).get("heater", {})
        return {
            "mode": heater.get("mode"),
        }


class WTHCoolerSensor(WTHBaseSensor):
    """Sensor for cooler output."""

    _attr_name = "Cooler Output"
    _attr_icon = "mdi:air-conditioner"
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_cooler_output"

    @property
    def native_value(self) -> int | None:
        """Return the cooler factor."""
        return self.coordinator.data.get("outputs", {}).get("cooler", {}).get("factor")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        cooler = self.coordinator.data.get("outputs", {}).get("cooler", {})
        return {
            "mode": cooler.get("mode"),
        }


class WTHPumpSpeedSensor(WTHBaseSensor):
    """Sensor for pump speed."""

    _attr_name = "Pump Speed"
    _attr_icon = "mdi:pump"
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_pump_speed"

    @property
    def native_value(self) -> int | None:
        """Return the pump speed."""
        return self.coordinator.data.get("outputs", {}).get("pump", {}).get("speed")


class WTHThermostatSensor(WTHBaseSensor):
    """Sensor for thermostat status."""

    def __init__(self, coordinator: WTHCoordinator, entry: ConfigEntry, index: int) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, entry)
        self._index = index
        self._attr_name = f"Thermostat {index + 1}"
        self._attr_icon = "mdi:thermostat"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_thermostat_{self._index}"

    @property
    def native_value(self) -> str | None:
        """Return the thermostat state."""
        thermostats = self.coordinator.data.get("inputs", {}).get("thermostats", [])
        if self._index < len(thermostats):
            return "on" if thermostats[self._index].get("isOn") else "off"
        return None

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        # Get both input and process thermostat data
        input_thermostats = self.coordinator.data.get("inputs", {}).get("thermostats", [])
        process_thermostats = self.coordinator.data.get("process", {}).get("thermostats", [])
        
        attrs = {}
        if self._index < len(input_thermostats):
            attrs["input_state"] = input_thermostats[self._index].get("isOn")
        
        if self._index < len(process_thermostats):
            process_data = process_thermostats[self._index]
            attrs["process_state"] = process_data.get("isOn")
            attrs["temperature"] = process_data.get("temperature")
            attrs["setpoint"] = process_data.get("setpoint")
        
        return attrs


class WTHThermostatTemperatureSensor(WTHBaseSensor):
    """Sensor for thermostat temperature."""

    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: WTHCoordinator, entry: ConfigEntry, index: int) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, entry)
        self._index = index
        self._attr_name = f"Thermostat {index + 1} Temperature"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_thermostat_{self._index}_temp"

    @property
    def native_value(self) -> float | None:
        """Return the temperature."""
        thermostats = self.coordinator.data.get("process", {}).get("thermostats", [])
        if self._index < len(thermostats):
            temp = thermostats[self._index].get("temperature", 0.0)
            return temp if temp > 0 else None
        return None

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        thermostats = self.coordinator.data.get("process", {}).get("thermostats", [])
        if self._index < len(thermostats):
            return {
                "setpoint": thermostats[self._index].get("setpoint"),
            }
        return {}


class WTHValveSensor(WTHBaseSensor):
    """Sensor for valve state."""

    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_icon = "mdi:valve"

    def __init__(self, coordinator: WTHCoordinator, entry: ConfigEntry, index: int) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, entry)
        self._index = index
        self._attr_name = f"Valve {index + 1}"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_valve_{self._index}"

    @property
    def native_value(self) -> int | None:
        """Return the valve state."""
        valves = self.coordinator.data.get("outputs", {}).get("valves", [])
        if self._index < len(valves):
            return valves[self._index].get("state")
        return None


class WTHMaxInputSensor(WTHBaseSensor):
    """Sensor for max input."""

    _attr_name = "Max Input"
    _attr_icon = "mdi:thermometer-alert"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_max_input"

    @property
    def native_value(self) -> str | None:
        """Return the state."""
        return self.coordinator.data.get("inputs", {}).get("max", {}).get("state")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        max_input = self.coordinator.data.get("inputs", {}).get("max", {})
        return {
            "message": max_input.get("message"),
            "temperature": max_input.get("temperature"),
        }


class WTHReturnInputSensor(WTHBaseSensor):
    """Sensor for return input."""

    _attr_name = "Return Input"
    _attr_icon = "mdi:thermometer"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_return_input"

    @property
    def native_value(self) -> str | None:
        """Return the state."""
        return self.coordinator.data.get("inputs", {}).get("return", {}).get("state")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        return_input = self.coordinator.data.get("inputs", {}).get("return", {})
        return {
            "message": return_input.get("message"),
            "temperature": return_input.get("temperature"),
        }


class WTHCondensInputSensor(WTHBaseSensor):
    """Sensor for condens input."""

    _attr_name = "Condens Input"
    _attr_icon = "mdi:water"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_condens_input"

    @property
    def native_value(self) -> str | None:
        """Return the state."""
        return self.coordinator.data.get("inputs", {}).get("condens", {}).get("state")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        condens = self.coordinator.data.get("inputs", {}).get("condens", {})
        return {
            "message": condens.get("message"),
            "value": condens.get("value"),
            "temperature": condens.get("temperature"),
        }


class WTHTemperatureSensor(WTHBaseSensor):
    """Sensor for temperature sensors."""

    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: WTHCoordinator, entry: ConfigEntry, index: int) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, entry)
        self._index = index
        self._attr_name = f"Temperature Sensor {index + 1}"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_temp_sensor_{self._index}"

    @property
    def native_value(self) -> float | None:
        """Return the temperature."""
        sensors = self.coordinator.data.get("inputs", {}).get("tSensors", [])
        if self._index < len(sensors):
            temp = sensors[self._index].get("temperature", 0.0)
            return temp if temp > 0 else None
        return None

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        sensors = self.coordinator.data.get("inputs", {}).get("tSensors", [])
        if self._index < len(sensors):
            return {
                "serial_number": sensors[self._index].get("serialNumber"),
            }
        return {}


class WTHFanlinkStatusSensor(WTHBaseSensor):
    """Sensor for Fanlink communication status."""

    _attr_name = "Fanlink Status"
    _attr_icon = "mdi:lan-connect"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_fanlink_status"

    @property
    def native_value(self) -> str | None:
        """Return the status."""
        return self.coordinator.data.get("communications", {}).get("fanlink", {}).get("state")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        fanlink = self.coordinator.data.get("communications", {}).get("fanlink", {})
        return {
            "message": fanlink.get("message"),
        }


class WTHRFStatusSensor(WTHBaseSensor):
    """Sensor for RF communication status."""

    _attr_name = "RF Status"
    _attr_icon = "mdi:wifi"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_rf_status"

    @property
    def native_value(self) -> str | None:
        """Return the status."""
        return self.coordinator.data.get("communications", {}).get("rf", {}).get("state")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        rf = self.coordinator.data.get("communications", {}).get("rf", {})
        return {
            "message": rf.get("message"),
        }


class WTHModbusStatusSensor(WTHBaseSensor):
    """Sensor for Modbus communication status."""

    _attr_name = "Modbus Status"
    _attr_icon = "mdi:serial-port"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_modbus_status"

    @property
    def native_value(self) -> str | None:
        """Return the status."""
        return self.coordinator.data.get("communications", {}).get("modbus", {}).get("state")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        modbus = self.coordinator.data.get("communications", {}).get("modbus", {})
        return {
            "message": modbus.get("message"),
        }


class WTHBluetoothStatusSensor(WTHBaseSensor):
    """Sensor for Bluetooth communication status."""

    _attr_name = "Bluetooth Status"
    _attr_icon = "mdi:bluetooth"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_bluetooth_status"

    @property
    def native_value(self) -> str | None:
        """Return the status."""
        return self.coordinator.data.get("communications", {}).get("bluetooth", {}).get("state")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        bluetooth = self.coordinator.data.get("communications", {}).get("bluetooth", {})
        return {
            "message": bluetooth.get("message"),
        }


class WTHEthernetStatusSensor(WTHBaseSensor):
    """Sensor for Ethernet communication status."""

    _attr_name = "Ethernet Status"
    _attr_icon = "mdi:ethernet"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_ethernet_status"

    @property
    def native_value(self) -> str | None:
        """Return the status."""
        return self.coordinator.data.get("communications", {}).get("ethernet", {}).get("state")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        ethernet = self.coordinator.data.get("communications", {}).get("ethernet", {})
        return {
            "message": ethernet.get("message"),
            "mac_address": ethernet.get("macAddress"),
            "dhcp": ethernet.get("dhcp"),
            "ip_address": ethernet.get("ipAddress"),
            "subnet_mask": ethernet.get("subnetMask"),
            "gateway_address": ethernet.get("gatewayAddress"),
            "dns_address": ethernet.get("dnsAddress"),
        }


class WTHFanlinkDeviceSensor(WTHBaseSensor):
    """Sensor for Fanlink device."""

    _attr_icon = "mdi:devices"

    def __init__(self, coordinator: WTHCoordinator, entry: ConfigEntry, index: int) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, entry)
        self._index = index
        self._attr_name = f"Fanlink Device {index + 1}"

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{self._entry.entry_id}_fanlink_device_{self._index}"

    @property
    def native_value(self) -> str | None:
        """Return the device type."""
        devices = self.coordinator.data.get("communications", {}).get("fanlink", {}).get("devices", [])
        if self._index < len(devices):
            device_type = devices[self._index].get("type", "")
            return device_type if device_type else "Not configured"
        return None

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional attributes."""
        devices = self.coordinator.data.get("communications", {}).get("fanlink", {}).get("devices", [])
        if self._index < len(devices):
            device = devices[self._index]
            return {
                "serial_number": device.get("serialNumber"),
                "last_seen": device.get("lastSeen"),
                "last_learn": device.get("lastLearn"),
            }
        return {}
