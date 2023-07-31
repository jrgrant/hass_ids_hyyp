"""Provides the ezviz DataUpdateCoordinator."""
from datetime import timedelta
import logging
from typing import Any
import json
import time

from async_timeout import timeout
from pyhyypapihawkmod.client import HyypClient
from pyhyypapihawkmod.exceptions import HTTPError, HyypApiError, InvalidURL

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, FCM_PERSISTENTIDFILE

_LOGGER = logging.getLogger(__name__)


class HyypDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching IDSHyyp data."""

    def __init__(
        self, hass: HomeAssistant, *, api: HyypClient, api_timeout: int
    ) -> None:
        """Initialize global IDS Hyyp data updater."""
        self.hyyp_client = api
        self._api_timeout = api_timeout
        update_interval = timedelta(seconds=30)
        self.push_notification_entity_callback_methods = []
        
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=update_interval)

        pids = self._read_fcm_pids()
        self.hyyp_client.initialize_fcm_notification_listener(callback=self._update_fcm_data, persistent_pids=pids)

    async def _async_update_data(self) -> dict[Any, Any]:
        """Fetch data from IDS Hyyp."""
 

        try:
            async with timeout(self._api_timeout):
                return await self.hass.async_add_executor_job(
                    self.hyyp_client.load_alarm_infos
                )

        except (InvalidURL, HTTPError, HyypApiError) as error:
            raise UpdateFailed(f"Invalid response from API: {error}") from error

    
    def _append_fcm_pids(self, pid):
        pid = str(pid)
        pidfile = open(FCM_PERSISTENTIDFILE, "a" )
        pidfile.write(pid + "\n")
        pidfile.close()
        
    def _read_fcm_pids(self):
        pidfile = open(FCM_PERSISTENTIDFILE, "r")
        raw_info = pidfile.read()
        pids = raw_info.split("\n")
        return pids
    
    def _update_fcm_data(self, data):
        #_LOGGER.warning(data)       
        if "new_persistent_id" in data:
            newid = data["new_persistent_id"]
            self._append_fcm_pids(pid=newid)
        if "notification" not in data:
            return
        if "data" not in data["notification"]:
            return
        if "notification" not in data["notification"]["data"]:
            return
        short_json = data["notification"]["data"]["notification"]
        if type(short_json) == str:
            short_json = json.loads(short_json)
        short_json["timestamp"] = time.time() 
        message = json.dumps(short_json)
        self._update_notification_entity(message) 
    
    def _update_notification_entity(self, data):
        for callback in self.push_notification_entity_callback_methods:
            callback(data=data)
        
    def _regisiter_callback_for_notification_entity(self, callback):
        self.push_notification_entity_callback_methods.append(callback)     