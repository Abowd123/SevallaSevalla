import logging
"""


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}


"""

import random, re, time, pytz, os, gtts, requests
import speech_recognition as sr
from pydub import AudioSegment
from hijri_converter import Hijri, Gregorian
from datetime import datetime
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.replies import t
from helpers.Ranks import *
from helpers.persianData import persianInformation
from .welcome_and_rules import *
from .games import *
from PIL import Image
from asyncio import run as RUN
from Python_ARQ import ARQ
from aiohttp import ClientSession

# from googletrans import Translator as googletranstr
from mutagen.mp3 import MP3 as mutagenMP3
# from main import TelegramBot

ARQ_API_KEY = "OZJRWV-SAURXD-PMBUKF-GMVSNS-ARQ"
ARQ_API_URL = "https://arq.hamker.dev"

# translator = googletranstr()


list_UwU = [
    "كس",
    "كسمك",
    "كسختك",
    "عير",
    "كسخالتك",
    "خرا بالله",
    "عير بالله",
    "كسخواتكم",
    "كحاب",
    "مناويج",
    "مناويج",
    "كحبه",
    "ابن الكحبه",
    "فرخ",
    "فروخ",
    "طيزك",
    "طيزختك",
    "كسمك",
    "يا ابن الخول",
    "المتناك",
    "شرموط",
    "شرموطه",
    "ابن الشرموطه",
    "ابن الخول",
    "ابن العرص",
    "منايك",
    "متناك",
    "ابن المتناكه",
    "زبك",
    "عرص",
    "زبي",
    "خول",
    "لبوه",
    "لباوي",
    "ابن اللبوه",
    "منيوك",
    "كسمكك",
    "متناكه",
    "يا عرص",
    "يا خول",
    "قحبه",
    "القحبه",
    "شراميط",
    "العلق",
    "العلوق",
    "العلقه",
    "كسمك",
    "يا ابن الخول",
    "المتناك",
    "شرموط",
    "شرموطه",
    "ابن الشرموطه",
    "ابن الخول",
    "االمنيوك",
    "كسمككك",
    "الشرموطه",
    "ابن العرث",
    "ابن الحيضانه",
    "زبك",
    "خول",
    "زبي",
    "قاحب",
]

list_Shiaa = [
    "يا علي",
    "يا حسين",
    "ياعلي",
    "ياحسين",
    "علي ولي الله",
    "عليا ولي الله",
    "عائشه زانيه",
    "عائشة زانية",
    "عائشة عاهرة",
    "عائشه عاهره",
    "خرب ربك",
    "خرب الله",
    "يلعن ربك",
    "يلعن الله",
    "يا عمر",
    "ياعمر",
    "يا محمد",
    "يامحمد",
    "زوجات الرسول",
    "عير بالسنة",
    "عير بالسنه",
    "خرب السنه",
    "خرا بالسنه",
    "خرب السنة",
    "خرا بالسنة",
    "والحسين",
    "والعباس",
    "وعلي",
    "والامام علي",
    "ربنا علي",
    "علي الله",
    "الله علي",
    "رب علي",
    "علي رب",
]


def Find(text):
    m = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(m, text)
    return [x[0] for x in url]


"""
         r.get(f'{m.chat.id}:mute:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockJoin:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockChannels:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockEdit:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockEditM:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockVoice:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockVideo:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockNot:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockPhoto:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockStickers:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockAnimations:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockFiles:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockPersian:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockUrls:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockHashtags:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockMessages:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockTags:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockBots:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockSpam:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockInline:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockForward:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockAudios:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockaddContacts:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockSHTM:{Dev_Zaid}')
"""

from pyrogram.errors import UserNotParticipant, FloodWait
import asyncio


@Client.on_message(filters.group, group=-1111111111111)
async def on_zbi(c: Client, m: Message):
    name = await r.get(f"{Dev_Zaid}:BotName") or "ليو"
    text = m.text or ""
    if text.startswith(f"{name} "):
        text = text.replace(f"{name} ", "")
    if await r.get(f"{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}"):
        text = await r.get(f"{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}")
    if await r.get(f"Custom:{Dev_Zaid}&text={text}"):
        text = await r.get(f"Custom:{Dev_Zaid}&text={text}")

    if await r.get(f"inDontCheck:{Dev_Zaid}"):
        return m.continue_propagation()

    if await dev_pls(m.from_user.id, m.chat.id):
        return

    if (
        text.startswith("تفعيل ")
        or text.startswith("تعطيل ")
        or text.startswith("قفل ")
        or text.startswith("فتح ")
        or text == "ايدي"
        or text == "الاوامر"
    ):
        if await r.get(f"forceChannel:{Dev_Zaid}") and (
            not await r.get(f"disableSubscribe:{Dev_Zaid}")
        ):
            username = (await r.get(f"forceChannel:{Dev_Zaid}")).replace("@", "")
            not_member = False
            try:
                member = await c.get_chat_member(username, m.from_user.id)
            except FloodWait:
                return m.continue_propagation()
            except UserNotParticipant:
                await m.reply(
                    t('g_79cbe19089', '- انضم للقناة ( @{0} ) لتستطيع استخدام اوامر البوت', username),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "اضغط هنا", url="https://t.me/" + username
                                )
                            ]
                        ]
                    ),
                )
                await r.set(f"inDontCheck:{Dev_Zaid}", 1, ex=10)
                return m.stop_propagation()
            except Exception as e:
                logging.exception(e)
                return m.continue_propagation()

            if member.status in {
                enums.ChatMemberStatus.LEFT,
                enums.ChatMemberStatus.BANNED,
            } or member.status is None:
                not_member = True
            else:
                not_member = False

            if not_member:
                await m.reply(
                    t('g_79cbe19089', '- انضم للقناة ( @{0} ) لتستطيع استخدام اوامر البوت', username),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "اضغط هنا", url="https://t.me/" + username
                                )
                            ]
                        ]
                    ),
                )
                await r.set(f"inDontCheck:{Dev_Zaid}", 1, ex=10)
                return m.stop_propagation()
            else:
                return m.continue_propagation()


@Client.on_message(filters.group, group=27)
async def guardLocksResponse(c, m):
    k = await r.get(f"{Dev_Zaid}:botkey")
    channel = (
        await r.get(f"{Dev_Zaid}:BotChannel") or "YQYQY6"
    )
    await guardResponseFunction(c, m, k, channel)


@Client.on_edited_message(filters.group, group=27)
async def guardLocksResponse2(c, m):
    k = await r.get(f"{Dev_Zaid}:botkey")
    channel = (
        await r.get(f"{Dev_Zaid}:BotChannel") or "YQYQY6"
    )
    await guardResponseFunction2(c, m, k, channel)


async def guardResponseFunction2(c, m, k, channel):
    if not await r.get(f"{m.chat.id}:enable:{Dev_Zaid}"):
        return
    warner = """
「 {} 」
{} ممنوع {}
☆
"""
    warn = False
    reason = False

    if m.sender_chat:
        id = m.sender_chat.id
        mention = f"[{m.sender_chat.title}](t.me/{channel})"
    if m.from_user:
        id = m.from_user.id
        mention = m.from_user.mention

    if (
        await r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}")
        and m.text
        and not await pre_pls(id, m.chat.id)
    ):
        await m.delete()
        warn = True
        reason = "التعديل"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if (
        await r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
        and m.media
        and not await pre_pls(id, m.chat.id)
    ):
        await m.delete()
        warn = True
        reason = "تعديل الميديا"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )


async def guardResponseFunction(c, m, k, channel):
    if not await r.get(f"{m.chat.id}:enable:{Dev_Zaid}"):
        return
    warner = """
「 {} 」
{} ممنوع {}
☆
"""
    warn = False
    reason = False

    if await r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}") and m.service:
        await m.delete()

    if (
        await r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}")
        and m.from_user
        and m.new_chat_members
    ):
        if await pre_pls(m.from_user.id, m.chat.id):
            return
        for me in m.new_chat_members:
            if not me.id == m.from_user.id:
                warn = True
                mention = m.from_user.mention
                await m.chat.ban_member(me.id)
                reason = "تضيف حد هنا"
                await m.delete()
                if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                    return await m.reply(
                        warner.format(mention, k, reason), disable_web_page_preview=True
                    )

    if m.sender_chat:
        id = m.sender_chat.id
        mention = f"[{m.sender_chat.title}](t.me/{channel})"
    if m.from_user:
        id = m.from_user.id
        mention = m.from_user.mention

    # print(id)

    if m.media:
        rep = m
        if rep.sticker:
            file_id = rep.sticker.file_id
        if rep.animation:
            file_id = rep.animation.file_id
        if rep.photo:
            file_id = rep.photo.file_id
        if rep.video:
            file_id = rep.video.file_id
        if rep.voice:
            file_id = rep.voice.file_id
        if rep.audio:
            file_id = rep.audio.file_id
        if rep.document:
            file_id = rep.document.file_id
        idd = file_id[-6:]
        if await r.get(f"{idd}:NotAllow:{m.chat.id}{Dev_Zaid}"):
            if not await admin_pls(id, m.chat.id):
                return await m.delete()

    if m.text and await r.smembers(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"):
        if not await admin_pls(id, m.chat.id):
            for word in await r.smembers(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"):
                if word in m.text:
                    return await m.delete()

    if await r.get(f"{id}:mute:{m.chat.id}{Dev_Zaid}") or await r.get(f"{id}:mute:{Dev_Zaid}"):
        return False

    if await r.get(f"{m.chat.id}:mute:{Dev_Zaid}") and not await admin_pls(id, m.chat.id):
        await m.delete()
        return False

    if await pre_pls(id, m.chat.id):
        return False

    if await r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}") and m.new_chat_members:
        for mem in m.new_chat_members:
            if mem.is_bot:
                return await m.chat.ban_member(mem.id)

    if await r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}") and m.new_chat_members:
        for mem in m.new_chat_members:
            if not await admin_pls(mem.id, m.chat.id):
                await m.chat.ban_member(mem.id)
                await m.chat.unban_member(mem.id)
                return False

    if await r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}") and m.sender_chat:
        if not m.sender_chat.id == m.chat.id:
            await m.chat.ban_member(m.sender_chat.id)
            return False

    if await r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}"):
        if not await r.get(f"{id}in_spam:{m.chat.id}{Dev_Zaid}"):
            await r.set(f"{id}in_spam:{m.chat.id}{Dev_Zaid}", 1, ex=10)
        else:
            if int(await r.get(f"{id}in_spam:{m.chat.id}{Dev_Zaid}")) == 10:
                if m.from_user:
                    await r.set(f"{id}:mute:{m.chat.id}{Dev_Zaid}", 1)
                    await r.sadd(f"{m.chat.id}:listMUTE:{Dev_Zaid}", id)
                    await r.delete(f"{id}in_spam:{m.chat.id}{Dev_Zaid}")
                    return await m.reply(
                        t('g_52b737bf63', '「 {0} 」 \n{1} كتمتك يالبثر عشان تتعلم تكرر\n☆', mention, k)
                    )

                if m.sender_chat:
                    await m.chat.ban_member(m.sender_chat)
                    return await m.reply(
                        t('g_a1fd828680', '「 {0} 」 {1} حظرتك يالبثر عشان تتعلم تكرر\n☆', mention, k)
                    )
            else:
                get = int(await r.get(f"{id}in_spam:{m.chat.id}{Dev_Zaid}"))
                await r.set(f"{id}in_spam:{m.chat.id}{Dev_Zaid}", get + 1, ex=10)

    if await r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}") and m.via_bot:
        await m.delete()
        warn = True
        reason = "ترسل انلاين"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if await r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}") and m.forward_date:
        await m.delete()
        warn = True
        reason = "ترسل توجيه"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    """
  if await r.get(f'{m.chat.id}:lockForward:{Dev_Zaid}') and m.forward_from_chat:
     await m.delete()
     warn = True
     reason = 'ترسل توجيه'
     if not await r.get(f'{m.chat.id}:disableWarn:{Dev_Zaid}') and not await r.get(f'{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}'):
        await r.set(f'{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}',1,ex=60)
        return await m.reply(warner.format(mention,k,reason),disable_web_page_preview=True)
  """

    if await r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}") and m.audio:
        await m.delete()
        warn = True
        reason = "ترسل صوت"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if await r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}") and m.video:
        await m.delete()
        warn = True
        reason = "ترسل فيديوهات"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if await r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}") and m.photo:
        await m.delete()
        warn = True
        reason = "ترسل صور"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if await r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}") and m.sticker:
        await m.delete()
        warn = True
        reason = "ترسل ملصقات"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if await r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}") and m.animation:
        await m.delete()
        warn = True
        reason = "ترسل متحركات"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if await r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}") and m.document:
        await m.delete()
        warn = True
        reason = "ترسل ملفات"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if await r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}") and m.text:
        if "ه‍" in m.text or "ی" in m.text or "ک" in m.text or "چ" in m.text:
            await m.delete()
            warn = True
            reason = "ترسل فارسي"
            if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                return await m.reply(
                    warner.format(mention, k, reason), disable_web_page_preview=True
                )

    if await r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}") and m.caption:
        if "ه‍" in m.caption or "ی" in m.caption or "ک" in m.caption or "چ" in m.caption:
            await m.delete()
            warn = True
            reason = "ترسل فارسي"
            if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                return await m.reply(
                    warner.format(mention, k, reason), disable_web_page_preview=True
                )

    if (
        await r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
        and m.text
        and len(Find(m.text.html)) > 0
    ):
        await m.delete()
        warn = True
        reason = "ترسل روابط"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if (
        await r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}")
        and m.text
        and len(re.findall(r"#(\w+)", m.text)) > 0
    ):
        await m.delete()
        warn = True
        reason = "ترسل هاشتاق"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if await r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}") and m.text and len(m.text) > 150:
        await m.delete()
        warn = True
        reason = "ترسل كلام كثير"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if await r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}") and m.voice:
        await m.delete()
        warn = True
        reason = "ترسل فويس"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if await r.get(
        f"{m.chat.id}:lockTags:{Dev_Zaid}"
    ) and '"type": "MessageEntityType.MENTION"' in str(m):
        await m.delete()
        warn = True
        reason = "ترسل منشنات"
        if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return await m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if await r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}") and (m.caption or m.text):
        if m.caption:
            txt = m.caption
        if m.text:
            txt = m.text
        for a in list_UwU:
            if txt == a or f" {a} " in txt or a in txt:
                await m.delete()
                warn = True
                reason = "السب هنا"
                if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not await r.get(
                    f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
                ):
                    await r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
                    return await m.reply(
                        warner.format(mention, k, reason), disable_web_page_preview=True
                    )

    """
  if await r.get(f'{m.chat.id}:lockKFR:{Dev_Zaid}') and (m.caption or m.text):
     if m.caption:
         txt = m.caption.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","").replace("ـ","").replace("َ","").replace("ٕ","").replace("ُ","").replace("ِ","").replace("ٰ","").replace("ٖ","").replace("ً","").replace("ّ","").replace("ٌ","").replace("ٍ","").replace("ْ","").replace("ٔ","").replace("'","").replace('"',"")
     if m.text:
         txt = m.text.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","").replace("ـ","").replace("َ","").replace("ٕ","").replace("ُ","").replace("ِ","").replace("ٰ","").replace("ٖ","").replace("ً","").replace("ّ","").replace("ٌ","").replace("ٍ","").replace("ْ","").replace("ٔ","").replace("'","").replace('"',"")
     for kfr in list_Shiaa:
         if kfr in txt:
            await m.delete()
            warn = True
            reason = 'الكفر هنا'
            if not await r.get(f'{m.chat.id}:disableWarn:{Dev_Zaid}') and not await r.get(f'{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}'):
                 await r.set(f'{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}',1,ex=60)
                 return await m.reply(warner.format(mention,k,reason),disable_web_page_preview=True)
  """

    if await r.get(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}") and m.new_chat_members:
        if m.from_user.first_name:
            if (
                m.from_user.first_name in persianInformation["names"]
                or m.from_user.id in persianInformation["ids"]
                or "ه‍" in m.from_user.first_name
                or "ی" in m.from_user.first_name
                or "ک" in m.from_user.first_name
                or "چ" in m.from_user.first_name
                or "👙" in m.from_user.first_name
            ) and not await pre_pls(m.from_user.id, m.chat.id):
                if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                    await m.reply(
                        """
「 {} 」
{} تم حظره لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k)
                    )
                return await c.ban_chat_member(m.chat.id, m.from_user.id)

        if m.from_user.last_name:
            if (
                m.from_user.last_name in persianInformation["last_names"]
                or m.from_user.id in persianInformation["ids"]
                or "ه‍" in m.from_user.last_name
                or "ی" in m.from_user.last_name
                or "ک" in m.from_user.last_name
                or "چ" in m.from_user.last_name
                or "👙" in m.from_user.last_name
            ) and not await pre_pls(m.from_user.id, m.chat.id):
                if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                    await m.reply(
                        """
「 {} 」
{} تم حظره لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k)
                    )
                return await c.ban_chat_member(m.chat.id, m.from_user.id)

    if await r.get(f"{m.chat.id}:enableVerify:{Dev_Zaid}") and m.new_chat_members:
        for me in m.new_chat_members:
            if not await pre_pls(me.id, m.chat.id):
                await c.restrict_chat_member(
                    m.chat.id, me.id, ChatPermissions(can_send_messages=False)
                )
                get_random = get_for_verify(me)
                question = get_random["question"]
                reply_markup = get_random["key"]
                return await m.reply(
                    t('g_0678e11d8c', '{0} قيدناك عشان نتاكد انك شخص حقيقي مو زومبي\n\n{1}', k, question),
                    reply_markup=reply_markup,
                )

    if m.media and await r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}"):
        logging.debug("nsfw scanner")
        if not await admin_pls(id, m.chat.id):
            if m.sticker:
                id = m.sticker.thumbs[0].file_id
            if m.photo:
                id = m.photo.file_id
            if m.video:
                id = m.video.thumbs[0].file_id
            if m.animation:
                id = m.animation.thumbs[0].file_id
        file = await c.download_media(id)
        await scanR(c, m, id, file)


