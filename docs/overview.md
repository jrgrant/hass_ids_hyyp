# IDS Hyyp (hawkMod) Home Assistant Integration

## Overview

This custom integration allows Home Assistant to control IDS alarm panels equipped with the Hyyp module, using the official IDS servers (cloud polling). It is a fork of the original integration, updated for compatibility with newer Home Assistant versions and with additional features.

## Features

- **Push Notifications:** Receives and displays IDS "cell phone" type push notifications as Home Assistant sensors.
- **Polling Modes:** Adjustable polling interval for GSM modules to manage data usage.
- **Entities Created:**
  - Alarm Control Panel (`alarm_control_panel`)
  - Binary Sensors (`binary_sensor`)
  - Buttons (`button`)
  - Sensors (`sensor`)
  - Switches (`switch`)
- **Zone Bypass:** Switch entities for each zone allow bypassing (with attributes for violated, tampered, stay_bypassed, triggered).
- **Multiple Sites/Partitions:** Supports multiple alarm sites and partitions per account.
- **Stay Profiles:** Button entities for each stay profile, and sensors for detailed partition status.
- **Automations/Triggers:** Button entities to activate programmable outputs (e.g., gates, garage doors).
- **Failure Cause Sensor:** Sensor entity shows the reason for arm/disarm/bypass failures.
- **Refresh Button:** Manually trigger an immediate update from IDS servers.

## Requirements

- Home Assistant 2024.11 or newer.
- Internet connection for Home Assistant server.
- HACS for installation.

## Installation

1. Add the custom repository to HACS: `https://github.com/hawky358/hass_ids_hyyp`
2. Install via HACS.
3. Restart Home Assistant.
4. Add and configure the integration via Home Assistant UI.

## Configuration

- Uses config flow for setup.
- Options include polling interval, arm/bypass codes, and package type.
- Stores FCM credentials for push notifications.

## Architecture

- **Domain:** `ids_hyyp`
- **Platforms:** Alarm Control Panel, Binary Sensor, Button, Sensor, Switch
- **Coordinator:** Central update coordinator manages data fetching and state updates.
- **API:** Uses `pyhyypapihawkmod` Python package for communication with IDS servers.

## Main Files

- `__init__.py`: Integration setup, config flow, coordinator initialization.
- `alarm_control_panel.py`: Implements the alarm control panel entity.
- `binary_sensor.py`, `button.py`, `sensor.py`, `switch.py`: Implement respective Home Assistant entities.
- `coordinator.py`: Data update coordinator logic.
- `const.py`: Constants and configuration keys.

## Entity Examples

- `sensor.[site]_ids_push_notifications`: Latest push notification (JSON format).
- `sensor.[site]_ids_poll_interval`: Current polling interval in seconds.
- `button.[site_name]_refresh_button`: Triggers immediate update.
- `switch.[zone_name]`: Zone bypass switch with attributes for state, violation, tamper, etc.
- `sensor.[site_id]_arm_failure_cause`: Shows reason for arm/disarm/bypass failure.

## Logging & Error Handling

- Logs errors and exceptions, especially for failed actions (arm, disarm, bypass).
- Provides user-friendly error messages.

## Changelog

- See `../README.md` for a detailed changelog of features, fixes, and version history.

## Support

- Not affiliated with IDS.
- Support is community-based via GitHub issues/discussions.
