import os

API_ID = int(os.getenv("API_ID", "26540741"))
API_HASH = os.getenv("API_HASH", "059766aed4b91e537ed3ab7a51d1d6b2")
BOT_TOKEN = os.getenv("BOT_TOKEN", "6898306197:AAGoOSWsWk0Py1lnoo_UY4iCwLrcP4DrlDc")
OWNER_ID = int(os.getenv("OWNER_ID", "6711696303"))
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002141621783"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001969856888 -1001571197486").split()))
MAX_BOT = int(os.getenv("MAX_BOT", "40"))
RMBG_API = os.getenv("RMBG_API", "b5ZnjZ2nUUpbdEHfcrWdjWbC")
AI_GOOGLE_API = os.getenv("AI_GOOGLE_API", "AIzaSyAM4A7L0Qj3loDZDupt0X74PDne6Tx2YLA")
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://MandarinCrew:mandarinloco@cluster0.muxhxgw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
