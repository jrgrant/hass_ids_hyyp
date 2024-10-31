"""Constants for the ids_hyyp integration."""

DOMAIN = "ids_hyyp"
MANUFACTURER = "IDS"
MODEL = "Hyyp"

# Configuration
CONF_PKG = "pkg"
USER_ID = "userId"
IMEI= "imei"
POLLING_TIME = "polling_time"
FCM_CREDENTIALS = "fcm_credentials"



# Package types
#PKG_IDS_HYYP = "com.hyyp247.home"
PKG_IDS_HYYP = "com.hyyp247.ios"
PKG_ADT_SECURE_HOME = "za.co.adt.securehome.android"

# Pacakage Alias
PGK_IDS_HYYP_ALIAS = "IDS Hyyp"
PKG_ADT_ALIAS = "ADT Securehome"


# Defaults
DEFAULT_TIMEOUT = 25
DEFAULT_POLL_TIME = 30


#GSM Mode
POLLING_TIME_24_HOURS = 24*3600 #1 day in seconds
POLLING_TIME_NEVER_POLL = 24*7*3600 #1 week in seconds


# Data
DATA_COORDINATOR = "coordinator"

# Service names
SERVICE_BYPASS_ZONE = "zone_bypass_code"
SERVICE_TRIGGER_AUTOMATION = "trigger_automation"
SERVICE_STAY_PROFILE_ARM = "stay_profile_arm"

# Attributes
ATTR_BYPASS_CODE = "bypass_code"
ATTR_ARM_CODE = "arm_code"

