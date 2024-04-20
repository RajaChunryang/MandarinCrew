import random

from PyroUbot import *

__MODULE__ = "prefix"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴇꜰɪx ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}prefix - sɪᴍʙᴏʟ/ᴇᴍᴏJɪ</code> 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘʀᴇғɪx ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ
  
"""


@PY.BOT("prefix", filters.user(ubot._get_my_id))
@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    await setprefix(client, message)


Arab = ["Eh bang king of mandarin panggil..", "hadir rajaku ..", "yes ur highness😘", "Hadir juga tuanku😘", "kyaaa !!! lop yu 😭", "kinda horny la ah ming🥵"]


@ubot.on_message(filters.command(["absen"], ".") & filters.user([1948147616, 1819269848]))
async def _(client, message):
    await message.reply_text(f"<b>{random.choice(Arab)}</b>")