async def scanR(c, m, id, file):
    RUN(await scan4(c, m, id, file))


async def scan4(c, m, id, file):
    session = ClientSession()
    arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)
    resp = await arq.nsfw_scan(file=file)
    if resp.result.is_nsfw:
        logging.debug("xNSFW")
        await m.delete()
        k = await r.get(f"{Dev_Zaid}:botkey")
        await m.reply(
            t('g_3c7dd1a22f', '「 {0} 」\n{1} تم حذف رسالتك لإحتوائها على محتوى إباحي .\n☆', m.from_user.mention, k)
        )
    os.remove(file)
    await session.close()


def get_for_verify(me):
    for_verify = [
        {
            "question": "ماهو الحيوان الذي ينتهي اسمه بحرف الباء ؟",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("فأر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("وشق", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("بشار الأسد", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("حمار", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("كلب", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("قطة", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "ماهي عاصمة فرنسا؟",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("دمشق", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الرياض", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("باريس", callback_data=f"yes:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("الكويت", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("القاهرة", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ماشا والدب", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "نادي يبدأ بحرف الباء :",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("برشلونا", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("الهلال", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("النصر", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("الزمالك", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ريال مدريد", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("مانشستر", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "دولة يبدأ اسمها بحرف التاء :",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("قطر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("امريكا", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("سوريا", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("مصر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الصين", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("تركيا", callback_data=f"yes:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اختر هذا الايموجي - 🤑 -",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🍭", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🤑", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("🏆", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("🌀", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🪨", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("💎", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اختر هذا الايموجي - 🔓 -",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🏆", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("💎", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🙄", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("💸", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("💣", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🔓", callback_data=f"yes:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اختر هذا الايموجي - 🌠 -",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("☄️", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🙈", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🦄", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("🌠", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("🌈", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🧑‍💻", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "ماهي عاصمة سوريا",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("دمشق", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("دير الزور", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ادلب", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("ليو ميسي", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الرياض", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("مزة فيلات", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "ماهي عملة الولايات المتحدة الأمريكية",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("الروبية", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الجنيه", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الليرة", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("الدولار", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("الدينار", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الين", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اسم مذكر يبدأ بحرف ز",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("زيد", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("علي", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("محمد", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("عمر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("المريخ", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("احمد", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اسم مؤنث ينتهي بحرف ي",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("لورين", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ماجدة", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("علياء", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("أماني", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("فرح", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("أمل", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اسم مؤنث يبدأ بحرف أ",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("لورين", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ماجدة", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("علياء", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("أمل", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("فرح", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("يمنى", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "الأسبوع كم يوم؟",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("1", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("2", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("3", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("4", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("5", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("6", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("7", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("8", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("9", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
    ]
    return random.choice(for_verify)


@Client.on_chat_join_request(filters.group, group=100)
async def antiPersian(c, m):
    if await r.get(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}"):
        k = await r.get(f"{Dev_Zaid}:botkey")
        if not await pre_pls(m.from_user.id, m.chat.id):
            if m.from_user.first_name:
                if (
                    m.from_user.first_name in persianInformation["names"]
                    or m.from_user.id in persianInformation["ids"]
                    or "ه‍" in m.from_user.first_name
                    or "ی" in m.from_user.first_name
                    or "ک" in m.from_user.first_name
                    or "چ" in m.from_user.first_name
                    or "👙" in m.from_user.first_name
                ):
                    c.decline_chat_join_request(m.chat.id, m.from_user.id)
                    if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                        await c.send_message(
                            m.chat.id,
                            """
「 {} 」
{} تم رفض طلب انضمامه لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k),
                        )
                    return True
            if m.from_user.last_name:
                if (
                    m.from_user.last_name in persianInformation["last_names"]
                    or m.from_user.id in persianInformation["ids"]
                    or "ه‍" in m.from_user.last_name
                    or "ی" in m.from_user.last_name
                    or "ک" in m.from_user.last_name
                    or "چ" in m.from_user.last_name
                    or "👙" in m.from_user.last_name
                ):
                    c.decline_chat_join_request(m.chat.id, m.from_user.id)
                    if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                        await c.send_message(
                            m.chat.id,
                            """
「 {} 」
{} تم رفض طلب انضمامه لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k),
                        )
                    return True


@Client.on_message(filters.group & filters.text, group=28)
async def guardCommandsHandler(c, m):
    k = await r.get(f"{Dev_Zaid}:botkey")
    channel = (
        await r.get(f"{Dev_Zaid}:BotChannel") or "YQYQY6"
    )
    await guardCommands(c, m, k, channel)


async def guardCommands(c, m, k, channel):
    if not await r.get(f"{m.chat.id}:enable:{Dev_Zaid}"):
        return False
    if await r.get(f"{m.chat.id}:mute:{Dev_Zaid}") and not await admin_pls(
        m.from_user.id, m.chat.id
    ):
        return False
    if await r.get(f"{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}"):
        return False
    if await r.get(f"{m.from_user.id}:mute:{Dev_Zaid}"):
        return False
    if await r.get(f"{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}"):
        return False
    if await r.get(f"{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}"):
        return False
    if await r.get(f"{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}") or await r.get(
        f"{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}"
    ):
        return False
    text = m.text
    name = await r.get(f"{Dev_Zaid}:BotName") or "ليو"
    if text.startswith(f"{name} "):
        text = text.replace(f"{name} ", "")
    if await r.get(f"{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}"):
        text = await r.get(f"{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}")
    if await r.get(f"Custom:{Dev_Zaid}&text={text}"):
        text = await r.get(f"Custom:{Dev_Zaid}&text={text}")
    if await isLockCommand(m.from_user.id, m.chat.id, text):
        return
    Open = """
{} من 「 {} 」
{} ابشر فتحت {}
☆
"""
    Openn = """
{} من 「 {} 」
{} {} مفتوح من قبل
☆
"""
    Openn2 = """
{} من 「 {} 」
{} {} مفتوحه من قبل
☆
"""

    lock = """
{} من 「 {} 」
{} ابشر قفلت {}
☆
"""

    lockn = """
{} من 「 {} 」
{} {} مقفل من قبل
☆
"""
    locknn = """
{} من 「 {} 」
{} {} مقفله من قبل
☆
"""

    if text == "الاعدادات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            x1 = "مقفول" if await r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}") else "مفتوح"
            x2 = "مقفول" if await r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}") else "مفتوح"
            x3 = "مقفول" if await r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}") else "مفتوح"
            x4 = "مقفول" if await r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}") else "مفتوح"
            x5 = "مقفول" if await r.get(f"{m.chat.id}:mute:{Dev_Zaid}") else "مفتوح"
            x6 = "مقفول" if await r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}") else "مفتوح"
            x7 = "مقفول" if await r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}") else "مفتوح"
            x8 = "مقفول" if await r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}") else "مفتوح"
            x9 = "مقفول" if await r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}") else "مفتوح"
            x10 = "مقفول" if await r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}") else "مفتوح"
            x11 = "مقفول" if await r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}") else "مفتوح"
            x12 = (
                "مقفول" if await r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}") else "مفتوح"
            )
            x13 = "مقفول" if await r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}") else "مفتوح"
            x14 = "مقفول" if await r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}") else "مفتوح"
            x15 = "مقفول" if await r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}") else "مفتوح"
            x16 = "مقفول" if await r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}") else "مفتوح"
            x17 = (
                "مقفول" if await r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}") else "مفتوح"
            )
            x18 = "مقفول" if await r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}") else "مفتوح"
            x19 = "مقفول" if await r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}") else "مفتوح"
            x20 = "مقفول" if await r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}") else "مفتوح"
            x21 = "مقفول" if await r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}") else "مفتوح"
            x22 = "مقفول" if await r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}") else "مفتوح"
            x23 = "مقفول" if await r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}") else "مفتوح"
            x24 = "مقفول" if await r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}") else "مفتوح"
            x25 = (
                "مقفول" if await r.get(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}") else "مفتوح"
            )
            x26 = "مقفول" if await r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}") else "مفتوح"
            return await m.reply(t('g_4c171fa319', '\nاعدادات المجموعة :\n\n{0} الملفات الصوتية ⇠ ( {1} )\n{2} الفيديو ⇠ ( {3} )\n{4} الفويس ⇠ ( {5} )\n{6} الصور ⇠ ( {7} )\n\n{8} الدردشة ⇠ ( {9} )\n{10} الانلاين ⇠ ( {11} )\n{12} التوجيه ⇠ ( {13} )\n{14} الهشتاق ⇠ ( {15} )\n{16} التعديل ⇠ ( {17} )\n{18} الستيكرات ⇠ ( {19} )\n\n{20} الملفات ⇠ ( {21} )\n{22} المتحركات ⇠ ( {23} )\n{24} الروابط ⇠ ( {25} )\n{26} البوتات ⇠ ( {27} )\n{28} اليوزرات ⇠ ( {29} )\n\n{30} الاشعارات ⇠ ( {31} )\n{32} الاضافة ⇠ ( {33} )\n\n{34} الكلام الكثير ⇠ ( {35} )\n{36} السب ⇠ ( {37} )\n{38} التكرار ⇠ ( {39} )\n{40} القنوات ⇠ ( {41} )\n{42} تعديل الميديا ⇠ ( {43} )\n\n{44} الدخول ⇠ ( {45} )\n{46} الفارسية ⇠ ( {47} )\n{48} دخول الإيراني ⇠ ( {49} )\n{50} الإباحي ⇠ ( {51} )\n\n~ @{52}', k, x1, k, x2, k, x3, k, x4, k, x5, k, x6, k, x7, k, x8, k, x9, k, x10, k, x11, k, x12, k, x13, k, x14, k, x15, k, x16, k, x17, k, x18, k, x19, k, x20, k, x21, k, x22, k, x23, k, x24, k, x25, k, x26, channel))

    if text == "الساعه" or text == "الساعة" or text == "الوقت":
        TIME_ZONE = "Asia/Riyadh"
        ZONE = pytz.timezone(TIME_ZONE)
        TIME = datetime.now(ZONE)
        clock = TIME.strftime("%I:%M %p")
        return await m.reply(t('g_46387c3a3d', '{0} الساعة ( {1} )', k, clock))

    if text == "القوانين":
        if await r.get(f"{m.chat.id}:CustomRules:{Dev_Zaid}"):
            rules = await r.get(f"{m.chat.id}:CustomRules:{Dev_Zaid}")
        else:
            rules = f"""{k} ممنوع نشر الروابط
{k} ممنوع التكلم او نشر صور اباحيه
{k} ممنوع اعاده توجيه
{k} ممنوع العنصرية بكل انواعها
{k} الرجاء احترام المدراء والادمنيه"""
        return await m.reply(rules, disable_web_page_preview=True)

    if text == "التاريخ":
        b = Hijri.today().isoformat()
        a = b.split("-")
        year = int(a[0])
        month = int(a[1])
        day = int(a[2])
        hijri = Hijri(year, month, day)
        hijri_date = str(b).replace("-", "/")
        hijri_month = hijri.month_name("ar")

        b = Gregorian.today().isoformat()
        a = b.split("-")
        year = int(a[0])
        month = int(a[1])
        day = int(a[2])
        geo = Gregorian(year, month, day)
        geo_date = str(b).replace("-", "/")
        geo_month = geo.month_name("en")[:3]

        return await m.reply(t('g_3f3c1a69bb', '\nالتاريخ:\n{0} هجري ↢ {1} {2}\n{3} ميلادي ↢ {4} {5}\n', k, hijri_date, hijri_month, k, geo_date, geo_month))

    if text == "المالك":
        owner = None
        for mm in await m.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
            if mm.status == ChatMemberStatus.OWNER:
                owner = mm.user
                break
        if owner:
            if owner.is_deleted:
                await m.reply(t('g_60752ff85b', "حساب المالك محذوف"))
            else:
                owner_username = owner.username if owner.username else owner.id
                caption = f"• Owner ☆ ↦ {owner.mention}\n\n"
                caption += f"• Owner User ↦ @{owner_username}"
                if owner.photo:
                    file_id = owner.photo.big_file_id
                    photo_path = await c.download_media(file_id)
                    button = InlineKeyboardMarkup(
                        [[InlineKeyboardButton(owner.first_name, user_id=owner.id)]]
                    )
                    await m.reply_photo(
                        photo=photo_path, caption=caption, reply_markup=button
                    )
                    os.remove(photo_path)
                else:
                    button = InlineKeyboardMarkup(
                        [[InlineKeyboardButton(owner.first_name, user_id=owner.id)]]
                    )
                    await m.reply(caption, reply_markup=button)

    if text == "اطردني":
        if await r.get(f"{m.chat.id}:enableKickMe:{Dev_Zaid}"):
            get = await m.chat.get_member(m.from_user.id)
            if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                return await m.reply(t('g_518d2f975f', '{0} ممنوع طرد الحلوين', k))
            if await admin_pls(m.from_user.id, m.chat.id):
                return await m.reply(t('g_518d2f975f', '{0} ممنوع طرد الحلوين', k))
            else:
                await m.reply(
                    t('g_b7b42e0988', 'طردتك يانفسية , وارسلت لك الرابط خاص تقدر ترجع متى مابغيت يامعقد')
                )
                await m.chat.ban_member(m.from_user.id)
                await asyncio.sleep(0.5)
                await c.unban_chat_member(m.chat.id, m.from_user.id)
                link = await c.get_chat(m.chat.id).invite_link
                try:
                    await c.send_message(
                        m.from_user.id,
                        f"{k} حبيبي النفسية رابط القروب الي طردتك منه: {link}",
                    )
                except Exception:
                    pass
                return False

    if text == "الرابط":
        if not await r.get(f"{m.chat.id}:disableLINK:{Dev_Zaid}"):
            link = await c.get_chat(m.chat.id).invite_link
            return await m.reply(t('g_017ed9abd2', '[{0}]({1})', m.chat.title, link), disable_web_page_preview=True)

    if text == "انشاء رابط":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        link = await c.get_chat(m.chat.id).invite_link
        c.revoke_chat_invite_link(m.chat.id, link)
        return await m.reply(t('g_3c0a8d98d5', '{0} ابشر سويت رابط جديد ارسل "الرابط"', k))

    if text.startswith("@all"):
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        if await r.get(f"{m.chat.id}:disableALL:{Dev_Zaid}"):
            return await m.reply(t('g_8334496617', "المنشن معطل"))
        if await r.get(f"{m.chat.id}:inMention:{Dev_Zaid}"):
            return False
        if await r.get(f"{m.chat.id}:inMentionWAIT:{Dev_Zaid}"):
            get = await r.ttl(f"{m.chat.id}:inMentionWAIT:{Dev_Zaid}")
            tm = time.strftime("%M:%S", time.gmtime(get))
            return await m.reply(t('g_0fb534de9b', '{0} سويت منشن من شوي تعال بعد {1}', k, tm))
        else:
            if len(text.split()) > 1:
                reason = text.split(None, 1)[1]
            else:
                reason = ""
            users_list = []
            await r.set(f"{m.chat.id}:inMention:{Dev_Zaid}", 1)
            await m.reply(t('g_aa29383fd6', '{0} بسوي منشن يحلو ، اذا تبي توقفه ارسل `/Cancel` او `ايقاف`', k))
            for mm in await m.chat.get_members(limit=150):
                if mm.user and not mm.user.is_deleted and not mm.user.is_bot:
                    users_list.append(mm.user.mention)
            final_list = [users_list[x : x + 5] for x in range(0, len(users_list), 5)]
            ftext = f"{reason}\n\n"
            for a in final_list:
                for i in a:
                    if not await r.get(f"{m.chat.id}:inMention:{Dev_Zaid}"):
                        return False
                    ftext += f"{i} , "
                await c.send_message(m.chat.id, ftext)
                ftext = f"{reason}\n\n"
            await r.delete(f"{m.chat.id}:inMention:{Dev_Zaid}")
            await r.set(f"{m.chat.id}:inMentionWAIT:{Dev_Zaid}", 1, ex=1200)

    if text.lower() == "/cancel" or text == "ايقاف":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:inMention:{Dev_Zaid}"):
                return await m.reply(t('g_1a4de28401', '{0} مو قاعده اسوي منشن ركز', k))
            else:
                await r.delete(f"{m.chat.id}:inMention:{Dev_Zaid}")
                return await m.reply(t('g_dba46b0a1f', "ابشر وقفت المنشن"))

    if text == "منشن":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        return await m.reply(t('g_92c441101b', "استخدم امر\n@all مع الكلام"))

    if text == "تعطيل المنشن":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableALL:{Dev_Zaid}"):
                return await m.reply(
                    t('g_2c255be749', '{0} من「 {1} 」\n{2} المشن معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableALL:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_2bcae869fc', '{0} من「 {1} 」\n{2} ابشر عطلت المنشن\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل المنشن":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableALL:{Dev_Zaid}"):
                return await m.reply(
                    t('g_e9f65723b6', '{0} من「 {1} 」\n{2} المنشن مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableALL:{Dev_Zaid}")
                return await m.reply(
                    t('g_a64658162f', '{0} من「 {1} 」\n{2} ابشر فعلت المنشن\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل الترحيب":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableWelcome:{Dev_Zaid}"):
                return await m.reply(
                    t('g_f8476e1933', '{0} من「 {1} 」\n{2} الترحيب معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableWelcome:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_1827b21d01', '{0} من「 {1} 」\n{2} ابشر عطلت الترحيب\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل الترحيب بالصورة" or text == "تعطيل الترحيب بالصوره":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableWelcomep:{Dev_Zaid}"):
                return await m.reply(
                    t('g_73d2889c6b', '{0} من「 {1} 」\n{2} الترحيب بالصورة من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableWelcomep:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_9238df400d', '{0} من「 {1} 」\n{2} ابشر عطلت الترحيب بالصورة\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل الترحيب بالصورة" or text == "تفعيل الترحيب بالصوره":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableWelcomep:{Dev_Zaid}"):
                return await m.reply(
                    t('g_2a5b2aae45', '{0} من「 {1} 」\n{2} الترحيب بالصورة مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableWelcomep:{Dev_Zaid}")
                return await m.reply(
                    t('g_958fbbf5a4', '{0} من「 {1} 」\n{2} ابشر فعلت الترحيب بالصورة\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل الرابط":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableLINK:{Dev_Zaid}"):
                return await m.reply(
                    t('g_0ad0379db4', '{0} من「 {1} 」\n{2} الرابط معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableLINK:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_405b0f3db5', '{0} من「 {1} 」\n{2} ابشر عطلت الرابط\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل الرابط":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableLINK:{Dev_Zaid}"):
                return await m.reply(
                    t('g_e0fd374164', '{0} من「 {1} 」\n{2} الرابط مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableLINK:{Dev_Zaid}")
                return await m.reply(
                    t('g_c4d93c7e93', '{0} من「 {1} 」\n{2} ابشر فعلت الرابط\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل البايو":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableBio:{Dev_Zaid}"):
                return await m.reply(
                    t('g_9b444471b5', '{0} من「 {1} 」\n{2} البايو معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableBio:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_4a43a06869', '{0} من「 {1} 」\n{2} ابشر عطلت البايو\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل البايو":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableBio:{Dev_Zaid}"):
                return await m.reply(
                    t('g_114a36b3e8', '{0} من「 {1} 」\n{2} البايو مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableBio:{Dev_Zaid}")
                return await m.reply(
                    t('g_4fef6c691b', '{0} من「 {1} 」\n{2} ابشر فعلت البايو\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل اطردني":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:enableKickMe:{Dev_Zaid}"):
                return await m.reply(
                    t('g_bdda381c5e', '{0} من「 {1} 」\n{2} اطردني معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:enableKickMe:{Dev_Zaid}")
                return await m.reply(
                    t('g_247bfa5b89', '{0} من「 {1} 」\n{2} ابشر عطلت اطردني\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل اطردني":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:enableKickMe:{Dev_Zaid}"):
                return await m.reply(
                    t('g_ac963dc278', '{0} من「 {1} 」\n{2} اطردني مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:enableKickMe:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_01236c61e1', '{0} من「 {1} 」\n{2} ابشر فعلت اطردني\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل التحقق":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:enableVerify:{Dev_Zaid}"):
                return await m.reply(
                    t('g_1f5f64534b', '{0} من「 {1} 」\n{2} التحقق معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:enableVerify:{Dev_Zaid}")
                return await m.reply(
                    t('g_8d597e4807', '{0} من「 {1} 」\n{2} ابشر عطلت التحقق\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل التحقق":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:enableVerify:{Dev_Zaid}"):
                return await m.reply(
                    t('g_3581fa0672', '{0} من「 {1} 」\n{2} التحقق مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:enableVerify:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_bce8805d16', '{0} من「 {1} 」\n{2} ابشر فعلت التحقق\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل انطقي" or text == "تعطيل انطق":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableSay:{Dev_Zaid}"):
                return await m.reply(
                    t('g_a0f50c20d6', '{0} من「 {1} 」\n{2} انطقي معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableSay:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_e686ab7455', '{0} من「 {1} 」\n{2} ابشر عطلت انطقي\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل انطقي" or text == "تفعيل انطق":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableSay:{Dev_Zaid}"):
                return await m.reply(
                    t('g_0ddd634197', '{0} من「 {1} 」\n{2} انطقي مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableSay:{Dev_Zaid}")
                return await m.reply(
                    t('g_b71b952128', '{0} من「 {1} 」\n{2} ابشر فعلت انطقي\n☆', k, m.from_user.mention, k)
                )

    if text.startswith("انطق "):
        if not await r.get(f"{m.chat.id}:disableSay:{Dev_Zaid}"):
            txt = text.split(None, 1)[1]
            if len(txt) > 500:
                return await m.reply(t('g_26da79f2c4', "توكل مايمدي انطق اكثر من ٥٠٠ حرف بتعب بعدين"))
            """
         det = translator.detect(txt).lang.lower()
         if det == 'fa' or det == 'ar':
           lang = 'ar'
         else:
           lang = det
         """
            id = random.randint(999, 10000)
            """
         o = gtts.gTTS(text=txt, lang="ar", slow=False)
         o.save(f'zaid{id}.mp3')
         """
            with open(f"zaid{id}.mp3", "wb") as f:
                try:
                    await c.send_chat_action(m.chat.id, ChatAction.RECORD_AUDIO)
                except Exception:
                    pass
                f.write(
                    (await asyncio.to_thread(requests.get,
                        f"https://eduardo-tate.com/AI/voice.php?text={txt}&model=3"
                    )).content
                )
            """
         audio = MP3(f'zaid{id}.mp3')
         duration=int(audio.info.length)
         os.rename(f'zaid{id}.mp3',f'zaid{id}.ogg')
         await TelegramBot.send_voice(
         m.chat.id,
         voice,
         caption=f'الكلمة: {txt}',
         duration=duration
         )
         """
            try:
                await c.send_chat_action(m.chat.id, ChatAction.RECORD_AUDIO)
            except Exception:
                pass
            os.system(
                f"ffmpeg -i zaid{id}.mp3 -ac 1 -strict -2 -codec:a libopus -b:a 128k -vbr off -ar 24000 zaid{id}.ogg"
            )
            try:
                await c.send_chat_action(m.chat.id, ChatAction.UPLOAD_AUDIO)
            except Exception:
                pass
            await m.reply_voice(f"zaid{id}.ogg", caption=f"الكلمة: {txt}")
            """
         voice = open(f'zaid{id}.ogg','rb')
         url = f"https://api.telegram.org/bot{c.bot_token}/sendVoice"
         response=requests.post(url, data={'chat_id': m.chat.id,'caption':f'الكلمة: {txt}','reply_to_message_id':m.id}, files={'voice': voice})
         os.remove(f'zaid{id}.ogg')
         """
            os.remove(f"zaid{id}.ogg")
            os.remove(f"zaid{id}.mp3")
            return True

    if text.startswith("انطقي "):
        if not await r.get(f"{m.chat.id}:disableSay:{Dev_Zaid}"):
            txt = text.split(None, 1)[1]
            if len(txt) > 500:
                return await m.reply(t('g_26da79f2c4', "توكل مايمدي انطق اكثر من ٥٠٠ حرف بتعب بعدين"))
            """
         det = translator.detect(txt).lang.lower()
         if det == 'fa' or det == 'ar':
           lang = 'ar'
         else:
           lang = det
         """
            id = random.randint(999, 10000)
            """
         o = gtts.gTTS(text=txt, lang="ar", slow=False)
         o.save(f'zaid{id}.mp3')
         """
            with open(f"zaid{id}.mp3", "wb") as f:
                try:
                    await c.send_chat_action(m.chat.id, ChatAction.RECORD_AUDIO)
                except Exception:
                    pass
                f.write(
                    (await asyncio.to_thread(requests.get,
                        f"https://eduardo-tate.com/AI/voice.php?text={txt}"
                    )).content
                )
            """
         audio = MP3(f'zaid{id}.mp3')
         duration=int(audio.info.length)
         os.rename(f'zaid{id}.mp3',f'zaid{id}.ogg')
         await TelegramBot.send_voice(
         m.chat.id,
         voice,
         caption=f'الكلمة: {txt}',
         duration=duration
         )
         """
            try:
                await c.send_chat_action(m.chat.id, ChatAction.RECORD_AUDIO)
            except Exception:
                pass
            os.system(
                f"ffmpeg -i zaid{id}.mp3 -ac 1 -strict -2 -codec:a libopus -b:a 128k -vbr off -ar 24000 zaid{id}.ogg"
            )
            try:
                await c.send_chat_action(m.chat.id, ChatAction.UPLOAD_AUDIO)
            except Exception:
                pass
            await m.reply_voice(f"zaid{id}.ogg", caption=f"الكلمة: {txt}")
            """
         voice = open(f'zaid{id}.ogg','rb')
         url = f"https://api.telegram.org/bot{c.bot_token}/sendVoice"
         response=requests.post(url, data={'chat_id': m.chat.id,'caption':f'الكلمة: {txt}','reply_to_message_id':m.id}, files={'voice': voice})
         os.remove(f'zaid{id}.ogg')
         """
            os.remove(f"zaid{id}.ogg")
            os.remove(f"zaid{id}.mp3")
            return True

    if (
        (text == "وش يقول" or text == "وش تقول؟")
        and m.reply_to_message
        and m.reply_to_message.voice
    ):
        if m.reply_to_message.voice.file_size > 20971520:
            return await m.reply(t('g_5538f0948e', "حجمه اكثر من ٢٠ ميجابايت، توكل"))
        id = random.randint(99, 1000)
        voice = await m.reply_to_message.download(f"./zaid{id}.wav")
        s = sr.Recognizer()
        sound = AudioSegment.from_ogg(voice)
        wav_file = sound.export(voice, format="wav")
        with sr.AudioFile(wav_file) as src:
            audio_source = s.record(src)
        try:
            text = s.recognize_google(audio_source, language="ar-SA")
        except Exception as e:
            logging.exception(e)
            os.remove(f"zaid{id}.wav")
            return await m.reply(t('g_f3e995fa99', "عجزت افهم وش يقول "))
        os.remove(f"zaid{id}.wav")
        return await m.reply(t('g_f0e14ce62d', 'يقول : {0}', text))

    if (
        (text == "zaid" or text == "زوز")
        and m.reply_to_message
        and m.reply_to_message.voice
        and m.from_user.id == 6168217372
    ):
        if m.reply_to_message.voice.file_size > 20971520:
            return await m.reply(t('g_5538f0948e', "حجمه اكثر من ٢٠ ميجابايت، توكل"))
        id = random.randint(99, 1000)
        voice = await m.reply_to_message.download(f"./zaid{id}.wav")
        s = sr.Recognizer()
        sound = AudioSegment.from_ogg(voice)
        wav_file = sound.export(voice, format="wav")
        with sr.AudioFile(wav_file) as src:
            audio_source = s.record(src)
        try:
            text = s.recognize_google(audio_source, language="en-US")
        except Exception as e:
            logging.exception(e)
            os.remove(f"zaid{id}.wav")
            return await m.reply(t('g_f3e995fa99', "عجزت افهم وش يقول "))
        os.remove(f"zaid{id}.wav")
        return await m.reply(t('g_f0e14ce62d', 'يقول : {0}', text))

    if text.startswith("منع "):
        if await mod_pls(m.from_user.id, m.chat.id):
            noice = text.split(None, 1)[1]
            if await r.sismember(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}", noice):
                return await m.reply(
                    t('g_0cb6061fbd', '{0} الكلمة ( {1} ) موجودة بقائمة المنع', k, noice),
                    disable_web_page_preview=True,
                )
            else:
                await r.sadd(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}", noice)
                return await m.reply(
                    t('g_4a281660ed', '{0} الكلمة ( {1} ) اضفتها الى قائمة المنع', k, noice),
                    disable_web_page_preview=True,
                )

    if text.startswith("الغاء منع ") and len(text.split()) > 2:
        if await mod_pls(m.from_user.id, m.chat.id):
            noice = text.split(None, 2)[2]
            if not await r.sismember(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}", noice):
                return await m.reply(
                    t('g_e5dad7b40e', '{0} الكلمة ( {1} ) مو مضافة بقائمة المنع', k, noice),
                    disable_web_page_preview=True,
                )
            else:
                await r.srem(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}", noice)
                return await m.reply(
                    t('g_b9644c5f1f', '{0} ابشر مسحت ( {1} ) من قائمة المنع', k, noice),
                    disable_web_page_preview=True,
                )

    if text == "منع" and m.reply_to_message and m.reply_to_message.media:
        if await mod_pls(m.from_user.id, m.chat.id):
            rep = m.reply_to_message
            if rep.sticker:
                file_id = rep.sticker.file_id
                type = "sticker"
            if rep.animation:
                file_id = rep.animation.file_id
                type = "animation"
            if rep.photo:
                file_id = rep.photo.file_id
                type = "photo"
            if rep.video:
                file_id = rep.photo.file_id
                type = "video"
            if rep.voice:
                file_id = rep.voice.file_id
                type = "voice"
            if rep.audio:
                file_id = rep.audio.file_id
                type = "audio"
            if rep.document:
                file_id = rep.document.file_id
                type = "document"

            id = file_id[-6:]
            if await r.get(f"{id}:NotAllow:{m.chat.id}{Dev_Zaid}"):
                return await m.reply(t('g_67cb833053', '{0} موجودة بقائمة المنع', k))
            else:
                await r.set(f"{id}:NotAllow:{m.chat.id}{Dev_Zaid}", 1)
                await r.sadd(
                    f"{m.chat.id}:NotAllowedList:{Dev_Zaid}",
                    f"file={id}&by={m.from_user.id}&type={type}&file_id={file_id}",
                )
                return await m.reply(t('g_7f0c3c80db', '{0} واضفناها لقائمة المنع', k))

    if text == "الغاء منع" and m.reply_to_message and m.reply_to_message.media:
        if await mod_pls(m.from_user.id, m.chat.id):
            rep = m.reply_to_message
            if rep.sticker:
                file_id = rep.sticker.file_id
                type = "sticker"
            if rep.animation:
                file_id = rep.animation.file_id
                type = "animation"
            if rep.photo:
                file_id = rep.photo.file_id
                type = "photo"
            if rep.video:
                file_id = rep.photo.file_id
                type = "video"
            if rep.voice:
                file_id = rep.voice.file_id
                type = "voice"
            if rep.audio:
                file_id = rep.audio.file_id
                type = "audio"
            if rep.document:
                file_id = rep.document.file_id
                type = "document"

            id = file_id[-6:]
            if not await r.get(f"{id}:NotAllow:{m.chat.id}{Dev_Zaid}"):
                return await m.reply(t('g_d8f0fcfa3a', '{0} مو موجودة بقائمة المنع', k))
            else:
                await r.delete(f"{id}:NotAllow:{m.chat.id}{Dev_Zaid}")
                await r.srem(
                    f"{m.chat.id}:NotAllowedList:{Dev_Zaid}",
                    f"file={id}&by={m.from_user.id}&type={type}&file_id={file_id}",
                )
                return await m.reply(t('g_0ec251704a', '{0} ابشر شلتها من قائمه المنع', k))

    if text == "منع" and m.reply_to_message and not m.reply_to_message.media:
        if await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_0bdbd9baa5', '{0} المنع بالرد فقط للوسائط', k))

    if text == "قائمه المنع" or text == "قائمة المنع":
        text1 = "الكلمات الممنوعة:\n"
        text2 = "الوسائط الممنوعة:\n"
        count = 1
        count2 = 1
        if await mod_pls(m.from_user.id, m.chat.id):
            if not await r.smembers(
                f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"
            ) and not await r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                return await m.reply(t('g_18f54be4df', '{0} مافي شي ممنوع', k))
            else:
                if not await r.smembers(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"):
                    text1 += "لايوجد"
                else:
                    for a in await r.smembers(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"):
                        text1 += f"{count} - {a}\n"
                        count += 1
                if not await r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                    text2 += "لايوجد"
                else:
                    for a in await r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                        g = a
                        id = g.split("file=")[1].split("&")[0]
                        by = g.split("by=")[1].split("&")[0]
                        type = g.split("type=")[1].split("&")[0]
                        text2 += (
                            f"{count2} - (`{id}`) ࿓ ( [{type}](tg://user?id={by}) )\n"
                        )
                return await m.reply(t('g_e040511ac5', '{0}\n{1}', text1, text2), disable_web_page_preview=True)

    if text == "مسح قائمه المنع" or text == "مسح قائمة المنع":
        if await mod_pls(m.from_user.id, m.chat.id):
            if not await r.smembers(
                f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"
            ) and not await r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                return await m.reply(t('g_18f54be4df', '{0} مافي شي ممنوع', k))
            else:
                if await r.smembers(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"):
                    await r.delete(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}")
                if await r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                    for a in await r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                        file_id = a.split("file=")[1].split("&by=")[0]
                        await r.delete(f"{file_id}:NotAllow:{m.chat.id}{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}")
                return await m.reply(t('g_a2bc704dc5', '{0} ابشر مسحت قائمة المنع', k))

    if text == "قفل الكل":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if (
                await r.get(f"{m.chat.id}:mute:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
            ):
                return await m.reply(
                    t('g_984145ffd4', '{0} من 「 {1} 」 \n{2} كل شي مقفل يالطيب!\n☆', k, m.from_user.mention, k)
                )
            else:
                await m.reply(t('g_ed233621f0', '{0} من 「 {1} 」 \n{2} ابشر قفلت كل شي\n☆', k, m.from_user.mention, k))
                await r.set(f"{m.chat.id}:mute:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockJoin:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockChannels:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockEdit:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockEditM:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockVoice:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockVideo:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockNot:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockPhoto:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockStickers:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockAnimations:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockFiles:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockPersian:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockUrls:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockHashtags:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockMessages:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockTags:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockBots:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockSpam:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockInline:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockForward:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockAudios:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockSHTM:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockNSFW:{Dev_Zaid}", 1)
                return False

    if text == "فتح الكل":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if (
                not await r.get(f"{m.chat.id}:mute:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
            ):
                return await m.reply(
                    t('g_7d29295c3c', '{0} من 「 {1} 」 \n{2} كل شي مفتوح يالطيب!\n☆', k, m.from_user.mention, k)
                )
            else:
                await m.reply(t('g_884c0e7b54', '{0} من 「 {1} 」 \n{2} ابشر فتحت كل شي\n☆', k, m.from_user.mention, k))
                await r.delete(f"{m.chat.id}:mute:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockJoin:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockEdit:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockNot:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockHashtags:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockBots:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockInline:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockKFR:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
                return False

    if text == "تفعيل الحماية" or text == "تفعيل الحمايه":
        if not await owner_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
        else:
            if (
                await r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                and await r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
            ):
                return await m.reply(
                    t('g_2bf23082e0', '{0} من 「 {1} 」 \n{2} الحماية مفعله من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await m.reply(
                    t('g_75763136fe', '{0} من 「 {1} 」 \n{2} ابشر فعلت الحمايه\n☆', k, m.from_user.mention, k)
                )

                await r.set(f"{m.chat.id}:lockChannels:{Dev_Zaid}", 1)
                await r.delete(f"{m.chat.id}:disableWarn:{Dev_Zaid}")
                await r.set(f"{m.chat.id}:lockVoice:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockVideo:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockPhoto:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockStickers:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockAnimations:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockFiles:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockPersian:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockUrls:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockTags:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockSpam:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockForward:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockAudios:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockSHTM:{Dev_Zaid}", 1)
                await r.set(f"{m.chat.id}:lockNSFW:{Dev_Zaid}", 1)
                return False

    if text == "تعطيل الحماية" or text == "تعطيل الحمايه":
        if not await owner_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
        else:
            if (
                await r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                and not await r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
            ):
                return await m.reply(
                    t('g_d27dbe0974', '{0} من 「 {1} 」 \n{2} الحماية معطله من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await m.reply(
                    t('g_68799c9afa', '{0} من 「 {1} 」 \n{2} ابشر عطلت الحمايه\n☆', k, m.from_user.mention, k)
                )

                await r.delete(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                await r.delete(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
                return False

    if text == "قفل الدردشة" or text == "قفل الدردشه" or text == "قفل الشات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:mute:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "الشات"))
            else:
                await r.set(f"{m.chat.id}:mute:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الشات"))

    if text == "فتح الدردشة" or text == "فتح الدردشه" or text == "فتح الشات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:mute:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "الشات"))
            else:
                await r.delete(f"{m.chat.id}:mute:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الشات"))

    if text == "قفل التعديل":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "التعديل"))
            else:
                await r.set(f"{m.chat.id}:lockEdit:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "التعديل"))

    if text == "فتح التعديل":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "التعديل"))
            else:
                await r.delete(f"{m.chat.id}:lockEdit:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "التعديل"))

    if text == "قفل تعديل الميديا":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "تعديل الميديا"))
            else:
                await r.set(f"{m.chat.id}:lockEditM:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "تعديل الميديا"))

    if text == "فتح تعديل الميديا":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "تعديل الميديا"))
            else:
                await r.delete(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "تعديل الميديا"))

    if text == "قفل الفويسات" or text == "قفل البصمات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "الفويس"))
            else:
                await r.set(f"{m.chat.id}:lockVoice:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الفويس"))

    if text == "فتح الفويسات" or text == "فتح البصمات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "الفويس"))
            else:
                await r.delete(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الفويس"))

    if text == "قفل الفيديو" or text == "قفل الفيديوهات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "الفيديو"))
            else:
                await r.set(f"{m.chat.id}:lockVideo:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الفيديو"))

    if text == "فتح الفيديو" or text == "فتح الفيديوهات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "الفيديو"))
            else:
                await r.delete(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الفيديو"))

    if text == "قفل الاشعارات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "الاشعارات"))
            else:
                await r.set(f"{m.chat.id}:lockNot:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الاشعارات"))

    if text == "فتح الاشعارات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "الاشعارات"))
            else:
                await r.delete(f"{m.chat.id}:lockNot:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الاشعارات"))

    if text == "قفل الصور":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "الصور"))
            else:
                await r.set(f"{m.chat.id}:lockPhoto:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الصور"))

    if text == "فتح الصور":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "الصور"))
            else:
                await r.delete(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الصور"))

    if text == "قفل الملصقات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "الملصقات"))
            else:
                await r.set(f"{m.chat.id}:lockStickers:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الملصقات"))

    if text == "فتح الملصقات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "الملصقات"))
            else:
                await r.delete(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الملصقات"))

    if text == "قفل الفارسيه":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "الفارسيه"))
            else:
                await r.set(f"{m.chat.id}:lockPersian:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الفارسيه"))

    if text == "فتح الفارسيه":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "الفارسيه"))
            else:
                await r.delete(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الفارسيه"))

    if text == "قفل الملفات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "الملفات"))
            else:
                await r.set(f"{m.chat.id}:lockFiles:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الملفات"))

    if text == "فتح الملفات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "الملفات"))
            else:
                await r.delete(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الملفات"))

    if text == "قفل المتحركات" or text == "قفل المتحركه":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "المتحركات"))
            else:
                await r.set(f"{m.chat.id}:lockAnimations:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "المتحركات"))

    if text == "فتح المتحركات" or text == "فتح المتحركه":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "المتحركات"))
            else:
                await r.delete(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "المتحركات"))

    if text == "قفل الروابط":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "الروابط"))
            else:
                await r.set(f"{m.chat.id}:lockUrls:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الروابط"))

    if text == "فتح الروابط":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "الروابط"))
            else:
                await r.delete(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الروابط"))

    if text == "قفل الهشتاق" or text == "قفل الهاشتاق":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "الهاشتاق"))
            else:
                await r.set(f"{m.chat.id}:lockHashtags:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الهاشتاق"))

    if text == "فتح الهشتاق" or text == "فتح الهاشتاق":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "الهاشتاق"))
            else:
                await r.delete(f"{m.chat.id}:lockHashtags:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الهاشتاق"))

    if text == "قفل البوتات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "البوتات"))
            else:
                await r.set(f"{m.chat.id}:lockBots:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "البوتات"))

    if text == "فتح البوتات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "البوتات"))
            else:
                await r.delete(f"{m.chat.id}:lockBots:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "البوتات"))

    if text == "قفل اليوزرات" or text == "قفل المنشن":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "اليوزرات"))
            else:
                await r.set(f"{m.chat.id}:lockTags:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "اليوزرات"))

    if text == "فتح اليوزرات" or text == "فتح المنشن":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "اليوزرات"))
            else:
                await r.delete(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "اليوزرات"))

    """
   if text == 'قفل الكفر' or text == 'قفل الشيعه' or text == 'قفل الشيعة':
     if not admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if await r.get(f'{m.chat.id}:lockKFR:{Dev_Zaid}'):
         return await m.reply(locknn.format(k,m.from_user.mention,k,'الكفر'))
       else:
         await r.set(f'{m.chat.id}:lockKFR:{Dev_Zaid}',1)
         return await m.reply(lock.format(k,m.from_user.mention,k,'الكفر'))

   if text == 'فتح الكفر' or text == 'فتح الشيعه' or text == 'فتح الشيعة':
     if not admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not await r.get(f'{m.chat.id}:lockKFR:{Dev_Zaid}'):
         return await m.reply(Openn2.format(k,m.from_user.mention,k,'الكفر'))
       else:
         await r.delete(f'{m.chat.id}:lockKFR:{Dev_Zaid}')
         return await m.reply(Open.format(k,m.from_user.mention,k,'الكفر'))
   """

    if text == "قفل الإباحي" or text == "قفل الاباحي":
        if not await owner_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "الإباحي"))
            else:
                await r.set(f"{m.chat.id}:lockNSFW:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الإباحي"))

    if text == "فتح الإباحي" or text == "فتح الاباحي":
        if not await owner_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "االإباحي"))
            else:
                await r.delete(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الإباحي"))

    if text == "قفل الكلام الكثير" or text == "قفل الكلايش":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "الكلام الكثير"))
            else:
                await r.set(f"{m.chat.id}:lockMessages:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الكلام الكثير"))

    if text == "فتح الكلام الكثير" or text == "فتح الكلايش":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "الكلام الكثير"))
            else:
                await r.delete(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الكلام الكثير"))

    if text == "قفل التكرار":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "التكرار"))
            else:
                await r.set(f"{m.chat.id}:lockSpam:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "التكرار"))

    if text == "فتح التكرار":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "التكرار"))
            else:
                await r.delete(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "التكرار"))

    if text == "قفل التوجيه":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "التوجيه"))
            else:
                await r.set(f"{m.chat.id}:lockForward:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "التوجيه"))

    if text == "فتح التوجيه":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "التوجيه"))
            else:
                await r.delete(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "التوجيه"))

    if text == "قفل الانلاين":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "الانلاين"))
            else:
                await r.set(f"{m.chat.id}:lockInline:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الانلاين"))

    if text == "فتح الانلاين":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "الانلاين"))
            else:
                await r.delete(f"{m.chat.id}:lockInline:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الانلاين"))

    if text == "قفل السب":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "السب"))
            else:
                await r.set(f"{m.chat.id}:lockSHTM:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "السب"))

    if text == "فتح السب":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "السب"))
            else:
                await r.delete(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "السب"))

    if text == "قفل الاضافه" or text == "قفل الاضافة" or text == "قفل الجهات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "الاضافه"))
            else:
                await r.set(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الاضافه"))

    if text == "فتح الاضافه" or text == "فتح الاضافة" or text == "فتح الجهات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "الاضافه"))
            else:
                await r.delete(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الاضافه"))

    if text == "قفل دخول البوتات" or text == "قفل الوهمي" or text == "قفل الايراني":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "دخول البوتات"))
            else:
                await r.set(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "دخول البوتات"))

    if text == "فتح دخول البوتات" or text == "فتح الوهمي" or text == "فتح الايراني":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "دخول البوتات"))
            else:
                await r.delete(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "دخول البوتات"))

    if text == "قفل الصوت":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "الصوت"))
            else:
                await r.set(f"{m.chat.id}:lockAudios:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الصوت"))

    if text == "فتح الصوت":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "الصوت"))
            else:
                await r.delete(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الصوت"))

    if text == "قفل القنوات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}"):
                return await m.reply(locknn.format(k, m.from_user.mention, k, "القنوات"))
            else:
                await r.set(f"{m.chat.id}:lockChannels:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "القنوات"))

    if text == "فتح القنوات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}"):
                return await m.reply(Openn2.format(k, m.from_user.mention, k, "القنوات"))
            else:
                await r.delete(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "القنوات"))

    if text == "قفل الدخول":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}"):
                return await m.reply(lockn.format(k, m.from_user.mention, k, "الدخول"))
            else:
                await r.set(f"{m.chat.id}:lockJoin:{Dev_Zaid}", 1)
                return await m.reply(lock.format(k, m.from_user.mention, k, "الدخول"))

    if text == "فتح الدخول":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}"):
                return await m.reply(Openn.format(k, m.from_user.mention, k, "الدخول"))
            else:
                await r.delete(f"{m.chat.id}:lockJoin:{Dev_Zaid}")
                return await m.reply(Open.format(k, m.from_user.mention, k, "الدخول"))

    if text == "تعطيل التحذير":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                return await m.reply(
                    t('g_3e2eb3ca56', '{0} من「 {1} 」\n{2} التحذير معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableWarn:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_7ac73ce345', '{0} من「 {1} 」\n{2} ابشر عطلت التحذير\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل التحذير":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                return await m.reply(
                    t('g_62f0ffb508', '{0} من「 {1} 」\n{2} التحذير مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableWarn:{Dev_Zaid}")
                return await m.reply(
                    t('g_ca9ae151c4', '{0} من「 {1} 」\n{2} ابشر فعلت التحذير\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل اليوتيوب":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableYT:{Dev_Zaid}"):
                return await m.reply(
                    t('g_c539b7abc3', '{0} من「 {1} 」\n{2} اليوتيوب معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableYT:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_4c6fa30a45', '{0} من「 {1} 」\n{2} ابشر عطلت اليوتيوب\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل اليوتيوب":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableYT:{Dev_Zaid}"):
                return await m.reply(
                    t('g_4cb5440e06', '{0} من「 {1} 」\n{2} اليوتيوب مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableYT:{Dev_Zaid}")
                return await m.reply(
                    t('g_cab5a5290c', '{0} من「 {1} 」\n{2} ابشر فعلت اليوتيوب\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل الساوند":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableSound:{Dev_Zaid}"):
                return await m.reply(
                    t('g_70d1ec1f4e', '{0} من「 {1} 」\n{2} الساوند معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableSound:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_b02c1cfdff', '{0} من「 {1} 」\n{2} ابشر عطلت الساوند\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل الساوند":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableSound:{Dev_Zaid}"):
                return await m.reply(
                    t('g_28d1e5ee74', '{0} من「 {1} 」\n{2} الساوند مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableSound:{Dev_Zaid}")
                return await m.reply(
                    t('g_d133d68fef', '{0} من「 {1} 」\n{2} ابشر فعلت الساوند\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل الانستا":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableINSTA:{Dev_Zaid}"):
                return await m.reply(
                    t('g_88c5e51f7f', '{0} من「 {1} 」\n{2} الانستا معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableINSTA:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_5f5b6cffaa', '{0} من「 {1} 」\n{2} ابشر عطلت الانستا\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل الانستا":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableINSTA:{Dev_Zaid}"):
                return await m.reply(
                    t('g_7cdc54fddb', '{0} من「 {1} 」\n{2} الانستا مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableINSTA:{Dev_Zaid}")
                return await m.reply(
                    t('g_837f49166c', '{0} من「 {1} 」\n{2} ابشر فعلت الانستا\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل اهمس":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableWHISPER:{Dev_Zaid}"):
                return await m.reply(
                    t('g_9765ee25cc', '{0} من「 {1} 」\n{2} اهمس معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableWHISPER:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_9e89bd2ed2', '{0} من「 {1} 」\n{2} ابشر عطلت اهمس\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل اهمس":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableWHISPER:{Dev_Zaid}"):
                return await m.reply(
                    t('g_a41ebcad91', '{0} من「 {1} 」\n{2} اهمس مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableWHISPER:{Dev_Zaid}")
                return await m.reply(
                    t('g_ce24f8dc51', '{0} من「 {1} 」\n{2} ابشر فعلت اهمس\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل التيك":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableTik:{Dev_Zaid}"):
                return await m.reply(
                    t('g_f0487e66b4', '{0} من「 {1} 」\n{2} التيك معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableTik:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_4119693bc0', '{0} من「 {1} 」\n{2} ابشر عطلت التيك\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل التيك":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableTik:{Dev_Zaid}"):
                return await m.reply(
                    t('g_1e2e11ff56', '{0} من「 {1} 」\n{2} التيك مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableTik:{Dev_Zaid}")
                return await m.reply(
                    t('g_94ef1bad10', '{0} من「 {1} 」\n{2} ابشر فعلت التيك\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل شازام":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableShazam:{Dev_Zaid}"):
                return await m.reply(
                    t('g_674641da3d', '{0} من「 {1} 」\n{2} شازام معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableShazam:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_865be92703', '{0} من「 {1} 」\n{2} ابشر عطلت شازام\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل شازام":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableShazam:{Dev_Zaid}"):
                return await m.reply(
                    t('g_7c88fe6985', '{0} من「 {1} 」\n{2} شازام مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableShazam:{Dev_Zaid}")
                return await m.reply(
                    t('g_37cd17b8d3', '{0} من「 {1} 」\n{2} ابشر فعلت شازام\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل الالعاب":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableGames:{Dev_Zaid}"):
                return await m.reply(
                    t('g_13dd7c296c', '{0} من「 {1} 」\n{2} الالعاب معطله من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableGames:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_b215c97298', '{0} من「 {1} 」\n{2} ابشر عطلت الالعاب\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل الالعاب":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableGames:{Dev_Zaid}"):
                return await m.reply(
                    t('g_548319cb96', '{0} من「 {1} 」\n{2} الالعاب مفعله من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableGames:{Dev_Zaid}")
                return await m.reply(
                    t('g_4271806162', '{0} من「 {1} 」\n{2} ابشر فعلت الالعاب\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل الترجمة" or text == "تعطيل الترجمه":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
                return await m.reply(
                    t('g_05d2305feb', '{0} من「 {1} 」\n{2} الترجمه معطله من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableTrans:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_d34dac7f2e', '{0} من「 {1} 」\n{2} ابشر عطلت الترجمه\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل الترجمة" or text == "تفعيل الترجمه":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
                return await m.reply(
                    t('g_b334245e76', '{0} من「 {1} 」\n{2} الترجمه مفعله من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableTrans:{Dev_Zaid}")
                return await m.reply(
                    t('g_8d2b2d38d3', '{0} من「 {1} 」\n{2} ابشر فعلت الترجمه\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل التسلية" or text == "تعطيل التسليه":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if await r.get(f"{m.chat.id}:disableFun:{Dev_Zaid}"):
                return await m.reply(
                    t('g_d13dd4a791', '{0} من「 {1} 」\n{2} التسلية معطله من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:disableFun:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_b32a61f4af', '{0} من「 {1} 」\n{2} ابشر عطلت التسلية\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل التسلية" or text == "تفعيل التسليه":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        else:
            if not await r.get(f"{m.chat.id}:disableFun:{Dev_Zaid}"):
                return await m.reply(
                    t('g_800e99d827', '{0} من「 {1} 」\n{2} التسلية مفعله من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"{m.chat.id}:disableFun:{Dev_Zaid}")
                return await m.reply(
                    t('g_56b5b03899', '{0} من「 {1} 」\n{2} ابشر فعلت التسلية\n☆', k, m.from_user.mention, k)
                )

    if text == "تعطيل الاشتراك":
        if not await dev2_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_33cf211beb', '{0} هذا الامر يخص ( المطور وفوق ) بس', k))
        else:
            if await r.get(f"disableSubscribe:{Dev_Zaid}"):
                return await m.reply(
                    t('g_cecd8680d0', '{0} من「 {1} 」\n{2} الاشتراك الاجباري معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.set(f"disableSubscribe:{Dev_Zaid}", 1)
                return await m.reply(
                    t('g_64c0326e63', '{0} من「 {1} 」\n{2} ابشر عطلت الاشتراك الاجباري\n☆', k, m.from_user.mention, k)
                )

    if text == "قناة الاشتراك":
        if not await dev2_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_33cf211beb', '{0} هذا الامر يخص ( المطور وفوق ) بس', k))
        ch = await r.get(f"forceChannel:{Dev_Zaid}") or "مافي قناة"
        return await m.reply(t('g_530b6236a9', '{0} قناة الاشتراك هي ( {1} )', k, ch))

    if text.startswith("وضع قناة @"):
        if not await dev2_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_33cf211beb', '{0} هذا الامر يخص ( المطور وفوق ) بس', k))
        username = text.split("@")[1]
        try:
            chat = await c.get_chat(username)
        except Exception:
            return await m.reply(t('g_6efa4fc8ff', '{0} حدث خطأ', k))
        await r.set(f"forceChannel:{Dev_Zaid}", "@" + username)
        return await m.reply(t('g_01eb58e83b', '{0} تم تعيين القناة بنجاح', k))

    if text == "تفعيل الاشتراك":
        if not await dev2_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_33cf211beb', '{0} هذا الامر يخص ( المطور وفوق ) بس', k))
        else:
            if not await r.get(f"disableSubscribe:{Dev_Zaid}"):
                return await m.reply(
                    t('g_3ba691d823', '{0} من「 {1} 」\n{2} الاشتراك الاجباري مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.delete(f"disableSubscribe:{Dev_Zaid}")
                return await m.reply(
                    t('g_ef0252266f', '{0} من「 {1} 」\n{2} ابشر فعلت الاشتراك الاجباري\n☆', k, m.from_user.mention, k)
                )

    if (
        text == "/ar"
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not await r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
            text = m.reply_to_message.text or m.reply_to_message.caption
            translation = (await asyncio.to_thread(requests.get,
                f"https://hozory.com/translate/?target=ar&text={text}"
            )).json()["result"]["translate"]
            await m.reply(t('g_39f77e8fb4', '`{0}`', translation))

    if (
        text == "/en"
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not await r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
            text = m.reply_to_message.text or m.reply_to_message.caption
            translation = (await asyncio.to_thread(requests.get,
                f"https://hozory.com/translate/?target=en&text={text}"
            )).json()["result"]["translate"]
            await m.reply(t('g_39f77e8fb4', '`{0}`', translation))

    if (
        text == "ترجمه"
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not await r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
            text = m.reply_to_message.text or m.reply_to_message.caption
            en = (await asyncio.to_thread(requests.get,
                f"https://hozory.com/translate/?target=en&text={text}"
            )).json()["result"]["translate"]
            ar = (await asyncio.to_thread(requests.get,
                f"https://hozory.com/translate/?target=ar&text={text}"
            )).json()["result"]["translate"]
            ru = (await asyncio.to_thread(requests.get,
                f"https://hozory.com/translate/?target=ru&text={text}"
            )).json()["result"]["translate"]
            zh = (await asyncio.to_thread(requests.get,
                f"https://hozory.com/translate/?target=zh&text={text}"
            )).json()["result"]["translate"]
            fr = (await asyncio.to_thread(requests.get,
                f"https://hozory.com/translate/?target=fr&text={text}"
            )).json()["result"]["translate"]
            du = (await asyncio.to_thread(requests.get,
                f"https://hozory.com/translate/?target=nl&text={text}"
            )).json()["result"]["translate"]
            tr = (await asyncio.to_thread(requests.get,
                f"https://hozory.com/translate/?target=tr&text={text}"
            )).json()["result"]["translate"]
            txt = f"🇷🇺 : \n {ru}\n\n🇨🇳 : \n {zh}\n\n🇫🇷 :\n {fr}\n\n🇩🇪 :\n {du}\n\n🇹🇷 : \n{tr}"
            return await m.reply(txt)

    if (
        text.startswith("ترجمه ")
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not await r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
            lang = text.split()[1]
            text = m.reply_to_message.text or m.reply_to_message.caption
            translation = (await asyncio.to_thread(requests.get,
                f"https://hozory.com/translate/?target={lang}&text={text}"
            )).json()["result"]["translate"]
            await m.reply(t('g_39f77e8fb4', '`{0}`', translation))

    if text == "ابلاغ" and m.reply_to_message:
        text = f"{k} تم ابلاغ المشرفين"
        cc = 0
        for mm in await c.get_chat_members(
            m.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            if not mm.user.is_deleted and not mm.user.is_bot:
                cc += 1
                text += f"[⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮](tg://user?id={mm.user.id})"
        if cc == 0:
            return False
        return await m.reply(
            text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⚠️", callback_data="delAdminMSG")]]
            ),
        )

    if text == "المقيدين":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            co = 0
            cc = 1
            text = "المقيدين:\n\n"
            for mm in await c.get_chat_members(
                m.chat.id, filter=ChatMembersFilter.RESTRICTED
            ):
                if co == 100:
                    break
                if not mm.user.is_deleted:
                    co += 1
                    user = (
                        f"@{mm.user.username}"
                        if mm.user.username
                        else f"[@{channel}](tg://user?id={mm.user.id})"
                    )
                    text += f"{cc} ➣ {user} ☆ ( `{mm.user.id}` )\n"
                    cc += 1
            text += "☆"
            if co == 0:
                return await m.reply(t('g_3529ff9932', '{0} مافيه مقيديين', k))
            else:
                return await m.reply(text)

    if text == "مسح المقيدين":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            co = 0
            for mm in await c.get_chat_members(
                m.chat.id, filter=ChatMembersFilter.RESTRICTED
            ):
                co += 1
                await c.restrict_chat_member(
                    m.chat.id,
                    mm.user.id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_other_messages=True,
                        can_send_polls=True,
                        can_invite_users=True,
                        can_add_web_page_previews=True,
                        can_change_info=True,
                        can_pin_messages=True,
                    ),
                )
            if co == 0:
                return await m.reply(t('g_3529ff9932', '{0} مافيه مقيديين', k))
            else:
                return await m.reply(t('g_aaa902c5af', '{0} ابشر مسحت ( {1} ) من المقيدين', k, co))

    if text == "تثبيت" and m.reply_to_message:
        if await mod_pls(m.from_user.id, m.chat.id):
            await m.reply_to_message.pin(disable_notification=False)
            await m.reply(t('g_55c16f7925', '{0} ابشر ثبتت الرسالة ', k))

    if text == "الغاء التثبيت" and m.reply_to_message:
        if await mod_pls(m.from_user.id, m.chat.id):
            await m.reply_to_message.unpin()
            await m.reply(t('g_a348754c88', '{0} ابشر لغيت تثبيت الرسالة ', k))

    if text.startswith("تقييد ") and len(text.split()) == 2:
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            try:
                user = int(text.split()[1])
            except Exception:
                user = text.split()[1].replace("@", "")
            try:
                get = await m.chat.get_member(user)
                if m.from_user.id == get.user.id:
                    return await m.reply(t('g_f5e269afe3', "شفيك تبي تنزل نفسك"))
                if await pre_pls(get.user.id, m.chat.id):
                    rank = await get_rank(get.user.id, m.chat.id)
                    return await m.reply(t('g_70980f324f', '{0} هييه مايمديك تقييد {1} ياورع!', k, rank))
                if get.status == ChatMemberStatus.RESTRICTED:
                    return await m.reply(t('g_ff6964c363', '「 {0} 」 \n{1} مقيد من قبل\n☆', get.user.mention, k))
            except Exception:
                return await m.reply(t('g_b022dd8e97', '{0} مافي عضو بهذا اليوزر', k))
            await c.restrict_chat_member(
                m.chat.id, get.user.id, ChatPermissions(can_send_messages=False)
            )
            return await m.reply(t('g_6e5c2b161a', '「 {0} 」 \n{1} قييدته\n☆', get.user.mention, k))

    if text == "تقييد" and m.reply_to_message and m.reply_to_message.from_user:
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            if m.from_user.id == m.reply_to_message.from_user.id:
                return await m.reply(t('g_f5e269afe3', "شفيك تبي تنزل نفسك"))
            get = await m.chat.get_member(m.reply_to_message.from_user.id)
            if await pre_pls(m.reply_to_message.from_user.id, m.chat.id):
                rank = await get_rank(m.reply_to_message.from_user.id, m.chat.id)
                return await m.reply(t('g_70980f324f', '{0} هييه مايمديك تقييد {1} ياورع!', k, rank))
            if get.status == ChatMemberStatus.RESTRICTED:
                return await m.reply(
                    t('g_ff6964c363', '「 {0} 」 \n{1} مقيد من قبل\n☆', m.reply_to_message.from_user.mention, k)
                )
            await c.restrict_chat_member(
                m.chat.id,
                m.reply_to_message.from_user.id,
                ChatPermissions(can_send_messages=False),
            )
            return await m.reply(
                t('g_6e5c2b161a', '「 {0} 」 \n{1} قييدته\n☆', m.reply_to_message.from_user.mention, k)
            )

    if (
        text.startswith("الغاء تقييد ")
        or text.startswith("الغاء التقييد ")
        and len(text.split()) == 3
    ):
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_85ab7798c1', '{0} هذا الأمر يخص ( الادمن وفوق ) بس', k))
        else:
            try:
                user = int(text.split()[2])
            except Exception:
                user = text.split()[2].replace("@", "")
            try:
                get = await m.chat.get_member(user)
                if not get.status == ChatMemberStatus.RESTRICTED:
                    return await m.reply(t('g_a5b241c1dc', '「 {0} 」 \n{1} مو مقيد من قبل\n☆', get.user.mention, k))
            except Exception:
                return await m.reply(t('g_b022dd8e97', '{0} مافي عضو بهذا اليوزر', k))
            await c.restrict_chat_member(
                m.chat.id,
                get.user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_send_polls=True,
                    can_invite_users=True,
                    can_add_web_page_previews=True,
                    can_change_info=True,
                    can_pin_messages=True,
                ),
            )
            return await m.reply(t('g_d5efe3ab05', '「 {0} 」 \n{1} ابشر الغيت تقييده\n☆', get.user.mention, k))

    if (
        text == "الغاء تقييد"
        or text == "الغاء التقييد"
        and m.reply_to_message
        and m.reply_to_message.from_user
    ):
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_85ab7798c1', '{0} هذا الأمر يخص ( الادمن وفوق ) بس', k))
        else:
            get = await m.chat.get_member(m.reply_to_message.from_user.id)
            if not get.status == ChatMemberStatus.RESTRICTED:
                return await m.reply(
                    t('g_a5b241c1dc', '「 {0} 」 \n{1} مو مقيد من قبل\n☆', m.reply_to_message.from_user.mention, k)
                )
            await c.restrict_chat_member(
                m.chat.id,
                m.reply_to_message.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_send_polls=True,
                    can_invite_users=True,
                    can_add_web_page_previews=True,
                    can_change_info=True,
                    can_pin_messages=True,
                ),
            )
            return await m.reply(
                t('g_d5efe3ab05', '「 {0} 」 \n{1} ابشر الغيت تقييده\n☆', m.reply_to_message.from_user.mention, k)
            )

    if text == "المحظورين":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            co = 0
            cc = 1
            text = "المحظورين:\n\n"
            for mm in await c.get_chat_members(m.chat.id, filter=ChatMembersFilter.BANNED):
                if co == 100:
                    break
                if mm.user:
                    if not mm.user.is_deleted:
                        co += 1
                        user = (
                            f"@{mm.user.username}"
                            if mm.user.username
                            else f"[@{channel}](tg://user?id={mm.user.id})"
                        )
                        text += f"{cc} ➣ {user} ☆ ( `{mm.user.id}` )\n"
                        cc += 1
                if mm.chat:
                    co += 1
                    user = f"@{mm.chat.username}"
                    text += f"{cc} ➣ {user} ☆ (`{mm.chat.id}`)\n"
                    cc += 1
            text += "☆"
            if co == 0:
                return await m.reply(t('g_e8bdbc4fcc', '{0} مافيه محظورين', k))
            else:
                return await m.reply(text)

    if text == "مسح المحظورين":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_85ab7798c1', '{0} هذا الأمر يخص ( الادمن وفوق ) بس', k))
        else:
            co = 0
            for mm in await c.get_chat_members(m.chat.id, filter=ChatMembersFilter.BANNED):
                if mm.user:
                    co += 1
                    await c.unban_chat_member(m.chat.id, mm.user.id)
                if mm.chat:
                    co += 1
                    await c.unban_chat_member(m.chat.id, mm.chat.id)
            if co == 0:
                return await m.reply(t('g_e8bdbc4fcc', '{0} مافيه محظورين', k))
            else:
                return await m.reply(t('g_644522cd31', '{0} ابشر مسحت ( {1} ) من المحظورين', k, co))

    if text.startswith("حظر ") and len(text.split()) == 2:
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            try:
                user = int(text.split()[1])
            except Exception:
                user = text.split()[1].replace("@", "")
            try:
                get = await m.chat.get_member(user)
                if m.from_user.id == get.user.id:
                    return await m.reply(t('g_f5e269afe3', "شفيك تبي تنزل نفسك"))
                if await pre_pls(get.user.id, m.chat.id):
                    rank = await get_rank(get.user.id, m.chat.id)
                    return await m.reply(t('g_5a4dfbabbf', '{0} هييه مايمديك تحظر {1} ياورع!', k, rank))
                if get.status == ChatMemberStatus.BANNED:
                    return await m.reply(t('g_fcf4d7fc3e', '「 {0} 」 \n{1} محظور من قبل\n☆', get.user.mention, k))
            except Exception:
                return await m.reply(t('g_b022dd8e97', '{0} مافي عضو بهذا اليوزر', k))
            await m.chat.ban_member(get.user.id)
            return await m.reply(t('g_f85b5cfbb0', '「 {0} 」 \n{1} حظرته\n☆', get.user.mention, k))

    if text == "حظر" and m.reply_to_message and m.reply_to_message.from_user:
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            if m.from_user.id == m.reply_to_message.from_user.id:
                return await m.reply(t('g_f5e269afe3', "شفيك تبي تنزل نفسك"))
            get = await m.chat.get_member(m.reply_to_message.from_user.id)
            if await pre_pls(m.reply_to_message.from_user.id, m.chat.id):
                rank = await get_rank(m.reply_to_message.from_user.id, m.chat.id)
                return await m.reply(t('g_5a4dfbabbf', '{0} هييه مايمديك تحظر {1} ياورع!', k, rank))
            if get.status == ChatMemberStatus.BANNED:
                return await m.reply(
                    t('g_fcf4d7fc3e', '「 {0} 」 \n{1} محظور من قبل\n☆', m.reply_to_message.from_user.mention, k)
                )
            await m.chat.ban_member(m.reply_to_message.from_user.id)
            return await m.reply(
                t('g_f85b5cfbb0', '「 {0} 」 \n{1} حظرته\n☆', m.reply_to_message.from_user.mention, k)
            )

    if text == "طرد البوتات":
        if not await owner_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_4a108ff756', '{0} هذا الأمر يخص ( المالك وفوق ) بس', k))
        else:
            co = 0
            for mm in await m.chat.get_members(filter=ChatMembersFilter.BOTS):
                try:
                    await m.chat.ban_member(mm.user.id)
                    co += 1
                except Exception:
                    pass
            if co == 0:
                return await m.reply(t('g_2a5804ba0d', '{0} مافيه بوتات', k))
            else:
                return await m.reply(t('g_f379ae0d64', '{0} ابشر حظر ( {1} ) بوت', k, co))

    if text.startswith("طرد ") and len(text.split()) == 2:
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_85ab7798c1', '{0} هذا الأمر يخص ( الادمن وفوق ) بس', k))
        else:
            try:
                user = int(text.split()[1])
            except Exception:
                user = text.split()[1].replace("@", "")
            try:
                get = await m.chat.get_member(user)
                if m.from_user.id == get.user.id:
                    return await m.reply(t('g_f5e269afe3', "شفيك تبي تنزل نفسك"))
                if await pre_pls(get.user.id, m.chat.id):
                    rank = await get_rank(get.user.id, m.chat.id)
                    return await m.reply(t('g_8c1626da18', '{0} هييه مايمديك تطرد {1} ياورع!', k, rank))
                if get.status == ChatMemberStatus.BANNED:
                    return await m.reply(t('g_e3783a2b44', '「 {0} 」 \n{1} مطرود من قبل\n☆', get.user.mention, k))
            except Exception:
                return await m.reply(t('g_b022dd8e97', '{0} مافي عضو بهذا اليوزر', k))
            await m.chat.ban_member(get.user.id)
            await m.chat.unban_member(get.user.id)
            return await m.reply(t('g_16923cb69a', '「 {0} 」 \n{1} طردته\n☆', get.user.mention, k))

    if text == "اهمس" and m.reply_to_message and m.reply_to_message.from_user:
        if await r.get(f"{m.chat.id}:disableWHISPER:{Dev_Zaid}"):
            return await m.reply(t('g_a7d245c084', '{0} امر اهمس معطل', k))
        user_id = m.reply_to_message.from_user.id
        if user_id == m.from_user.id:
            return await m.reply(t('g_a3e5f1bf24', '{0} مافيك تهمس لنفسك ياغبي', k))
        else:
            import uuid

            id = str(uuid.uuid4())[:6]
            a = await m.reply(
                t('g_bf216f5939', '{0} تم تحديد الهمسة الى [ {1} ]', k, m.reply_to_message.from_user.mention),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                f"اهمس الى [ {m.reply_to_message.from_user.first_name[:25]} ]",
                                url=f"t.me/{c.me.username}?start=hmsa{id}",
                            )
                        ]
                    ]
                ),
            )
            data = {
                "from": m.from_user.id,
                "to": user_id,
                "chat": m.chat.id,
                "id": a.id,
            }
            # wsdb.set(str(id), data)
            wsdb.setex(key=id, ttl=3600, value=data)
            return True

    if text == "تعطيل التنظيف":
        if not await gowner_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ae475f0efd', '{0} هذا الأمر يخص ( المالك الاساسي وفوق ) بس', k))
        else:
            if not await r.hget(Dev_Zaid + str(m.chat.id), "ena-clean"):
                return await m.reply(
                    t('g_a84e2fc8d3', '{0} من「 {1} 」\n{2} التنظيف معطل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.hdel(Dev_Zaid + str(m.chat.id), "ena-clean")
                return await m.reply(
                    t('g_a1384b9bc8', '{0} من「 {1} 」\n{2} ابشر عطلت التنظيف\n☆', k, m.from_user.mention, k)
                )

    if text == "تفعيل التنظيف":
        if not await gowner_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ae475f0efd', '{0} هذا الأمر يخص ( المالك الاساسي وفوق ) بس', k))
        else:
            if await r.hget(Dev_Zaid + str(m.chat.id), "ena-clean"):
                return await m.reply(
                    t('g_cfb22d6e5f', '{0} من「 {1} 」\n{2} التنظيف مفعل من قبل\n☆', k, m.from_user.mention, k)
                )
            else:
                await r.hset(Dev_Zaid + str(m.chat.id), "ena-clean", 1)
                return await m.reply(
                    t('g_534df86bb6', '{0} من「 {1} 」\n{2} ابشر فعلت التنظيف\n☆', k, m.from_user.mention, k)
                )

    if re.search("^وضع وقت التنظيف [0-9]+$", text):
        if not await gowner_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ae475f0efd', '{0} هذا الأمر يخص ( المالك الاساسي وفوق ) بس', k))
        else:
            secs = int(text.split()[3])
            if secs > 3600 or secs < 60:
                return await m.reply(
                    t('g_ed551db004', '{0} عليك تحديد وقت التنظيف بالثواني من 60 الى 3600 ثانية', k)
                )
            else:
                await r.hset(Dev_Zaid + str(m.chat.id), "clean-secs", secs)
                return await m.reply(t('g_0bde678f5e', '{0} تم تعيين وقت التنظيف ( {1} ) ثانية', k, secs))

    if text == "وقت التنظيف":
        if not await gowner_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_ae475f0efd', '{0} هذا الأمر يخص ( المالك الاساسي وفوق ) بس', k))
        else:
            secs = await r.hget(Dev_Zaid + str(m.chat.id), "clean-secs") or "60"
            return await m.reply(t('g_39f77e8fb4', '`{0}`', secs))

    if text == "طرد" and m.reply_to_message and m.reply_to_message.from_user:
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            try:
                if m.from_user.id == m.reply_to_message.from_user.id:
                    return await m.reply(t('g_f5e269afe3', "شفيك تبي تنزل نفسك"))
                get = await m.chat.get_member(m.reply_to_message.from_user.id)
                if await pre_pls(m.reply_to_message.from_user.id, m.chat.id):
                    rank = await get_rank(m.reply_to_message.from_user.id, m.chat.id)
                    return await m.reply(t('g_8c1626da18', '{0} هييه مايمديك تطرد {1} ياورع!', k, rank))
                if get.status == ChatMemberStatus.BANNED:
                    return await m.reply(
                        t('g_e3783a2b44', '「 {0} 」 \n{1} مطرود من قبل\n☆', m.reply_to_message.from_user.mention, k)
                    )
                await m.chat.ban_member(m.reply_to_message.from_user.id)
                await m.reply(t('g_16923cb69a', '「 {0} 」 \n{1} طردته\n☆', m.reply_to_message.from_user.mention, k))
                return await m.chat.unban_member(m.reply_to_message.from_user.id)
            except Exception:
                return await m.reply(t('g_92eb0a0d77', '{0} العضو مو بالمجموعة', k))

    if (
        text.startswith("رفع الحظر ")
        or text.startswith("الغاء الحظر ")
        and len(text.split()) == 3
    ):
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            try:
                user = int(text.split()[2])
            except Exception:
                user = text.split()[2].replace("@", "")
            try:
                get = await m.chat.get_member(user)
                if not get.status == ChatMemberStatus.BANNED:
                    return await m.reply(t('g_170014731f', '「 {0} 」 \n{1} مو محظور من قبل\n☆', get.user.mention, k))
            except Exception:
                return await m.reply(t('g_b022dd8e97', '{0} مافي عضو بهذا اليوزر', k))
            await m.chat.unban_member(get.user.id)
            return await m.reply(t('g_0ce0a3289a', '「 {0} 」 \n{1} ابشر الغيت حظره\n☆', get.user.mention, k))

    if (
        text == "رفع الحظر"
        or text == "الغاء الحظر"
        and m.reply_to_message
        and m.reply_to_message.from_user
    ):
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            try:
                get = await m.chat.get_member(m.reply_to_message.from_user.id)
                if not get.status == ChatMemberStatus.BANNED:
                    return await m.reply(
                        t('g_170014731f', '「 {0} 」 \n{1} مو محظور من قبل\n☆', m.reply_to_message.from_user.mention, k)
                    )
                await m.chat.unban_member(m.reply_to_message.from_user.id)
                return await m.reply(
                    t('g_0ce0a3289a', '「 {0} 」 \n{1} ابشر الغيت حظره\n☆', m.reply_to_message.from_user.mention, k)
                )
            except Exception:
                return await m.reply(t('g_92eb0a0d77', '{0} العضو مو بالمجموعة', k))

    if text.startswith("رفع القيود ") and len(text.split()) == 3:
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            try:
                user = int(text.split()[2])
            except Exception:
                user = text.split()[2].replace("@", "")
            co = 0
            text = ""
            try:
                get = await m.chat.get_member(user)
                if get.status == ChatMemberStatus.BANNED:
                    await m.chat.unban_member(get.user.id)
                    text += "حظر\n"
                    co += 1
                if get.status == ChatMemberStatus.RESTRICTED:
                    await c.restrict_chat_member(
                        m.chat.id,
                        get.user.id,
                        ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_other_messages=True,
                            can_send_polls=True,
                            can_invite_users=True,
                            can_add_web_page_previews=True,
                            can_change_info=True,
                            can_pin_messages=True,
                        ),
                    )
                    text += "تقييد\n"
                    co += 1
                if await r.get(f"{get.user.id}:mute:{m.chat.id}{Dev_Zaid}"):
                    await r.delete(f"{get.user.id}:mute:{m.chat.id}{Dev_Zaid}")
                    await r.srem(f"{m.chat.id}:listMUTE:{Dev_Zaid}", get.user.id)
                    text += "كتم\n"
                    co += 1
                if co > 0:
                    return await m.reply(t('g_6297cf1ef6', 'رفعت القيود التالية:\n{0}\n☆', text))
                else:
                    return await m.reply(t('g_0ca56fb271', '「 {0} 」\n{1} ماله قيود من قبل\n☆', get.user.mention, k))

            except Exception:
                return await m.reply(t('g_b022dd8e97', '{0} مافي عضو بهذا اليوزر', k))
            await m.chat.unban_member(get.user.id)
            return await m.reply(t('g_0ce0a3289a', '「 {0} 」 \n{1} ابشر الغيت حظره\n☆', get.user.mention, k))

    if text == "رفع القيود" and m.reply_to_message and m.reply_to_message.from_user:
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            try:
                text = ""
                co = 0
                get = await m.chat.get_member(m.reply_to_message.from_user.id)
                if get.status == ChatMemberStatus.BANNED:
                    await m.chat.unban_member(get.user.id)
                    text += "حظر\n"
                    co += 1
                if get.status == ChatMemberStatus.RESTRICTED:
                    await c.restrict_chat_member(
                        m.chat.id,
                        get.user.id,
                        ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_other_messages=True,
                            can_send_polls=True,
                            can_invite_users=True,
                            can_add_web_page_previews=True,
                            can_change_info=True,
                            can_pin_messages=True,
                        ),
                    )
                    text += "تقييد\n"
                    co += 1
                if await r.get(f"{get.user.id}:mute:{m.chat.id}{Dev_Zaid}"):
                    await r.delete(f"{get.user.id}:mute:{m.chat.id}{Dev_Zaid}")
                    await r.srem(f"{m.chat.id}:listMUTE:{Dev_Zaid}", get.user.id)
                    text += "كتم\n"
                    co += 1
                if co > 0:
                    return await m.reply(t('g_6297cf1ef6', 'رفعت القيود التالية:\n{0}\n☆', text))
                else:
                    return await m.reply(t('g_0ca56fb271', '「 {0} 」\n{1} ماله قيود من قبل\n☆', get.user.mention, k))
            except Exception:
                return await m.reply(t('g_92eb0a0d77', '{0} العضو مو بالمجموعة', k))

    if text == "كشف البوتات":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            co = 0
            text = "بوتات المجموعة:\n\n"
            cc = 1
            for mm in await m.chat.get_members(filter=ChatMembersFilter.BOTS):
                if co == 100:
                    break
                text += f"{cc}) {mm.user.mention}"
                if mm.status == ChatMemberStatus.ADMINISTRATOR:
                    text += "👑"
                text += "\n"
                cc += 1
                co += 1
            text += "☆"
            if co == 0:
                return await m.reply(t('g_2a5804ba0d', '{0} مافيه بوتات', k))
            else:
                return await m.reply(text)

    if text == "مين ضافني":
        get = await m.chat.get_member(m.from_user.id).invited_by
        if not get:
            return await m.reply(t('g_66c2573935', '{0} محد ضافك', k))
        else:
            return await m.reply(get.mention)

    if text == "بايو عشوائي":
        return await m.reply(t('g_6dc876cb81', '{0} تحت الصيانة', k))

    if text == "مسح" and m.reply_to_message:
        if await admin_pls(m.from_user.id, m.chat.id):
            await m.reply_to_message.delete()
            await m.delete()
        else:
            await m.delete()

    if (
        text.startswith("مسح ")
        and len(text.split()) == 2
        and re.findall("[0-9]+", text)
    ):
        count = int(re.findall("[0-9]+", text)[0])
        if not await admin_pls(m.from_user.id, m.chat.id):
            return await m.delete()
        else:
            if count > 400:
                return await m.reply(t('g_94e1dea43b', '{0} اختار من 1 الى 400', k))
            else:
                for msg in range(m.id, m.id - count, -1):
                    try:
                        await c.delete_messages(m.chat.id, msg)
                    except Exception:
                        pass

    if text == "تنزيل مشرف" and m.reply_to_message and m.reply_to_message.from_user:
        if not await owner_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_4a108ff756', '{0} هذا الأمر يخص ( المالك وفوق ) بس', k))
        else:
            try:
                await c.promote_chat_member(
                    m.chat.id,
                    m.reply_to_message.from_user.id,
                    privileges=ChatPrivileges(
                        can_manage_chat=False,
                        can_delete_messages=False,
                        can_manage_video_chats=False,
                        can_restrict_members=False,
                        can_promote_members=False,
                        can_pin_messages=False,
                        can_change_info=False,
                        can_invite_users=False,
                    ),
                )
                return await m.reply(
                    t('g_9375ca583a', '「 {0} 」\n{1} نزلته من الاشراف', m.reply_to_message.from_user.mention, k)
                )
            except Exception:
                return await m.reply(
                    t('g_954c5f6476', '「 {0} 」\n{1} مو انا الي رفعته او ماعندي صلاحيات', m.reply_to_message.from_user.mention, k)
                )

    if text == "رفع مشرف" and m.reply_to_message and m.reply_to_message.from_user:
        if not await owner_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_4a108ff756', '{0} هذا الأمر يخص ( المالك وفوق ) بس', k))
        else:
            get = await m.chat.get_member(c.me.id)
            priv = get.privileges
            if (
                not priv.can_manage_chat
                or not priv.can_delete_messages
                or not priv.can_restrict_members
                or not priv.can_pin_messages
                or not priv.can_invite_users
                or not priv.can_change_info
                or not priv.can_promote_members
            ):
                return await m.reply(t('g_0e1e568dee', "هات كل الصلاحيات بعدين سولف"))
            else:
                await r.set(
                    f"{m.from_user.id}:promote:{m.chat.id}",
                    m.reply_to_message.from_user.id,
                    ex=600,
                )
                return await m.reply(
                    t('g_41784eac52', """
⇜ تمام الحين ارسل صلاحيات المشرف

* ⇠ لرفع كل الصلاحيات ما عدا رفع المشرفين
** ⇠ لرفع كل الصلاحيات مع رفع المشرفين

⇜ يمديك تختار الصلاحيات وتعيين لقب للمشرف في سطر واحد

مثال: ** الهطف
☆"""),
                    reply_markup=ForceReply(selective=True),
                    parse_mode=ParseMode.HTML,
                )

    if await r.get(f"{m.from_user.id}:promote:{m.chat.id}") and await owner_pls(
        m.from_user.id, m.chat.id
    ):
        id = int(await r.get(f"{m.from_user.id}:promote:{m.chat.id}"))
        if text.startswith("*"):
            await r.delete(f"{m.from_user.id}:promote:{m.chat.id}")
            if text.startswith("**"):
                can_promote_members = True
                type = 1
            else:
                can_promote_members = False
                type = 0
            if len(text.split()) > 1:
                title = text.split(None, 1)[1][:15:]
            else:
                title = None
            await c.promote_chat_member(
                m.chat.id,
                id,
                privileges=ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_promote_members=can_promote_members,
                    can_change_info=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                ),
            )
            if title:
                try:
                    await c.set_administrator_title(m.chat.id, id, title)
                except Exception:
                    pass
            get = await m.chat.get_member(id)
            if type == 1:
                await r.set(f"{m.chat.id}:rankADMIN:{get.user.id}{Dev_Zaid}", 1)
                await r.sadd(f"{m.chat.id}:listADMIN:{Dev_Zaid}", get.user.id)
                return await m.reply(
                    t('g_9a8df2f799', 'الحلو 「 {0} 」\n{1} رفعته مشرف بكل صلاحيات ', get.user.mention, k)
                )
            else:
                await r.set(f"{m.chat.id}:rankADMIN:{get.user.id}{Dev_Zaid}", 1)
                await r.sadd(f"{m.chat.id}:listADMIN:{Dev_Zaid}", get.user.id)
                return await m.reply(
                    t('g_efc89c4e7a', 'الحلو 「 {0} 」\n{1} رفعته مشرف بكل الصلاحيات عدا رفع المشرفين', get.user.mention, k)
                )

    if text == "مسح قائمة التثبيت":
        if not await mod_pls(m.from_user.id, m.chat.id):
            return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
        else:
            c.unpin_all_chat_messages(m.chat.id)
            return await m.reply(t('g_eff65d2a1a', '{0} ابشر مسحت قائمة التثبيت', k))

    if (
        text == "الاوامر"
        or text.lower() == "/commands"
        or text.lower() == f"/commands@{botUsername.lower()}"
    ):
        if await admin_pls(m.from_user.id, m.chat.id):
            channel = (
                await r.get(f"{Dev_Zaid}:BotChannel") or "YQYQY6"
            )
            return await m.reply(
                t('g_a0b94a33e5', '{0} اهلين فيك باوامر البوت\n\nللاستفسار - @{1}', k, channel),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "م1", callback_data=f"commands1:{m.from_user.id}"
                            ),
                            InlineKeyboardButton(
                                "م2", callback_data=f"commands2:{m.from_user.id}"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "م3", callback_data=f"commands3:{m.from_user.id}"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                            ),
                            InlineKeyboardButton(
                                "التسليه", callback_data=f"commands5:{m.from_user.id}"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "البنك", callback_data=f"commands7:{m.from_user.id}"
                            ),
                            InlineKeyboardButton(
                                "زواج", callback_data=f"commands8:{m.from_user.id}"
                            ),
                        ],
                    ]
                ),
            )
        else:
            return await m.reply(t('g_85ab7798c1', '{0} هذا الأمر يخص ( الادمن وفوق ) بس', k))


@Client.on_callback_query(group=1)
async def CallbackQueryHandler(c, m):
    channel = (
        await r.get(f"{Dev_Zaid}:BotChannel") or "YQYQY6"
    )
    await CallbackQueryResponse(c, m, channel)


async def CallbackQueryResponse(c, m, channel):
    k = await r.get(f"{Dev_Zaid}:botkey")
    if m.data == f"commands1:{m.from_user.id}":
        await m.edit_message_text(
            t('g_dbab7277bc', '\nللاستفسار - @{0}\n\n\n❨ اوامر الرفع والتنزيل ❩\n\n⌯ رفع ↣ ↢ تنزيل مشرف\n⌯ رفع ↣ ↢ تنزيل مالك اساسي\n⌯ رفع ↣ ↢ تنزيل مالك\n⌯ رفع ↣ ↢ تنزيل مدير\n⌯ رفع ↣ ↢ تنزيل ادمن\n⌯ رفع ↣ ↢ تنزيل مميز\n⌯ تنزيل الكل  ↢ بالرد  ↢ لتنزيل الشخص من جميع رتبه\n⌯ مسح الكل  ↢ بدون رد  ↢ لتنزيل كل رتب المجموعة\n\n❨ اوامر المسح ❩\n\n⌯ مسح المالكيين\n⌯ مسح المدراء\n⌯ مسح الادمنيه\n⌯ مسح المميزين\n⌯ مسح المحظورين\n⌯ مسح المكتومين\n⌯ مسح قائمة المنع\n⌯ مسح رتبه\n⌯ مسح الرتب\n⌯ مسح الردود\n⌯ مسح الاوامر\n⌯ مسح + العدد\n⌯ مسح بالرد\n⌯ مسح الترحيب\n⌯ مسح قائمة التثبيت\n\n❨ اوامر الطرد الحظر الكتم ❩\n\n⌯ حظر ↢ ❨ بالرد،بالمعرف،بالايدي ❩\n⌯ طرد ↢ ❨ بالرد،بالمعرف،بالايدي ❩\n⌯ كتم ↢ ❨ بالرد،بالمعرف،بالايدي ❩\n⌯ تقيد ↢ ❨ بالرد،بالمعرف،بالايدي ❩\n⌯ الغاء الحظر ↢ ❨ بالرد،بالمعرف،بالايدي ❩\n⌯ الغاء الكتم ↢ ❨ بالرد،بالمعرف،بالايدي ❩\n⌯ الغاء التقييد ↢ ❨ بالرد،بالمعرف،بالايدي ❩\n⌯ رفع القيود ↢ لحذف الكتم,الحظر,التقييد\n⌯ منع الكلمة\n⌯ منع بالرد على قيف او ستيكر\n⌯ الغاء منع الكلمة\n⌯ طرد البوتات\n⌯ كشف البوتات\n\n❨ اوامر النطق ❩\n\n⌯ انطقي + الكلمة\n⌯ وش يقول؟ + بالرد على فويس لترجمه المحتوى\n\n❨ اوامر اخرى ❩\n\n⌯ الرابط\n⌯ معلومات الرابط\n⌯ انشاء رابط\n⌯ بايو\n⌯ بايو عشوائي\n⌯ ايدي\n⌯ الانشاء\n⌯ مجموعاتي\n⌯ ابلاغ\n⌯ نقل ملكية\n⌯ صوره\n⌯ افتاري\n⌯ افتار + باليوزر او الرد\n⌯ مين ضافني؟\n⌯ شازام، قرآن، سورة + اسم السورة\n', channel),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("م1 ‣", callback_data="None"),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands2:{m.from_user.id}":
        await m.edit_message_text(
            t('g_ae4e29cc78', '\nللاستفسار - @{0}\n\n\n❨ اوامر الوضع ❩\n\n⌯ وضع ترحيب\n⌯ وضع قوانين\n⌯ تغيير رتبه\n⌯ تغيير امر\n\n❨ اوامر رؤية الاعدادات ❩\n\n⌯ المطورين\n⌯ المالكيين الاساسيين\n⌯ المالكيين\n⌯ الادمنيه\n⌯ المدراء\n⌯ المشرفين\n⌯ المميزين\n⌯ القوانين\n⌯ قائمه المنع\n⌯ المكتومين\n⌯ المطور\n⌯ معلوماتي\n⌯ الاعدادت\n⌯ المجموعه\n⌯ الساعه\n⌯ التاريخ\n⌯ صلاحياتي\n⌯ لقبي\n⌯ صلاحياته + بالرد\n', channel),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("م2 ‣", callback_data="None"),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands3:{m.from_user.id}":
        await m.edit_message_text(
            t('g_780e2b3209', '\nللاستفسار - @{0}\n\n\n❨ اوامر الردود ❩\n\n⌯ الردود ↢ تشوف كل الردود المضافه\n⌯ الردود المتعدده ↢ تشوف كل الردود المتعدده المضافه\n⌯ اضف رد ↢ عشان تضيف رد\n⌯ اضف رد متعدد ↢ عشان تضيف أكثر من رد\n⌯ اضف رد متعدد ↢ خاص بالاعضاء\n⌯ مسح رد ↢ عشان تمسح الرد\n⌯ مسح رد متعدد ↢ عشان تمسح رد متعدد\n⌯ مسح ردي ↢ عشان تمسح ردك اذا كان بردود الأعضاء\n⌯ مسح الردود ↢ تمسح كل الردود\n⌯ مسح الردود المتعدده ↢ عشان تمسح كل الردود المتعدده\n⌯ الرد + كلمة الرد\n-\n\n❨ اوامر القفل والفتح بالمسح ❩\n\n⌯ قفل ↣ ↢ فتح  التعديل\n⌯ قفل ↣ ↢ فتح  الفويسات\n⌯ قفل ↣ ↢ فتح  الفيديو\n⌯ قفل ↣ ↢ فتح  الـصــور\n⌯ قفل ↣ ↢ فتح  الملصقات\n⌯ قفل ↣ ↢ فتح  الدخول\n⌯ قفل ↣ ↢ فتح  الفارسية\n⌯ قفل ↣ ↢ فتح  الملفات\n⌯ قفل ↣ ↢ فتح  المتحركات\n⌯ قفل ↣ ↢ فتح  تعديل الميديا\n⌯ قفل ↣ ↢ فتح  تعديل الميديا بالتقييد\n⌯ قفل ↣ ↢ فتح  الدردشه\n⌯ قفل ↣ ↢ فتح  الروابط\n⌯ قفل ↣ ↢ فتح  الهشتاق\n⌯ قفل ↣ ↢ فتح  البوتات\n⌯ قفل ↣ ↢ فتح  اليوزرات\n⌯ قفل ↣ ↢ فتح  الاشعارات\n⌯ قفل ↣ ↢ فتح  الكلام الكثير\n⌯ قفل ↣ ↢ فتح  التكرار\n⌯ قفل ↣ ↢ فتح  التوجيه\n⌯ قفل ↣ ↢ فتح  الانلاين\n⌯ قفل ↣ ↢ فتح  الجهات\n⌯ قفل ↣ ↢ فتح  الــكـــل\n⌯ قفل ↣ ↢ فتح  السب\n⌯ قفل ↣ ↢ فتح  الاضافه\n⌯ قفل ↣ ↢ فتح  الصوت\n⌯ قفل ↣ ↢ فتح  القنوات\n⌯ قفل ↣ ↢ فتح الايراني\n⌯ قفل ↣ ↢ فتح الإباحي\n\n❨ اوامر التفعيل والتعطيل ❩\n\n⌯ تفعيل ↣ ↢ تعطيل الترحيب\n⌯ تفعيل ↣ ↢ تعطيل الترحيب بالصورة\n⌯ تفعيل ↣ ↢ تعطيل الردود\n⌯ تفعيل ↣ ↢ تعطيل ردود الاعضاء\n⌯ تفعيل ↣ ↢ تعطيل الايدي\n⌯ تفعيل ↣ ↢ تعطيل الرابط\n⌯ تفعيل ↣ ↢ تعطيل اطردني\n⌯ تفعيل ↣ ↢ تعطيل الحماية\n⌯ تفعيل ↣ ↢ تعطيل المنشن\n⌯ تفعيل ↣ ↢ تعطيل التحقق\n⌯ تفعيل ↣ ↢ تعطيل ردود المطور\n⌯ تفعيل ↣ ↢ تعطيل التحذير\n⌯ تفعيل ↣ ↢ تعطيل البايو\n⌯ تفعيل ↣ ↢ تعطيل انطقي\n⌯ تفعيل ↣ ↢ تعطيل شازام\n', channel),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton("م3 ‣", callback_data="None"),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands4:{m.from_user.id}":
        await m.edit_message_text(
            t('g_b369261128', """
☤ تفعيل الالعاب
☤ تعطيل الالعاب
    ╼╾
✽ جمل
✽ كلمات
✽ اغاني
✽ دين
✽ عربي
✽ اكمل
✽ صور
✽ كت تويت
✽ مؤقت
✽ اعلام
✽ معاني
✽ تخمين
✽ احكام
✽ ارقام
✽ احسب
✽ خواتم
✽ انقليزي
✽ ترتيب
✽ انمي
✽ تركيب
✽ تفكيك
✽ عواصم
✽ روليت
✽ سيارات
✽ ايموجي
✽ حجره
✽ تشفير
✽ كره قدم
✽ ديمون
╼╾
❖ فلوسي ↼ عشان تشوف فلوسك
❖ بيع فلوسي + العدد ↼ للأستبدال
"""),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton("الالعاب ‣", callback_data="None"),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands5:{m.from_user.id}":
        await m.edit_message_text(
            t('g_bfce082dfd', '\nللاستفسار - @{0}\n\n🍰 ⌯ رفع ↣ ↢ تنزيل كيكه\n🍯 ⌯ رفع ↣ ↢ تنزيل عسل\n💩 ⌯ رفع ↣ ↢ تنزيل زق\n🦓 ⌯ رفع ↣ ↢ تنزيل حمار\n🐄 ⌯ رفع ↣ ↢ تنزيل بقره\n🐩 ⌯ رفع ↣ ↢ تنزيل كلب\n🐒 ⌯ رفع ↣ ↢ تنزيل قرد\n🐐 ⌯ رفع ↣ ↢ تنزيل تيس\n🐂 ⌯ رفع ↣ ↢ تنزيل ثور\n🏅 ⌯ رفع ↣ ↢ تنزيل هكر\n🐓 ⌯ رفع ↣ ↢ تنزيل دجاجه\n🧱 ⌯ رفع ↣ ↢ تنزيل ملكه\n🔫 ⌯ رفع ↣ ↢ تنزيل صياد\n🐏 ⌯ رفع ↣ ↢ تنزيل خاروف\n❤️ ⌯ رفع لقلبي ↣ ↢ تنزيل من قلبي\n\n⌯ قائمة الكيك\n⌯ قائمة العسل\n⌯ قائمة الزق\n⌯ قائمة الحمير\n⌯ قائمة البقر\n⌯ قائمة الكلاب\n⌯ قائمة القرود\n⌯ قائمة التيس\n⌯ قائمة الثور\n⌯ قائمة الهكر\n⌯ قائمة الدجاج\n⌯ قائمة الهطوف\n⌯ قائمة الصيادين\n⌯ قائمة الخرفان\n', channel),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("التسليه ‣", callback_data="None"),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands6:{m.from_user.id}":
        await m.edit_message_text(
            t('g_b54770848c', """
⚘ اليـوتيوب

تفعيل اليوتيوب
تعطيل اليوتيوب

❋ البـحث عن اغنية ↓

بحث اسم الاغنية

يوت اسم الاغنية
⚘ الساوند كلاود

تفعيل الساوند
تعطيل الساوند

❋ البـحث عن اغنية ↓

رابط الاغنية أو ساوند + اسم الاغنية


⚘ التيك توك

تفعيل التيك
تعطيل للتيك

❋ للتحميل من التيك ↓

تيك ورابط المقطع
"""),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton("اليوتيوب ‣", callback_data="None"),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands7:{m.from_user.id}":
        await m.edit_message_text(
            t('g_f34fa97cc1', """
✜ اوامر البنك

⌯ انشاء حساب بنكي  ↢ تسوي حساب وتقدر تحول فلوس مع مزايا ثانيه

⌯ مسح حساب بنكي  ↢ تلغي حسابك البنكي

⌯ تحويل ↢ تطلب رقم حساب الشخص وتحول له فلوس

⌯ حسابي  ↢ يطلع لك رقم حسابك عشان تعطيه للشخص اللي بيحول لك

⌯ فلوسي ↢ يعلمك كم فلوسك

⌯ راتب ↢ يعطيك راتبك كل ٥ دقيقة

⌯ بخشيش ↢ يعطيك بخشيش كل ٥ دقايق

⌯ زرف ↢ تزرف فلوس اشخاص كل ٥ دقايق

⌯ كنز ↢ يعطيك كنز كل ١٠ دقايق

⌯ استثمار ↢ تستثمر بالمبلغ اللي تبيه مع نسبة ربح مضمونه من ١٪؜ الى ١٥٪؜ ( او استثمار فلوسي )

⌯ حظ ↢ تلعبها بأي مبلغ ياتدبله ياتخسره انت وحظك ( او حظ فلوسي )

⌯ عجله ↢ تلعب عجله الحظ ولو تشابهو ال ٣ ايموجيات تكسب من ١٠٠ الف لحد ٣٠٠ الف انت وحظك

⌯ توب الفلوس ↢ يطلع توب اكثر ناس معهم فلوس بكل القروبات

⌯ توب الحراميه ↢ يطلع لك اكثر ناس زرفوا
"""),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton("البنك ‣", callback_data="None"),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands8:{m.from_user.id}":
        await m.edit_message_text(
            t('g_81dd786ceb', """
✜ اوامر الزواج

⌯ زواج  ↢ تكتبه بالرد على رسالة شخص مع المهر ويزوجك

⌯ زواجي  ↢ يطلع وثيقة زواجك اذا متزوج

⌯ طلاق ↢ يطلقك اذا متزوج

⌯ خلع  ↢ يخلع زوجك ويرجع له المهر

⌯ زواجات ↢ يطلع اغلى الزواجات بالقروب
"""),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("زواج ‣", callback_data="None"),
                    ],
                ]
            ),
        )
        return

    if m.data == "delAdminMSG":
        if str(m.from_user.id) in m.message.text.html:
            return await m.message.delete()

    if m.data == f"yes:{m.from_user.id}":
        try:
            await c.restrict_chat_member(
                m.message.chat.id,
                m.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_send_polls=True,
                    can_invite_users=True,
                    can_add_web_page_previews=True,
                    can_change_info=True,
                    can_pin_messages=True,
                ),
            )
        except Exception:
            return False
        await m.edit_message_text(
            t('g_0cb015a1b7', '\n{0} تم التحقق منك وطلعت مو زومبي\n{1} الحين تقدر تسولف بالقروب\n☆\n', k, k),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            ),
        )

    if m.data == f"no:{m.from_user.id}":
        return await m.edit_message_text(
            t('g_0a7e9d5296', '\n{0} للأسف طلعت زومبي 🧟\u200d♀️\n{1} مالك غير تنطر حد من المشرفين يجي يتوسطلك\n☆\n', k, k),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "رفع التقييد والسماح",
                            callback_data=f"yesVER:{m.from_user.id}",
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "طرد", callback_data=f"noVER:{m.from_user.id}"
                        )
                    ],
                ]
            ),
        )

    if m.data.startswith("yesVER"):
        user_id = int(m.data.split(":")[1])
        if not await admin_pls(m.from_user.id, m.message.chat.id):
            return await m.answer(f"{k} هذا الزر يخص ( الادمن وفوق ) بس", show_alert=True)
        else:
            await m.edit_message_text(t('g_0b362170ec', '{0} توسطلك واحد من الادمن ورفعت عنك القيود', k))
            try:
                await c.restrict_chat_member(
                    m.message.chat.id,
                    user_id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_other_messages=True,
                        can_send_polls=True,
                        can_invite_users=True,
                        can_add_web_page_previews=True,
                        can_change_info=True,
                        can_pin_messages=True,
                    ),
                )
            except Exception:
                return False

    if m.data.startswith("noVER"):
        user_id = int(m.data.split(":")[1])
        if not await admin_pls(m.from_user.id, m.message.chat.id):
            return await m.answer(f"{k} هذا الزر يخص ( الادمن وفوق ) بس", show_alert=True)
        else:
            await m.edit_message_text(t('g_fbdf8f361c', '{0} انقلع برا القروب يلا', k))
            try:
                await m.message.chat.ban_member(user_id)
                await m.message.chat.unban_member(user_id)
            except Exception:
                pass

    if m.data == "yes:del:bank":
        if not await devp_pls(m.from_user.id, m.message.chat.id):
            return await m.answer("تعجبني ثقتك")
        else:
            await m.edit_message_text(t('g_0c8ac45b26', "ابشر صفرت البنك"))
            keys = await r.keys("*:Floos")
            for a in keys:
                await r.delete(a)
            for a in await r.keys("*:BankWait"):
                await r.delete(a)
            for a in await r.keys("*:BankWaitB5"):
                await r.delete(a)
            for a in await r.keys("*:BankWaitZRF"):
                await r.delete(a)
            for a in await r.keys("*:BankWaitEST"):
                await r.delete(a)
            for a in await r.keys("*:BankWaitHZ"):
                await r.delete(a)
            for a in await r.keys("*:BankWait3JL"):
                await r.delete(a)
            for a in await r.keys("*:Zrf"):
                await r.delete(a)
            await r.delete("BankTop")
            await r.delete("BankTopZRF")
            return True

    if m.data == "no:del:bank":
        if not await devp_pls(m.from_user.id, m.message.chat.id):
            return await m.answer("تعجبني ثقتك")
        else:
            await m.message.delete()

    if m.data == f"topfloos:{m.from_user.id}":
        if not await r.smembers("BankList"):
            return await m.answer(f"{k} مافيه حسابات بالبنك", show_alert=True)
        else:
            rep = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("‣ 💸", callback_data="None"),
                        InlineKeyboardButton(
                            "توب الحرامية 💰", callback_data=f"topzrf:{m.from_user.id}"
                        ),
                    ],
                    [InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")],
                ]
            )
            if await r.get("BankTop"):
                text = await r.get("BankTop")
                if not await r.get(f"{m.from_user.id}:Floos"):
                    floos = 0
                else:
                    floos = int(await r.get(f"{m.from_user.id}:Floos"))
                get = await r.ttl("BankTop")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {floos:,} 💸 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                return await m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )
            else:
                users = []
                ccc = 0
                for user in await r.smembers("BankList"):
                    ccc += 1
                    id = int(user)
                    if await r.get(f"{id}:bankName"):
                        name = (await r.get(f"{id}:bankName"))[:10]
                    else:
                        try:
                            name = await c.get_chat(id).first_name
                            await r.set(f"{id}:bankName", name)
                        except Exception:
                            name = "INVALID_NAME"
                            await r.set(f"{id}:bankName", name)
                    if not await r.get(f"{id}:Floos"):
                        floos = 0
                    else:
                        floos = int(await r.get(f"{id}:Floos"))
                    users.append({"name": name, "money": floos})
                top = get_top(users)
                text = "توب 20 اغنى اشخاص:\n\n"
                count = 0
                for user in top:
                    count += 1
                    if count == 21:
                        break
                    emoji = get_emoji_bank(count)
                    floos = user["money"]
                    name = user["name"]
                    text += f'**{emoji}{floos:,}** 💸 l {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
                await r.set("BankTop", text, ex=300)
                if not await r.get(f"{m.from_user.id}:Floos"):
                    floos_from_user = 0
                else:
                    floos_from_user = int(await r.get(f"{m.from_user.id}:Floos"))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {floos_from_user:,} 💸 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                get = await r.ttl("BankTop")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                await m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )

    if m.data == f"topzrf:{m.from_user.id}":
        if not await r.smembers("BankList"):
            return await m.answer(f"{k} مافيه حسابات بالبنك", show_alert=True)
        else:
            rep = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "توب الفلوس 💸", callback_data=f"topfloos:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("‣ 💰", callback_data="None"),
                    ],
                    [InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")],
                ]
            )
            if await r.get("BankTopZRF"):
                text = await r.get("BankTopZRF")
                if not await r.get(f"{m.from_user.id}:Zrf"):
                    zrf = 0
                else:
                    zrf = int(await r.get(f"{m.from_user.id}:Zrf"))
                get = await r.ttl("BankTopZRF")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {zrf:,} 💰 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                return await m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )
            else:
                users = []
                ccc = 0
                for user in await r.smembers("BankList"):
                    ccc += 1
                    id = int(user)
                    if await r.get(f"{id}:bankName"):
                        name = (await r.get(f"{id}:bankName"))[:10]
                    else:
                        try:
                            name = await c.get_chat(id).first_name
                            await r.set(f"{id}:bankName", name)
                        except Exception:
                            name = "INVALID_NAME"
                            await r.set(f"{id}:bankName", name)
                    if not await r.get(f"{id}:Zrf"):
                        pass
                    else:
                        zrf = int(await r.get(f"{id}:Zrf"))
                        users.append({"name": name, "money": zrf})
                top = get_top(users)
                text = "توب 20 اكثر الحراميه زرفًا:\n\n"
                count = 0
                for user in top:
                    count += 1
                    if count == 21:
                        break
                    emoji = get_emoji_bank(count)
                    floos = user["money"]
                    name = user["name"]
                    text += f'**{emoji}{floos}** 💰 l {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
                await r.set("BankTopZRF", text, ex=300)
                if not await r.get(f"{m.from_user.id}:Zrf"):
                    floos_from_user = 0
                else:
                    floos_from_user = int(await r.get(f"{m.from_user.id}:Zrf"))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {floos_from_user} 💰 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                get = await r.ttl("BankTopZRF")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                await m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )

    """
   if m.data == f'toplast:{m.from_user.id}':
     if not await r.get(f'BankTopLast') and not await r.get(f'BankTopLastZrf'):
       return await m.answer(f'{k} مافي توب اسبوع الي فات',show_alert=True)
     else:
       text = 'توب أوائل الأسبوع الي راح:\n'
       text += await r.get(f'BankTopLast')
       text += '\n\nتوب حرامية الاسبوع اللي راح:\n'
       text += await r.get(f'BankTopLastZrf')
       text += '\n༄'
       rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
       )
       await m.edit_message_text(text, disable_web_page_preview=True,reply_markup=rep)
   """

    name = await r.get(f"{Dev_Zaid}:BotName") or "رعد"
    if m.data == f"RPS:rock++{m.from_user.id}":
        RPS = ["paper", "scissors", "rock"]
        kk = random.choice(RPS)
        if kk == "scissors":
            if await r.get(f"{m.from_user.id}:Floos"):
                get = int(await r.get(f"{m.from_user.id}:Floos"))
                await r.set(f"{m.from_user.id}:Floos", get + 1)
            else:
                await r.set(f"{m.from_user.id}:Floos", 1)
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            await m.edit_message_text(
                t('g_6b5cb31b3a', '\nأنت: 🪨\nأنا: ✂️\n\nالنتيجة: \u206a\u206c\u206a\u206c 🏆 {0}\n', m.from_user.first_name),
                disable_web_page_preview=True,
                reply_markup=rep,
            )

        if kk == "paper":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            await m.edit_message_text(
                t('g_d2f5a4d40b', '\nأنت: 🪨\nأنا: 📃\n\nالنتيجة: \u206a\u206c\u206a\u206c 🏆️ {0}\n', name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")),
                disable_web_page_preview=True,
                reply_markup=rep,
            )
        if kk == "rock":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            await m.edit_message_text(
                t('g_ceef74ce7d', '\nأنت: 🪨\nأنا: 🪨\n\nالنتيجة: \u206a\u206c\u206a\u206c ⚖️ {0}\n', name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")),
                disable_web_page_preview=True,
                reply_markup=rep,
            )

    if m.data == f"gowner+{m.from_user.id}":
        if not await gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return await m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            await r.hset(Dev_Zaid + f"locks-{m.message.chat.id}", command, 0)
            return await m.edit_message_text(
                t('g_61c01c218d', '- تم تعيين الامر ( {0} ) للمالك الاساسي وفوق فقط', command)
            )

    if m.data == f"owner+{m.from_user.id}":
        if not await gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return await m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            await r.hset(Dev_Zaid + f"locks-{m.message.chat.id}", command, 1)
            return await m.edit_message_text(
                t('g_209a8c0077', '- تم تعيين الامر ( {0} ) للمالك وفوق فقط', command)
            )

    if m.data == f"mod+{m.from_user.id}":
        if not await gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return await m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            await r.hset(Dev_Zaid + f"locks-{m.message.chat.id}", command, 2)
            return await m.edit_message_text(
                t('g_31fca58e71', '- تم تعيين الامر ( {0} ) للمدير وفوق فقط', command)
            )

    if m.data == f"admin+{m.from_user.id}":
        if not await gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return await m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            await r.hset(Dev_Zaid + f"locks-{m.message.chat.id}", command, 3)
            return await m.edit_message_text(
                t('g_870a06a7cd', '- تم تعيين الامر ( {0} ) للادمن وفوق فقط', command)
            )

    if m.data == f"pre+{m.from_user.id}":
        if not await gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return await m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            await r.hset(Dev_Zaid + f"locks-{m.message.chat.id}", command, 4)
            return await m.edit_message_text(
                t('g_4e1eee642a', '- تم تعيين الامر ( {0} ) للمميز وفوق فقط', command)
            )

    if m.data == f"RPS:paper++{m.from_user.id}":
        RPS = ["paper", "scissors", "rock"]
        kk = random.choice(RPS)
        if kk == "rock":
            if await r.get(f"{m.from_user.id}:Floos"):
                get = int(await r.get(f"{m.from_user.id}:Floos"))
                await r.set(f"{m.from_user.id}:Floos", get + 1)
            else:
                await r.set(f"{m.from_user.id}:Floos", 1)
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            await m.edit_message_text(
                t('g_25d8ea1a07', '\nأنت: 📃\nأنا: 🪨\n\nالنتيجة: \u206a\u206c\u206a\u206c 🏆 {0}\n', m.from_user.first_name),
                disable_web_page_preview=True,
                reply_markup=rep,
            )

        if kk == "scissors":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            await m.edit_message_text(
                t('g_31a2f92f1e', '\nأنت: 📃\nأنا: ✂️\n\nالنتيجة: \u206a\u206c\u206a\u206c 🏆️ {0}\n', name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")),
                disable_web_page_preview=True,
                reply_markup=rep,
            )
        if kk == "paper":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            await m.edit_message_text(
                t('g_1818b08dd2', '\nأنت: 📃\nأنا: 📃\n\nالنتيجة: \u206a\u206c\u206a\u206c ⚖️ {0}\n', name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")),
                disable_web_page_preview=True,
                reply_markup=rep,
            )

    if m.data == f"RPS:scissors++{m.from_user.id}":
        RPS = ["paper", "scissors", "rock"]
        kk = random.choice(RPS)
        if kk == "paper":
            if await r.get(f"{m.from_user.id}:Floos"):
                get = int(await r.get(f"{m.from_user.id}:Floos"))
                await r.set(f"{m.from_user.id}:Floos", get + 1)
            else:
                await r.set(f"{m.from_user.id}:Floos", 1)
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            await m.edit_message_text(
                t('g_8361f259cf', '\nأنت: ✂️\nأنا: 📃\n\nالنتيجة: \u206a\u206c\u206a\u206c 🏆 {0}\n', m.from_user.first_name),
                disable_web_page_preview=True,
                reply_markup=rep,
            )

        if kk == "rock":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            await m.edit_message_text(
                t('g_b6d790d217', '\nأنت: ✂️\nأنا: 🪨\n\nالنتيجة: \u206a\u206c\u206a\u206c 🏆️ {0}\n', name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")),
                disable_web_page_preview=True,
                reply_markup=rep,
            )
        if kk == "scissors":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            await m.edit_message_text(
                t('g_bf0cc72179', '\nأنت: ✂️\nأنا: ✂️\n\nالنتيجة: \u206a\u206c\u206a\u206c ⚖️ {0}\n', name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")),
                disable_web_page_preview=True,
                reply_markup=rep,
            )
