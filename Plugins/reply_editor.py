# -*- coding: utf-8 -*-
# Reply customization commands (developer-only, GLOBAL across all groups).
# Works in groups and in the bot's private chat.
#   تغيير              (reply to a bot message) -> then send the new text
#   استرجاع الرد       (reply to a bot message) -> restore that reply
#   الردود المعدلة     -> list all customized replies
#   استرجاع كل الردود -> restore ALL replies to default
import logging
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.replies import (
    install, get_key_for_message, set_override, clear_override,
    set_label, list_overrides, clear_all_overrides,
)

install()


@Client.on_message(filters.text & (filters.group | filters.private), group=-100)
async def change_reply_handler(c, m):
    try:
        if not m.from_user:
            return
        text = m.text or ""
        uid = m.from_user.id
        state_key = f"chgreply:{m.chat.id}:{uid}{Dev_Zaid}"
        state = await r.get(state_key)
        # capture the new reply text (only a developer can ever be in this state)
        if state:
            if not await devp_pls(uid, m.chat.id):
                return
            if text == "الغاء":
                await r.delete(state_key)
                return await m.reply("تم إلغاء تغيير الرد")
            if len(text) > 3000:
                return await m.reply("النص طويل جداً")
            await set_override(m.chat.id, state, text, glob=True)
            await r.delete(state_key)
            return await m.reply("تم تغيير الرد في كل القروبات ✅")
        if text == "تغيير":
            if not await devp_pls(uid, m.chat.id):
                return
            if not m.reply_to_message:
                return await m.reply("رد على رسالة البوت التي تريد تغييرها ثم اكتب: تغيير")
            key = await get_key_for_message(m.chat.id, m.reply_to_message.id)
            if not key:
                return await m.reply("هذا الرد غير قابل للتغيير بعد")
            label = (m.reply_to_message.text or m.reply_to_message.caption or "")[:120]
            await set_label(key, label)
            await r.set(state_key, key, ex=120)
            return await m.reply("أرسل نص الرد الجديد الآن (أو اكتب: الغاء)")
        if text == "استرجاع الرد":
            if not await devp_pls(uid, m.chat.id):
                return
            if not m.reply_to_message:
                return await m.reply("رد على رسالة البوت المراد استرجاعها ثم اكتب: استرجاع الرد")
            key = await get_key_for_message(m.chat.id, m.reply_to_message.id)
            if not key:
                return await m.reply("هذا الرد غير مخصّص")
            await clear_override(m.chat.id, key, glob=True)
            return await m.reply("تم استرجاع الرد الأصلي في كل القروبات ✅")
        if text in ("الردود المعدلة", "الردود المعدله", "قائمة الردود"):
            if not await devp_pls(uid, m.chat.id):
                return
            items = await list_overrides()
            if not items:
                return await m.reply("لا توجد ردود معدّلة حالياً")
            lines = [f"الردود المعدّلة ({len(items)}):", ""]
            for i, (key, lbl, val) in enumerate(items, 1):
                lbl = (lbl or "-").replace(chr(10), " ")[:35]
                val = (val or "").replace(chr(10), " ")[:35]
                lines.append(f"{i}. {lbl} ⇜ {val}")
            return await m.reply(chr(10).join(lines)[:4000])
        if text in ("استرجاع كل الردود", "تصفير الردود"):
            if not await devp_pls(uid, m.chat.id):
                return
            n = await clear_all_overrides()
            return await m.reply(f"تم استرجاع كل الردود الأصلية ✅ ({n})")
    except Exception as e:
        logging.exception(e)
