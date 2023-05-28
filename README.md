# hass_ids_hyyp (hawkMod)

Home Assistant integration for IDS Hyyp (Beta)

**Requires Home Assistant version 2023.4 and newer**

*Disclaimer: I am not a programmer/developer/coder/etc. I created this fork since I want to continue using this integration. It was broken for me, so I fixed it (for me) and thought I'd share it so other people can also continue using it.
Support, updates, bugfixes, features, etc. will be limited*

# To Install 
**HACS Method (https://hacs.xyz/docs/setup/download/)**

Steps in 1-4 Youtube video: **http://www.youtube.com/watch?v=FGoE4XzUE38**


0) DELETE THE OLD VERSION! (If you still have the old Pre 2023.4 version by @RenierM26)
1) Add the following custom repository to HACS: https://github.com/hawky358/hass_ids_hyyp
2) Download the integration using HACS 
3) Restart Home Assistant
4) Add Hyyp integration via Settings > Devices and Services and configure via config flow. 


**SSH Method**

0) DELETE THE OLD VERSION from /config/custom_components/
1) Copy the ids_hyyp folder into /config/custom_components/
2) Reboot
3) Add Hyyp integration via Settings > Devices and Services and configure via config flow. (See later part of youtube video)


---
# Changelog:

**Version 1.0.0**

Updated version number only
The integration is working and I want to start fresh with version numbers
API Version number also updated and bumped to 1.0.0



**Version 0.0.1.7**

Updated Readme and allowed for display on HACS

**Version 0.0.1.6** (Main changes from the original @RenierM26 version)

1) This is a fork of @francoistk 's version. 
    - Fixed the requirement that a stay profile is required for every partitions
2) Reverse engineered the pyHyypApi protobuf files and recompiled. This is not a direct change to ids_hyyp, rather it's a change to the API (https://github.com/hawky358/pyHyypApi)
3) Modified dependancies in IDS_HYYP to point to new modified pyhyypapi package
4) Changed name to IDS Hyyp (Beta)(hawkMod) to avoid potential conflicts with previous version
5) Works with 2023.4 and higher.



