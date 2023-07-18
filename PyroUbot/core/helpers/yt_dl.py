from asyncio import get_event_loop
from functools import partial

from yt_dlp import YoutubeDL

from PyroUbot.core.helpers.tools import *


def run_sync(func, *args, **kwargs):
    return get_event_loop().run_in_executor(None, partial(func, *args, **kwargs))


async def YoutubeDownload(url, message, as_video=False):
    if as_video:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    else:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio[ext=m4a]",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    data_ytp = "<b>💡 ɪɴꜰᴏʀᴍᴀsɪ {}</b>\n\n<b>🏷 ɴᴀᴍᴀ:</ʙ> {}<b>\n<b>🧭 ᴅᴜʀᴀsɪ:</b> {}\n<b>👀 ᴅɪʟɪʜᴀᴛ:</b> {}\n<b>📢 ᴄʜᴀɴɴᴇʟ:</b> {}\n<b>🔗 ᴛᴀᴜᴛᴀɴ:</b> <a href={}>ʏᴏᴜᴛᴜʙᴇ</a>\n\n<b>⚡ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> {}"
    ydl = YoutubeDL(ydl_opts)

    async def progress_hook(d):
        if d["status"] == "downloading":
            progress_str = "{0}{1} {2}%\n".format(
                "".join(
                    "•"
                    for _ in range(
                        math.floor(d["downloaded_bytes"] * 10 / d["total_bytes"])
                    )
                ),
                "".join(
                    "~"
                    for _ in range(
                        10 - math.floor(d["downloaded_bytes"] * 10 / d["total_bytes"])
                    )
                ),
                round(d["downloaded_bytes"] * 100 / d["total_bytes"], 2),
            )
            tmp = progress_str + "{0} of {1}\nᴇsᴛɪᴍᴀᴛᴇᴅ ᴛɪᴍᴇ: {2}".format(
                humanbytes(d["downloaded_bytes"]),
                humanbytes(d["total_bytes"]),
                time_formatter(d["eta"]),
            )
            try:
                await message.edit(f"{type_of_ps}\n{tmp}")
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass

    ydl_opts["progress_hooks"] = [progress_hook]
    ytdl_data = await run_sync(ydl.extract_info, url, download=True)

    file_name = ydl.prepare_filename(ytdl_data)
    videoid = ytdl_data["id"]
    title = ytdl_data["title"]
    url = f"https://youtu.be/{videoid}"
    duration = ytdl_data["duration"]
    channel = ytdl_data["uploader"]
    views = f"{ytdl_data['view_count']:,}".replace(",", ".")
    thumb = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
    return file_name, title, url, duration, views, channel, thumb, data_ytp
