import os

API_ID = int(os.getenv("API_ID", "22039315"))

API_HASH = os.getenv("API_HASH", "b9d878c0e74f6b2a2e2df3a1d9be968b")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6207982225:AAGVegK7PzqYd20G1qnAzgl2vyqJNbnSv3A")

OWNER_ID = int(os.getenv("OWNER_ID", "1964437366"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1001969856888"))

COMMAND = os.getenv("COMMAND", ". , : ; !")
PREFIX = COMMAND.split()

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001969856888").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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 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",
).split()

SESSION_STRING = os.getenv(
    "SESSION_STRING",
    "BQFQSxMAtFYRw4HCfhL6yO1IwAwVfCr8aNmR1ab0HvnKIPHCKrwgC1rbG8lMl5ozOrduqnnmrzrnSO85q599DeaUeR8bEokr50nJjzMG_BwOKklQZdv3rGLHRJwErwVDUdqd1f3IW4HNl5_IBDMsGlXB42WioQK-E-7EOEsET0tZoo7fAz5o7xLxobDzluUgHOvnQNR7fAOIqUwJ1qSbmTxCNAwZLLv6SGR0abZZbQiXOrRB0mOIQlrLC0QkMTXV7rntrtDZ91Kwxw7E8mILgYhxG_XRNJj_7Y6b8TPOIgdsXoPkhPHQfxlMcOJSrnzfi7HZug2UmoSlzRajwCVkJqxIFR_t_QAAAAB1Fu92AA",
)

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://PremUbot:sST5VL04n85JkcxS@cluster0.wixneuz.mongodb.net/?retryWrites=true&w=majority",
)

TEXT_PAYMENT = os.getenv(
    "TEXT_PAYMENT",
    """
<b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ sᴇʙᴇsᴀʀ ʀᴘ25.000 = 1 ʙᴜʟᴀɴ</b>

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
  <b>┣ ᴅᴀɴᴀ: </b> <code>089525658633</code>
  <b>┣ ɢᴏᴘᴀʏ:</b> </b> <code>089525658633</code>
  <b>┣ ᴏᴠᴏ:</b> </b> <code>089525658633</code>
  <b>┣ sᴘᴀʏ</b> </b> <code>089525658633</code>
  <b>┗ ǫʀɪs:</b> </b> <a href=https://api.qrcode-monkey.com/tmp/2274eaefa4ad07bab3a2578ac5c1e000.png>ᴋʟɪᴋ ᴅɪsɪɴɪ</a>

<b>✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b>
""",
)
