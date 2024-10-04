"""Provides the DataUpdateCoordinator."""
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
        self, hass: HomeAssistant, *, api: HyypClient, api_timeout: int, update_time: int = 30
    ) -> None:
        """Initialize global IDS Hyyp data updater."""
        self.hyyp_client = api
        self._api_timeout = api_timeout
        update_interval = timedelta(seconds=update_time)
        self.push_notification_entity_callback_methods = []
        self.poll_interval_callback_method = None
        self._arm_fail_cause_callback_method = None
        
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=update_interval)
        self.hyyp_client.register_generic_callback_to_hass(callback=self._generic_callback_for_data_from_api)
        hass.async_add_executor_job(self._init_FCM_notifications)
        
    async def _async_update_data(self) -> dict[Any, Any]:
        """Fetch data from IDS Hyyp."""
 
        try:
            async with timeout(self._api_timeout):
                return await self.hass.async_add_executor_job(
                    self.hyyp_client.load_alarm_infos
                )

        except (InvalidURL, HTTPError, HyypApiError) as error:
            raise UpdateFailed(f"Invalid response from API: {error}") from error
    
    def _update_fcm_data(self, data):
        if "new_persistent_id" in data:
            newid = data["new_persistent_id"]
            self._append_fcm_pids(pid=newid)          
        if data == "restart_push_receiver":     
            self.hyyp_client.initialize_fcm_notification_listener(callback=self._update_fcm_data, restart=True)
            return         
        if "notification" not in data:
            return
        if "data" not in data["notification"]:
            return
        if "notification" not in data["notification"]["data"]:
            return
        short_json = data["notification"]["data"]["notification"]
        if isinstance(short_json, str):
            short_json = json.loads(short_json)
        short_json["timestamp"] = time.time() 
        message = json.dumps(short_json)
        self._update_push_notification_entity(message) 
    
    def _update_push_notification_entity(self, data):
        for callback in self.push_notification_entity_callback_methods:
            callback(data=data)
        
    def _register_callback_for_push_notification_entity(self, callback):
        self.push_notification_entity_callback_methods.append(callback)     
    
    def _register_poll_inverval_update_callback(self, callback):
        self.poll_interval_callback_method = callback
        
    def _register_arm_fail_cause_callback(self, callback):
        self._arm_fail_cause_callback_method = callback       
        

    def _generic_callback_for_data_from_api(self, data):
        _LOGGER.warning(data)
        if "arm_fail_cause" in data:
            short_json = data["arm_fail_cause"]
            if isinstance(short_json, str):
                short_json = json.loads(short_json)
            short_json["timestamp"] = time.time() 
            message = json.dumps(short_json)          
            self._arm_fail_cause_callback_method(message)
            return
        
        if "fcm_data" in data:
            self._update_fcm_data(data=data["fcm_data"])
        

    def _init_FCM_notifications(self):    
        pids = self._read_fcm_pids()
        # _LOGGER.warning("Here are the PIDS ^^^")
        # _LOGGER.warning(pids)
        self.hyyp_client.initialize_fcm_notification_listener(callback=self._update_fcm_data, persistent_pids=pids)
        
        
    def _read_fcm_pids(self):
        pidfile = open(FCM_PERSISTENTIDFILE, "a" )
        pidfile.close()
        pidfile = open(FCM_PERSISTENTIDFILE, "r")
        raw_info = pidfile.read()
        pids = raw_info.split("\n")
        pidfile.close()
        return pids
    
    def _append_fcm_pids(self, pid):
        pid = str(pid)
        pidfile = open(FCM_PERSISTENTIDFILE, "a" )
        pidfile.write(pid + "\n")
        pidfile.close()
     