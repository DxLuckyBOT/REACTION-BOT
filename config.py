from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "20402718"
# -------------------------------------------------------------
API_HASH = "14de703801bf414bcffadfb59ae21fba"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "6458155947"))
SUPPORT_GRP = "DX_SOPORT"
UPDATE_CHNL = "DxAbouT"
OWNER_USERNAME = "Dx_LUCKY"
    
