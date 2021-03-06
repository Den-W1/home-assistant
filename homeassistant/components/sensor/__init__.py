"""
Component to interface with various sensors that can be monitored.

For more details about this component, please refer to the documentation at
https://home-assistant.io/components/sensor/
"""

from datetime import timedelta
import logging

import voluptuous as vol

from homeassistant.helpers.entity_component import EntityComponent
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA  # noqa

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'sensor'

ENTITY_ID_FORMAT = DOMAIN + '.{}'

SCAN_INTERVAL = timedelta(seconds=30)
DEVICE_CLASSES = [
    'battery',  # % of battery that is left
    'humidity',  # % of humidity in the air
    'temperature',  # temperature (C/F)
]

DEVICE_CLASSES_SCHEMA = vol.All(vol.Lower, vol.In(DEVICE_CLASSES))


async def async_setup(hass, config):
    """Track states and offer events for sensors."""
    component = EntityComponent(
        _LOGGER, DOMAIN, hass, SCAN_INTERVAL)

    await component.async_setup(config)
    return True
