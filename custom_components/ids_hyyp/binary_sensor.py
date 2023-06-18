"""Support for Hyyp binary sensors."""
from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DATA_COORDINATOR, DOMAIN
from .coordinator import HyypDataUpdateCoordinator
from .entity import HyypSiteEntity, HyypPartitionEntity

PARALLEL_UPDATES = 1

BINARY_SENSOR_TYPES: dict[str, BinarySensorEntityDescription] = {
    "isMaster": BinarySensorEntityDescription(key="isMaster"),
    "hasPin": BinarySensorEntityDescription(key="hasPin"),
    "isOnline": BinarySensorEntityDescription(key="isOnline"),
}


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up IDS Hyyp binary sensors based on a config entry."""
    coordinator: HyypDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id][
        DATA_COORDINATOR
    ]

    async_add_entities(

        [
            HyypSensor(coordinator, site_id, sensor)
            for site_id in coordinator.data
            for sensor, value in coordinator.data[site_id].items()
            if sensor in BINARY_SENSOR_TYPES
            if value is not None
            
        ]

    )
    
    
    async_add_entities(
        
        [
            
            HyypZoneTriggerSensor(coordinator, site_id, partition_id, zone_id)
            for site_id in coordinator.data
            for partition_id in coordinator.data[site_id]["partitions"]
            for zone_id in coordinator.data[site_id]["partitions"][partition_id]["zones"]
            if 'triggered' in coordinator.data[site_id]["partitions"][partition_id]["zones"][zone_id]
            
        ]
    )


class HyypSensor(HyypSiteEntity, BinarySensorEntity):
    """Representation of a IDS Hyyp sensor."""

    coordinator: HyypDataUpdateCoordinator

    def __init__(
        self,
        coordinator: HyypDataUpdateCoordinator,
        site_id: int,
        binary_sensor: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, site_id)
        self._sensor_name = binary_sensor
        self._attr_name = f"{self.data['name']} {binary_sensor.title()}"
        self._attr_unique_id = f"{self._site_id}_{binary_sensor}"
        self.entity_description = BINARY_SENSOR_TYPES[binary_sensor]

    @property
    def is_on(self) -> bool:
        """Return the state of the binary sensor."""
        return bool(self.data[self._sensor_name])


class HyypZoneTriggerSensor(HyypPartitionEntity, BinarySensorEntity):
    """Representation of a IDS Hyyp sensor."""

    coordinator: HyypDataUpdateCoordinator

    def __init__(
        self,
        coordinator: HyypDataUpdateCoordinator,
        site_id: int,
        partition_id: int,
        zone_id: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, site_id, partition_id)
        self._sensor_name = f"{self.partition_data['zones'][zone_id]['name'].title()} trigger"
        self._zone_id = zone_id
        self._attr_name = f"{self.partition_data['zones'][zone_id]['name'].title()} trigger"
        self._attr_unique_id = f"{self._site_id}_{partition_id}_{zone_id}_trigger"
      
   
    @property
    def is_on(self) -> bool:
        """Return the state of the binary sensor."""
        return bool(self.partition_data["zones"][self._zone_id]["triggered"])