from PyroUbot import *

__MODULE__ = "convert"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴠᴇʀᴛ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}toanime</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ/sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘʜᴏᴛᴏ/sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ ᴍᴇɴᴊᴀᴅɪ ɢᴀᴍʙᴀʀ ᴀɴɪᴍᴇ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}toimg</code> [ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ ᴍᴇɴᴊᴀᴅɪ ᴘʜᴏᴛᴏ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}tosticker</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ꜰᴏᴛᴏ ᴍᴇɴᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}togif</code> [ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>  ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ sᴛɪᴄᴋᴇʀ ᴍᴇɴᴊᴀᴅɪ ɢɪꜰ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}toaudio</code> [ʀᴇᴘʟʏ ᴛᴏ ᴠɪᴅᴇᴏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴠɪᴅᴇᴏ ᴍᴇɴᴊᴀᴅɪ ᴀᴜᴅɪᴏ ᴍᴘ3

  <b>❑ ᴄᴍᴅ:</b> <code>{0}efek</code> [ᴇꜰᴇᴋ_ᴄᴏᴅᴇ - ʀᴇᴘʟʏ ᴛᴏ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ sᴜᴀʀᴀ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}list_efek</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀғᴛᴀʀ ᴇғᴇᴋ
  
  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}colong</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ ᴛɪᴍᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴍᴇᴅɪᴀ ᴛɪᴍᴇʀ ᴅᴀɴ ᴍᴇɴʏɪᴍᴘᴀɴ ᴋᴇ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ
"""


@PY.UBOT("toanime", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await convert_anime(client, message)


@PY.UBOT("toimg", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await convert_photo(client, message)


@PY.UBOT("tosticker", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await convert_sticker(client, message)


@PY.UBOT("togif", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await convert_gif(client, message)


@PY.UBOT("toaudio", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await convert_audio(client, message)


@PY.UBOT("efek", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await convert_efek(client, message)


@PY.UBOT("list_efek", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await list_cmd_efek(client, message)


@PY.UBOT("colong", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await colong_cmn(client, message)
