# IDS Hyyp (hawkMod) Configuration

## Options

- **Polling Interval:**
  - Set how often the integration polls the IDS servers (default: 30 seconds).
  - For GSM modules, can be set to once a day or "Never" (about 1 week).
- **Arm/Bypass Codes:**
  - Optionally store arm and bypass codes for partitions.
- **Package Type:**
  - Select between IDS Hyyp and ADT Securehome package types.
- **FCM Credentials:**
  - Required for push notification support. Managed automatically during config flow.

## Configuration Flow

1. Add the integration via Home Assistant UI (Settings > Devices & Services > Add Integration > IDS Hyyp).
2. Enter your IDS Hyyp credentials and select options as prompted.
3. After setup, you can adjust options (polling interval, codes) via the integration's options menu.

## Advanced

- **Multiple Sites/Partitions:**
  - The integration will automatically discover and create entities for all sites and partitions linked to your account.
- **Stay Profiles:**
  - Button entities are created for each stay profile. Use these to arm specific profiles.
- **Automations/Triggers:**
  - Button entities are created for each programmable output (automation/trigger) configured in the IDS app.

## Updating

- Update via HACS when new versions are released.
- Restart Home Assistant after updating.

## Troubleshooting

- If entities do not appear, check Home Assistant logs for errors.
- For push notification issues, ensure FCM credentials are valid and internet connectivity is available.
- For arm/disarm failures, check the `sensor.[site_id]_arm_failure_cause` entity for details.

## Uninstalling

- Remove the integration from Home Assistant UI.
- Optionally, remove files from `custom_components/ids_hyyp` if no longer needed.
