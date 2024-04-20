from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import LOGS_MAKER_UBOT, OWNER_ID, bot, get_expired_date, ubot


class MSG:
    async def STATUS_UB(id):
        user = [x for x in ubot._ubot if x.me.id == int(id)]
        prefix = await ubot.get_prefix(id)
        if user:
            for x in user:
                expired_date = await get_expired_date(x.me.id)
                text = f"""
{bot.me.mention}
    ɴᴀᴍᴀ ᴜsᴇʀ : [{x.me.first_name} {x.me.last_name}](tg://user?id={x.me.id})
    sᴛᴀᴛᴜs ᴜʙᴏᴛ : ✅ ᴀᴄᴛɪᴠᴇᴅ 
    ᴍᴀsᴀ ᴀᴋᴛɪғ ᴜʙᴏᴛ : {expired_date.strftime('%d-%m-%Y')} 
    ᴘʀᴇғɪxᴇs : {' '.join(prefix)}
    sᴛᴀᴛᴜs ᴜsᴇʀ : ᴍᴇᴍʙᴇʀ ᴏғ si ʀᴀᴊᴀ
"""
        else:
            me = await bot.get_users(int(id))
            text = f"""
{bot.me.mention}
    ɴᴀᴍᴀ ᴜsᴇʀ : [{me.first_name} {me.last_name}](tg://user?id={me.id})
    sᴛᴀᴛᴜs ᴜʙᴏᴛ : ❎ ɴᴏᴛ ᴀᴄᴛɪᴠᴀᴛᴇᴅ
    ᴍᴀsᴀ ᴀᴋᴛɪғ ᴜʙᴏᴛ : ʙᴇʟᴜᴍ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ 
    ᴘʀᴇғɪxᴇs : {' '.join(prefix)}
    sᴛᴀᴛᴜs ᴜsᴇʀ : ɴᴏᴛ ᴀ ᴍᴇᴍʙᴇʀ ᴏғ sɪ ʀᴀᴊᴀ           
"""
        return text

    def EXPIRED_MSG_BOT(X):
        return f"""
<b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b>
"""

    def START(message):
        if not message.from_user.id == OWNER_ID:
            msg = f"""
<b>👋🏻 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

💬 ᴘᴇʀᴋᴇɴᴀʟᴋᴀɴ sᴀʏᴀ ᴀᴅᴀʟᴀʜ {bot.me.mention} ʏᴀɴɢ ᴀᴋᴀɴ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴜsᴇʀʙᴏᴛ ᴅɪ ᴀᴋᴜɴ ᴀɴᴅᴀ.

{bot.me.mention} ᴀᴅᴀʟᴀʜ ᴜsᴇʀʙᴏᴛ ᴅᴇɴɢᴀɴ ʙᴇʀʙᴀɢᴀɪ ᴍᴀᴄᴀᴍ ᴍᴏᴅᴜʟ ʏᴀɴɢ ᴋᴇʀᴇɴ ʙᴀɴɢᴇᴛ ɢᴜʏs, ᴘᴍᴘᴇʀᴍɪᴛ, ᴘᴍ-ʟᴏɢs, ᴀғᴋ ᴅᴀɴ ᴊᴜɢᴀ ғᴜʟʟ ᴇᴍᴏᴊɪ ᴘʀᴇᴍɪᴜᴍ.
ᴅɪ ʙᴇʀʙᴀɢᴀɪ ᴍᴏᴅᴜʟɴʏᴀ ᴡɪʜ gempak tak ?

👉🏻 sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪ sɪɴɪ</b>
"""
        else:
            msg = f"""
🧑‍💻 ᴍᴏᴅᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>

✅ ɢᴜɴᴀᴋᴀɴʟᴀʜ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ᴅᴇɴɢᴀɴ ʙɪᴊᴀᴋ
"""
        return msg

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>🎟️ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: 8.00 {harga}
<b>╰ ʜᴀʀɢᴀ ᴘᴇʀ 2 ʙᴜʟᴀɴ {16.000}

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>

