# hass_ids_hyyp
Home Assistant integration for IDS Hyyp (Beta)

**Requires version 2022.5 and newer**

# To Install:
0) DELETE THE OLD VERSION !!
1) Add custom repository to HACS (https://github.com/hawky358/hass_ids_hyyp)
2) Add Hyyp integration and configure via config flow.

Changes from the original @RenierM26 version:

1) This is a fork of @francoistk 's version. 
    - Fixed the requirement that a stay profile is required for every partitions

2) Reverse engineered the pyHyypApi protobuf files and recompiled. (Created new package on pypi)
3) Modified dependancies to point to new modified pyhyypapi package
4) Changed name to IDS Hyyp (Beta)(hawkMod) to avoid potential conflicts with previous version



