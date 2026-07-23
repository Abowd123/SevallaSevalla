import logging
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

=====================================================================
[ async ] هذا الملف محوَّل بالكامل إلى النمط غير المتزامن
نموذج مرجعي: عميل Redis غير متزامن + await على كل دوال Pyrogram
بدون Threads. الدوال المساعدة (admin_pls...) تبقى متزامنة كما هي.
=====================================================================

'''

import random, re, time, os, sys, pytz, string
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from datetime import datetime
from config import *
from helpers.replies import t
from helpers.Ranks import *
from helpers.Ranks import isLockCommand



def get_sarhni_id():
    rndm = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
    return rndm


@Client.on_message(filters.text & filters.group, group=37)
async def sarhniHandler(c, m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
        return
    if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):
        return
    if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):
        return
    if await r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):
        return
    if await r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or await r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):
        return
    if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id, m.chat.id):
        return
    if await r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):
        return

    text = m.text
    name = await r.get(f'{Dev_Zaid}:BotName') or 'رعد'
    if text.startswith(f'{name} '):
        text = text.replace(f'{name} ', '')

    custom = await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
    if custom:
        text = custom
    custom_g = await r.get(f'Custom:{Dev_Zaid}&text={text}')
    if custom_g:
        text = custom_g

    if text == 'صارحني':
        if not await r.get(f'{m.from_user.id}:sar7ni:{Dev_Zaid}'):
            id = get_sarhni_id()
            await r.set(f'{m.from_user.id}:sar7ni:{Dev_Zaid}', id)
            await r.set(f'{id}:sarhni:{Dev_Zaid}', m.from_user.id)
        else:
            id = await r.get(f'{m.from_user.id}:sar7ni:{Dev_Zaid}')
        await r.set(f'{m.from_user.id}:sarhniname', m.from_user.first_name)
        return await m.reply(
            t('g_38220f7a88', '{0} أهلين عيني「 \u206a\u206c\u206a\u206c{1} 」\n{2} هذا رابط صارحني الخاص فيك', k, m.from_user.mention, k),
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('📩', url=f't.me/{botUsername}?start=sarhni{id}')]]),
        )


@Client.on_message(filters.private, group=2)
async def sarhniHandlerP(c, m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    channel = await r.get(f'{Dev_Zaid}:BotChannel') or 'yqyqy66'
    if not m.text:
        return
    text = m.text

    if text.startswith('/start sarhni'):
        id = text.split('sarhni')[1]
        if not await r.get(f'{id}:sarhni:{Dev_Zaid}'):
            return await m.reply(t('g_34481a1b02', '{0} رابط صارحني غلط', k))
        else:
            user_id = int(await r.get(f'{id}:sarhni:{Dev_Zaid}'))
            if m.from_user.id == user_id:
                return await m.reply(t('g_f5b7a87d20', 'انت هطف تدخل رابط صراحة حقك؟'))
            get = await c.get_chat(user_id)
            await r.set(f'{m.from_user.id}:sarhni', get.id, ex=300)
            a = await m.reply(
                t('g_9a1b5f3c4d', '{0} دخلت الحين رابط صارحني مع 「 \u206a\u206c\u206a\u206c{1} 」\n{2} اي رسالة ترسلها لي راح احولها له بسرية تامة بدون مايعرفك\n༄', k, get.first_name, k),
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('الغاء', callback_data='sarhni:bye')], [InlineKeyboardButton('🧚‍♀️', url=f't.me/{channel}')]]),
                quote=True,
            )
            return await a.pin(both_sides=True)

    if await r.get(f'{m.from_user.id}:sarhni') and len(text) < 1000:
        user_id = int(await r.get(f'{m.from_user.id}:sarhni'))
        name = await r.get(f'{user_id}:sarhniname')
        TIME_ZONE = "Asia/Riyadh"
        ZONE = pytz.timezone(TIME_ZONE)
        TIME = datetime.now(ZONE)
        clock = TIME.strftime("%I:%M %p")
        date = TIME.strftime("%d/%m/%Y")
        txt = f'{k} وصلتك رسالة مصارحة جديدة\n{k} التاريخ : {date}\n{k} الساعة : {clock}\n\n{k} الرسالة :\n\n{text}\n☆'
        try:
            await c.send_message(
                user_id, txt, disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton('رد', callback_data=f'sarhni+rep{m.from_user.id}')],
                    [InlineKeyboardButton('🧚‍♀️', url=f't.me/{channel}')],
                ]),
            )
            return await m.reply(t('g_ace5a9c555', '{0} ابشر ارسلت رسالتك بسرية تامة لـ {1}', k, name), quote=True)
        except Exception as e:
            logging.exception(e)
            return await m.reply(t('g_9339bec150', 'مقدر ارسله شيء يمكن حاظرني'), quote=True)

    if await r.get(f'{m.from_user.id}:sarhni'):
        user_id = int(await r.get(f'{m.from_user.id}:sarhni'))
        name = await r.get(f'{user_id}:sarhniname')
        TIME_ZONE = "Asia/Riyadh"
        ZONE = pytz.timezone(TIME_ZONE)
        TIME = datetime.now(ZONE)
        clock = TIME.strftime("%I:%M %p")
        date = TIME.strftime("%d/%m/%Y")
        txt = f'{k} وصلتك رسالة مصارحة جديدة\n{k} التاريخ : {date}\n{k} الساعة : {clock}\n\n{k} الرسالة :'
        try:
            await c.send_message(user_id, txt, disable_web_page_preview=True)
            await m.copy(
                user_id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton('رد', callback_data=f'sarhni+rep{m.from_user.id}')],
                    [InlineKeyboardButton('🧚‍♀️', url=f't.me/{channel}')],
                ]),
            )
            return await m.reply(t('g_ace5a9c555', '{0} ابشر ارسلت رسالتك بسرية تامة لـ {1}', k, name), quote=True)
        except Exception as e:
            logging.exception(e)
            return await m.reply(t('g_9339bec150', 'مقدر ارسله شيء يمكن حاظرني'), quote=True)

    if await r.get(f'{m.from_user.id}:sarhnirep'):
        user_id = int(await r.get(f'{m.from_user.id}:sarhnirep'))
        await r.delete(f'{m.from_user.id}:sarhnirep')
        await m.reply(t('g_cb9a29fe20', '{0} ابشر ارسلت له ردك', k), quote=True)
        return await m.copy(user_id)


@Client.on_callback_query(filters.regex('sarhni'))
async def sarhni_callback(c, m):
    if m.data == 'sarhni:bye':
        await r.delete(f'{m.from_user.id}:sarhni')
        await m.message.delete()
        return await m.answer('ابشر طلعتك من كل جلسة صارحني', show_alert=True)

    if m.data.startswith('sarhni+rep'):
        user_id = int(m.data.split('rep')[1])
        if not await r.get(f'{user_id}:sarhni'):
            return await m.answer('مايمدي ترد عليه لأنه طلع من جلسة صارحني', show_alert=True)
        if not int(await r.get(f'{user_id}:sarhni')) == m.from_user.id:
            return await m.answer('مايمدي ترد عليه لأنه طلع من جلسة صارحني', show_alert=True)
        else:
            await r.set(f'{m.from_user.id}:sarhnirep', user_id, ex=300)
            return await c.send_message(m.from_user.id, 'ارسل الرد الحين')