touch and go dan online transfer
 <b>├────• ᴜɴᴛᴜᴋ ᴍᴇᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ʟᴀɴɢꜱᴜɴɢ ʜᴜʙ @jngyeol

<b>🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: RM8.00 {total} 
<b>🗓️ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: {bulan}</b> 

<b>✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b>
"""

    def POLICY():
        return """
↪️ ᴋᴇʙɪᴊᴀᴋᴀɴ ᴘᴇɴɢᴇᴍʙᴀʟɪᴀɴ

✅ sᴇᴛᴇʟᴀʜ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ, ᴊɪᴋᴀ ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴍᴇᴍᴘᴇʀᴏʟᴇʜ/
ᴍᴇɴᴇʀɪᴍᴀ ᴍᴀɴꜰᴀᴀᴛ ᴅᴀʀɪ ᴘᴇᴍʙᴇʟɪᴀɴ, 
ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʜᴀᴋ ᴘᴇɴɢɢᴀɴᴛɪᴀɴ ᴅᴀʟᴀᴍ ᴡᴀᴋᴛᴜ 2 ʜᴀʀɪ sᴇᴛᴇʟᴀʜ ᴘᴇᴍʙᴇʟɪᴀɴ. ɴᴀᴍᴜɴ, ᴊɪᴋᴀ 
ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ/ᴍᴇɴᴇʀɪᴍᴀ sᴀʟᴀʜ sᴀᴛᴜ ᴍᴀɴꜰᴀᴀᴛ ᴅᴀʀɪ 
ᴘᴇᴍʙᴇʟɪᴀɴ, ᴛᴇʀᴍᴀsᴜᴋ ᴀᴋsᴇs ᴋᴇ ꜰɪᴛᴜʀ ᴘᴇᴍʙᴜᴀᴛᴀɴ ᴜsᴇʀʙᴏᴛ, ᴍᴀᴋᴀ 
ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʟᴀɢɪ ʙᴇʀʜᴀᴋ ᴀᴛᴀs ᴘᴇɴɢᴇᴍʙᴀʟɪᴀɴ wang .

ꜱᴇʙᴀʀᴀɴɢ ᴘᴇʀᴛᴀɴʏᴀᴀɴ , ʙᴏʟᴇʜ ʜᴜʙ @jngyeol

👉🏻 ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʟᴀɴᴊᴜᴛᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴʏᴀᴛᴀᴋᴀɴ ʙᴀʜᴡᴀ ᴀɴᴅᴀ ᴛᴇʟᴀʜ 
ᴍᴇᴍʙᴀᴄᴀ ᴅᴀɴ ᴍᴇɴᴇʀɪᴍᴀ ᴋᴇᴛᴇɴᴛᴜᴀɴ ɪɴɪ ᴅᴀɴ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ 
ᴘᴇᴍʙᴇʟɪᴀɴ. ᴊɪᴋᴀ ᴛɪᴅᴀᴋ, ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʙᴀᴛᴀʟᴋᴀɴ.
"""

    async def USERBOT(count):
        expired_date = await get_expired_date(ubot._ubot[int(count)].me.id)
        return f"""
<b>❏ ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ├ ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code>
<b> ╰ ᴇxᴘɪʀᴇᴅ</b> <code>{expired_date.strftime('%d-%m-%Y')}</code>
"""


async def sending_user(user_id):
    try:
        await bot.send_message(
            user_id,
            "💬 sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜʟᴀɴɢ ᴜsᴇʀʙᴏᴛ ᴀɴᴅᴀ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🌀 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 🌀",
                            callback_data="bahan",
                        )
                    ],
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        await bot.send_message(
            LOGS_MAKER_UBOT,
            f"""
➡️ ʏᴀɴɢ ᴍᴇʀᴀsᴀ ᴍᴇᴍɪʟɪᴋɪ ɪᴅ: {user_id}

✅ sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜʟᴀɴɢ ᴜsᴇʀʙᴏᴛ ɴʏᴀ ᴅɪ: @{bot.me.username}
    """,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "📁 ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ 📁",
                            callback_data=f"cek_masa_aktif {user_id}",
                        )
                    ],
                ]
            ),
            disable_web_page_preview=True,
        )
