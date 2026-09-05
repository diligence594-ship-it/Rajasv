import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "22470912"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "511be78079ed5d4bd4c967bc7b5ee023")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7678862761"))
# ------------------X------------------------------
CREATOR_ID = int(os.environ.get("CREATOR_ID", "7678862761"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1003878357392"))


SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7678862761").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003878357392"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003878357392"))
