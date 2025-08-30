# IDS Hyyp (hawkMod) Entities

This integration creates several Home Assistant entities for each site, partition, and zone configured in your IDS Hyyp account.

## Entity Types

### Alarm Control Panel

- **Entity:** `alarm_control_panel.[site]_[partition]`
- **Description:** Main control for arming/disarming partitions. Supports arm away, arm home (stay), and trigger.

### Binary Sensor

- **Entity:** `binary_sensor.[zone_name]_trigger` (deprecated in favor of switch attribute)
- **Description:** Shows if a zone triggered the alarm (now available as an attribute on the switch entity).

### Button

- **Entities:**
  - `button.[site_name]_refresh_button`: Forces immediate update from IDS servers.
  - `button.[site_name]_[partition_name]_[stay_profile_name]`: Arms a specific stay profile.
  - `button.[site_name]_[automation_name]`: Activates a programmable output (automation/trigger).

### Sensor

- **Entities:**
  - `sensor.[site]_ids_push_notifications`: Latest push notification (JSON format).
  - `sensor.[site]_ids_poll_interval`: Current polling interval in seconds.
  - `sensor.[site_id]_arm_failure_cause`: Reason for arm/disarm/bypass failure (JSON format).
  - `sensor.[site_name]_[partition_name]_status`: Detailed partition status, including custom stay profile names.

### Switch

- **Entity:** `switch.[zone_name]`
- **Description:** Bypass control for each zone. Switches zone on/off (bypass). Attributes include:
  - `violated`: True if zone is violated (e.g., door open)
  - `tampered`: True if zone is tampered
  - `stay_bypassed`: True if bypassed due to stay profile
  - `triggered`: True if zone triggered the alarm

## Example Entity Names

- `alarm_control_panel.home_main`
- `switch.front_door`
- `sensor.home_ids_push_notifications`
- `button.home_refresh_button`
- `sensor.home_arm_failure_cause`

## Notes

- Entity names are based on your site, partition, and zone names as configured in IDS Hyyp.
- Some entities and attributes may only appear if supported by your panel or configuration.
- For detailed notification and failure cause formats, see the [overview](./overview.md).
