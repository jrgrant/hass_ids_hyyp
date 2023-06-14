# hass_ids_hyyp (hawkMod)
Home Assistant integration for IDS Hyyp 


**What is "hawkMod"**

- This integration was originally developed by @RenierM26. 
- With Home Assistant version 2023.4 this integration broke and there was no longer any support or updates from the original developer.
- "hawkMod" is the name of this fork. The name was changed to distinguish it from the original and to prevent any confusion with the original version.
- hawkMod also uses a different modified API and has also added several features (See changelog below)

**Requires Home Assistant version 2023.4 and newer**

*Disclaimer: I am not a programmer/developer/coder/etc. I created this fork since I want to continue using this integration. It was broken for me (2023.4), so I fixed it (for me) and thought I'd share it so other people can also continue using it.
Support, updates, bugfixes, features, etc. will be limited, but I will share anything I develop.*

# To Install 
**HACS Method** 

Get HACS here: (https://hacs.xyz/docs/setup/download/)

Steps in 1-4 Youtube video: **http://www.youtube.com/watch?v=FGoE4XzUE38**

0) DELETE THE OLD VERSION! (If you still have the old Pre 2023.4 version by @RenierM26)
1) Add the following custom repository to HACS: https://github.com/hawky358/hass_ids_hyyp
2) Download the integration using HACS 
3) Restart Home Assistant
4) Add Hyyp integration via Settings > Devices and Services and configure via config flow. 

HACS Method is recommended. If you know how to use SSH or another sharing method, you don't need a guide in any event.


---
# Changelog:

**Version 1.3.0-b2**
- Test version, please give feedback on issues
- Merged fixes from 1.2.1 and 1.2.2 branches.

**Version 1.3.0-b1**
- Test version, please give feedback on issues
- Added Binary sensor which shows which zone triggered the alarm.

    The sensor binary_sensor.[zonename]_trigger is normally FALSE.
    If the alarm triggers this binary sensor will turn to TRUE on the zone that has triggered the alarm. 
        (Note multiple sensors can trigger the alarm at the same time if it's armed) 
    The sensor will only remain TRUE for 1 update cycle and then go back to FALSE (You should handle any home assistant triggers with automations)

Note that due to the polling time to the IDS server this currently only updates once every 30 seconds since there is no push from IDS implemented


**Version 1.2.2**
- Remove "Beta" from the name, since it doesn't really mean anything at this point.

**Version 1.2.1**
- Fixed a bug where the "Panel" showed disarmed even though the state attribute for the panel showed a "Stay Armed" name. This is a limitation of the home assistant alarm control panel entity. The control panel state attribute has been reverted and no longer has detailed names.
- The status and name of the armed mode is now contained within a new sensor "sensor.[site]_[parition]_armed_status" and will display the various states e.g.  "Stay Arm 1" or "Stay Arm 2", disarmed etc.


**Version 1.2.0**
- If you have more that one stay-profile, there will now be a button entity (and a service) in home assistant for each of the stay-profiles which allows you to arm each of the "Stay-Profiles" and swap between them
- When armed to a stay profile, the stay profile name will be shown in the "armed" box

**Version 1.1.0**
Added the ability to trigger automations
    If you've set up any automations/triggers in the IDS app it will now be available as a "button" entity (and a service) in home assistant

**Version 1.0.1**

Fixed a bug which wouldn't allow set ups with multiple sites to be added.


**Version 1.0.0**

Updated version number only
The integration is working and I want to start fresh with version numbers
API Version number also updated and bumped to 1.0.0

Changed polling to 30 seconds as test. (Don't want to be too agressive on IDS servers)


**Version 0.0.1.7**

Updated Readme and allowed for display on HACS

**Version 0.0.1.6** (Main changes from the original @RenierM26 version)

1) This is a fork of @francoistk 's version. 
    - Fixed the requirement that a stay profile is required for every partitions
2) Reverse engineered the pyHyypApi protobuf files and recompiled. This is not a direct change to ids_hyyp, rather it's a change to the API (https://github.com/hawky358/pyHyypApi)
3) Modified dependancies in IDS_HYYP to point to new modified pyhyypapi package
4) Changed name to IDS Hyyp (Beta)(hawkMod) to avoid potential conflicts with previous version
5) Works with 2023.4 and higher.



