import os
from datetime import timedelta
from time import time

import wget
from youtubesearchpython import VideosSearch

from PyroUbot import *


async def vsong_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ <b>ᴠɪᴅᴇᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ,</b>\nᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴀɴ ᴊᴜᴅᴜʟ ᴠɪᴅᴇᴏ ᴅᴇɴɢᴀɴ ʙᴇɴᴀʀ.",
        )
    infomsg = await message.reply_text("<b>🔍 ᴘᴇɴᴄᴀʀɪᴀɴ...</b>", quote=False)
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()[
            "result"
        ][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"<b>🔍 ᴘᴇɴᴄᴀʀɪᴀɴ...\n\n{error}</b>")
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=True)
    except Exception as error:
        return await infomsg.edit(f"<b>📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...\n\n{error}</b>")
    thumbnail = wget.download(thumb)
    time()
    await client.send_video(
        message.chat.id,
        video=file_name,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption=data_ytp.format(
            "ᴠɪᴅᴇᴏ",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            bot.me.mention,
        ),
        reply_to_message_id=message.id,
        progress=progress,
        progress_args=(
            progress,
            message=infomsg,
            start=time(),
            type_of_ps="📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ᴠɪᴅᴇᴏ",
            file_name=f"{search['id']}.mp4",
        ),
    )
    await infomsg.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)


async def song_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ <b>ᴀᴜᴅɪᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ,</b>\nᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴀɴ ᴊᴜᴅᴜʟ ᴠɪᴅᴇᴏ ᴅᴇɴɢᴀɴ ʙᴇɴᴀʀ.",
        )
    infomsg = await message.reply_text("<b>🔍 ᴘᴇɴᴄᴀʀɪᴀɴ...</b>", quote=False)
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()[
            "result"
        ][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"<b>🔍 ᴘᴇɴᴄᴀʀɪᴀɴ...\n\n{error}</b>")
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=False)
    except Exception as error:
        return await infomsg.edit(f"<b>📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...\n\n{error}</b>")
    thumbnail = wget.download(thumb)
    await client.send_audio(
        message.chat.id,
        audio=file_name,
        thumb=thumbnail,
        file_name=title,
        performer=channel,
        duration=duration,
        caption=data_ytp.format(
            "ᴀᴜᴅɪᴏ",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            bot.me.mention,
        ),
        reply_to_message_id=message.id,
        progress=progress,
        progress_args=(
            message=infomsg,
            start=time(),
            type_of_ps="📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ᴀᴜᴅɪᴏ",
            file_name=f"{search['id']}.mp3",
        ),
    )
    await infomsg.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)
