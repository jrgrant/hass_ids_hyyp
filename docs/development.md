# IDS Hyyp (hawkMod) Development Notes

## Repository Structure

- `custom_components/ids_hyyp/`
  - `__init__.py`: Integration setup and teardown logic.
  - `alarm_control_panel.py`: Alarm control panel entity implementation.
  - `binary_sensor.py`: Binary sensor entity (deprecated, see switch attributes).
  - `button.py`: Button entities for refresh, stay profiles, automations.
  - `config_flow.py`: Handles Home Assistant config flow UI and logic.
  - `const.py`: Constants and configuration keys.
  - `coordinator.py`: Data update coordinator for polling and state management.
  - `entity.py`: Base entity classes for site/partition/zone.
  - `sensor.py`: Sensor entities for notifications, poll interval, failure cause, status.
  - `switch.py`: Switch entities for zone bypass and attributes.
  - `manifest.json`: Home Assistant integration manifest.
  - `services.yaml`: Service definitions (if any).
  - `strings.json`: UI strings for config flow.
  - `translations/`: Localized UI strings.

## Key Concepts

- **Coordinator Pattern:**
  - Uses a central data update coordinator to manage API polling and state updates for all entities.
- **API Dependency:**
  - Relies on `pyhyypapihawkmod` for all communication with IDS servers.
- **Config Flow:**
  - Supports Home Assistant's config flow for easy setup and options management.
- **Cloud Polling:**
  - All data is fetched from the IDS cloud servers; no local LAN communication.

## Adding Features

- Add new entities by extending the appropriate platform file and registering with the coordinator.
- Use the `const.py` file for new configuration keys or service names.
- Update `manifest.json` for new dependencies or metadata.

## Testing

- Use Home Assistant's built-in developer tools to reload, test, and debug entities.
- Check logs for errors and user-friendly messages.

## Contributing

- Fork the repository and submit pull requests for improvements or bugfixes.
- Follow Home Assistant's best practices for custom integrations.

## References

- [Home Assistant Developer Docs](https://developers.home-assistant.io/)
- [pyhyypapihawkmod API](https://github.com/hawky358/pyHyypApi)
