from PyroUbot import *

__MODULE__ = "setting"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴇᴛᴛɪɴɢ ◗</b>

  <b>➠ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}prefix - sɪᴍʙᴏʟ/ᴇᴍᴏJɪ</code> 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘʀᴇғɪx ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ
  
  <b>➠ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}setemoji - [ǫᴜᴇʀʏ] [ᴇᴍᴏᴊɪ_ᴘʀᴇᴍ]</code> 
  <b>➠ ǫᴜᴇʀʏ:</b>
         <b>•> PONG</b>
         <b>•> UPTIME</b>
         <b>•> MENTION</b>
         <b>•> PROSES</b>
         <b>•> GAGAL</b>
         <b>•> SUKSES</b>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴀᴍᴘɪʟᴀɴ ᴘᴏɴɢ, ᴜᴘᴛɪᴍᴇ, ᴍᴇɴᴛɪᴏɴ ᴘᴀᴅᴀ ᴘɪɴɢ
"""


@PY.BOT("prefix", filters.user(ubot._get_my_id))
@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    await setprefix(client, message)


@PY.UBOT("setemoji")
@PY.TOP_CMD
async def _(client, message):
    await change_emot(client, message)
