# hass_ids_hyyp (hawkMod)

Home Assistant integration for IDS Hyyp (Beta)
**Requires Home Assistant version 2023.4 and newer**


# To Install 
**HACS Method**

0) DELETE THE OLD VERSION! 
1) Add custom repository to HACS (https://github.com/hawky358/hass_ids_hyyp)
2) Download integration into HACS (+reboot)
3) Add Hyyp integration via HASS and configure via config flow.

**SSH Method**

0) DELETE THE OLD VERSION from /config/custom_components/
1) Copy the ids_hyyp folder into /config/custom_components/





# Main changes from the original @RenierM26 version:

**Version 0.0.1.8**

####

**Version 0.0.1.7**

Updated Readme and allowed for display on HACS

**Version 0.0.1.6**

1) This is a fork of @francoistk 's version. 
    - Fixed the requirement that a stay profile is required for every partitions
2) Reverse engineered the pyHyypApi protobuf files and recompiled. This is not a direct change to ids_hyyp, rather it's a change to the API
3) Modified dependancies in IDS_HYYP to point to new modified pyhyypapi package
4) Changed name to IDS Hyyp (Beta)(hawkMod) to avoid potential conflicts with previous version
5) Works with 2023.4 and higher.



