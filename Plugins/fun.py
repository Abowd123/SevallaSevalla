'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''

import random, re, time
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.replies import t
from helpers.Ranks import *
from helpers.Ranks import isLockCommand
import asyncio


@Client.on_message(filters.text & filters.group, group=34)
async def funHandler(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    channel = await r.get(f'{Dev_Zaid}:BotChannel') or 'yqyqy66'
    await funFunc(c,m,k,channel)
    
async def funFunc(c,m,k,channel):
   if await r.get(f'{m.chat.id}:disableFun:{Dev_Zaid}'):  return 
   if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return
   if await r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or await r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return  
   if await r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = await r.get(f'{Dev_Zaid}:BotName') or 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if await r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = await r.get(f'Custom:{Dev_Zaid}&text={text}')
   if await isLockCommand(m.from_user.id, m.chat.id, text): return
   ################# CAKE #################
   if text == 'رفع كيك' or text == 'رفع كيكه' or text == 'رفع كيكة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:CakeList:{m.chat.id}',id):
         return await m.reply(t('g_4cfa2a67ec', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} كيكه من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:CakeList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:CakeName:{id}', mention)
         return await m.reply(t('g_b05d35ffa1', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته كيكه 🍰\n☆', mention, k))
   
   if text == 'تنزيل كيك' or text == 'تنزيل كيكه' or text == 'تنزيل كيكة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:CakeList:{m.chat.id}',id):
         return await m.reply(t('g_3f19e77c11', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو كيكه من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:CakeList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:CakeName:{id}')
         return await m.reply(t('g_87dba2c7f2', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من كيكه\n☆', mention, k))
   
   if text == 'قائمه الكيك' or text == 'قائمة الكيك':
     if not await r.smembers(f'{Dev_Zaid}:CakeList:{m.chat.id}'):
       return await m.reply(t('g_3a6b4a2c8f', '{0} قائمة الكيك فاضية', k))
     else:
       txt = '- قائمة الكيك 🍰\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:CakeList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:CakeName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الكيك' or text == 'مسح قائمه الكيك':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:CakeList:{m.chat.id}'):
         return await m.reply(t('g_3a6b4a2c8f', '{0} قائمة الكيك فاضية', k))
       else:
         await m.reply(t('g_81d1693ce1', '{0} ابشر مسحت قائمة الكيك', k))
         for cake in await r.smembers(f'{Dev_Zaid}:CakeList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:CakeList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:CakeName:{cake}')
           
   ################# CAKE #################
   
   ################# 3SL #################
   if text == 'رفع عسل':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:3SLList:{m.chat.id}',id):
         return await m.reply(t('g_df706acc6f', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} عسل من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:3SLList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:3SLName:{id}', mention)
         return await m.reply(t('g_3c0c3db8cc', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته عسل 🍯\n☆', mention, k))
   
   if text == 'تنزيل عسل':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:3SLList:{m.chat.id}',id):
         return await m.reply(t('g_b819c2ccc2', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو عسل من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:3SLList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:3SLName:{id}')
         return await m.reply(t('g_3bc3c223ad', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من عسل\n☆', mention, k))
   
   if text == 'قائمه العسل' or text == 'قائمة العسل':
     if not await r.smembers(f'{Dev_Zaid}:3SLList:{m.chat.id}'):
       return await m.reply(t('g_cd7558f6a5', '{0} قائمة العسل فاضية', k))
     else:
       txt = '- قائمة العسل 🍯\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:3SLList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:3SLName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة العسل' or text == 'مسح قائمه العسل':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:3SLList:{m.chat.id}'):
         return await m.reply(t('g_cd7558f6a5', '{0} قائمة العسل فاضية', k))
       else:
         await m.reply(t('g_86350ec1a8', '{0} ابشر مسحت قائمة العسل', k))
         for cake in await r.smembers(f'{Dev_Zaid}:3SLList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:3SLList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:3SLName:{cake}')

   ################# 3SL #################
   
   ################# ZQ #################
   if text == 'رفع نصاب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:ZQList:{m.chat.id}',id):
         return await m.reply(t('g_a68bf468ea', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} نصاب من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:ZQList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:ZQName:{id}', mention)
         return await m.reply(t('g_d91632e8e2', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته نصاب 💩\n☆', mention, k))
   
   if text == 'تنزيل نصاب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:ZQList:{m.chat.id}',id):
         return await m.reply(t('g_c0bc14515e', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو نصاب من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:ZQList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:ZQName:{id}')
         return await m.reply(t('g_ac2893573f', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من نصاب\n☆', mention, k))
   
   if text == 'قائمه النصابين' or text == 'قائمة النصابين':
     if not await r.smembers(f'{Dev_Zaid}:ZQList:{m.chat.id}'):
       return await m.reply(t('g_7dbdd3c43e', '{0} قائمة النصابين فاضية', k))
     else:
       txt = '- قائمة النصابين 💩\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:ZQList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:ZQName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة النصابين' or text == 'مسح قائمه النصابين':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:ZQList:{m.chat.id}'):
         return await m.reply(t('g_7dbdd3c43e', '{0} قائمة النصابين فاضية', k))
       else:
         await m.reply(t('g_c17188e152', '{0} ابشر مسحت قائمة النصابين', k))
         for cake in await r.smembers(f'{Dev_Zaid}:ZQList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:ZQList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:ZQName:{cake}')

   ################# ZQ #################
   
   ################# 7MR #################
   if text == 'رفع حمار':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:7MRList:{m.chat.id}',id):
         return await m.reply(t('g_521c4c94b5', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} حمار من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:7MRList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:7MRName:{id}', mention)
         return await m.reply(t('g_aa8b67214c', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته حمار 🦓\n☆', mention, k))
   
   if text == 'تنزيل حمار':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:7MRList:{m.chat.id}',id):
         return await m.reply(t('g_e4c2577a1a', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو حمار من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:7MRList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:7MRName:{id}')
         return await m.reply(t('g_1e4c6b5967', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من حمار\n☆', mention, k))
   
   if text == 'قائمه الحمير' or text == 'قائمة الحمير':
     if not await r.smembers(f'{Dev_Zaid}:7MRList:{m.chat.id}'):
       return await m.reply(t('g_d1c99a86e2', '{0} قائمة الحمير فاضية', k))
     else:
       txt = '- قائمة الحمير 🦓\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:7MRList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:7MRName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الحمير' or text == 'مسح قائمه الحمير':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:7MRList:{m.chat.id}'):
         return await m.reply(t('g_d1c99a86e2', '{0} قائمة الحمير فاضية', k))
       else:
         await m.reply(t('g_6c896eb6d3', '{0} ابشر مسحت قائمة الحمير', k))
         for cake in await r.smembers(f'{Dev_Zaid}:7MRList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:7MRList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:7MRName:{cake}')

   ################# 7MR #################
   
   ################# COW #################
   if text == 'رفع بقرة' or text == 'رفع بقره':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:COWList:{m.chat.id}',id):
         return await m.reply(t('g_fa9d1c9bd2', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} بقرة من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:COWList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:COWName:{id}', mention)
         return await m.reply(t('g_fb2eb6f45b', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته بقرة 🐄\n☆', mention, k))
   
   if text == 'تنزيل بقرة' or text == 'تنزيل بقره':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:COWList:{m.chat.id}',id):
         return await m.reply(t('g_fb5cb1bd70', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو بقرة من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:COWList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:COWName:{id}')
         return await m.reply(t('g_a909c0d006', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من بقرة\n☆', mention, k))
   
   if text == 'قائمه البقر' or text == 'قائمة البقر':
     if not await r.smembers(f'{Dev_Zaid}:COWList:{m.chat.id}'):
       return await m.reply(t('g_eed6ea1d0d', '{0} قائمة البقر فاضية', k))
     else:
       txt = '- قائمة البقر 🐄\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:COWList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:COWName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة البقر' or text == 'مسح قائمه البقر':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:COWList:{m.chat.id}'):
         return await m.reply(t('g_eed6ea1d0d', '{0} قائمة البقر فاضية', k))
       else:
         await m.reply(t('g_8a0bf255e7', '{0} ابشر مسحت قائمة البقر', k))
         for cake in await r.smembers(f'{Dev_Zaid}:COWList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:COWList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:COWName:{cake}')

   ################# COW #################
   
   ################# DOG #################
   if text == 'رفع كلب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:DOGList:{m.chat.id}',id):
         return await m.reply(t('g_13f836adae', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} كلب من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:DOGList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:DOGName:{id}', mention)
         return await m.reply(t('g_e17b74c116', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته كلب 🐩\n☆', mention, k))
   
   if text == 'تنزيل كلب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:DOGList:{m.chat.id}',id):
         return await m.reply(t('g_8e9bc90a2f', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو كلب من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:DOGList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:DOGName:{id}')
         return await m.reply(t('g_0897c068d0', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من كلب\n☆', mention, k))
   
   if text == 'قائمه الكلاب' or text == 'قائمة الكلاب':
     if not await r.smembers(f'{Dev_Zaid}:DOGList:{m.chat.id}'):
       return await m.reply(t('g_a04c16703b', '{0} قائمة الكلاب فاضية', k))
     else:
       txt = '- قائمة الكلاب 🐩\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:DOGList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:DOGName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الكلاب' or text == 'مسح قائمه الكلاب':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:DOGList:{m.chat.id}'):
         return await m.reply(t('g_a04c16703b', '{0} قائمة الكلاب فاضية', k))
       else:
         await m.reply(t('g_fc319de941', '{0} ابشر مسحت قائمة الكلاب', k))
         for cake in await r.smembers(f'{Dev_Zaid}:DOGList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:DOGList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:DOGName:{cake}')

   ################# DOG #################
   
   ################# MON #################
   if text == 'رفع قرد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:MONList:{m.chat.id}',id):
         return await m.reply(t('g_1c53d26711', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} قرد من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:MONList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:MONName:{id}', mention)
         return await m.reply(t('g_9616771ddd', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته قرد 🐒\n☆', mention, k))
   
   if text == 'تنزيل قرد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:MONList:{m.chat.id}',id):
         return await m.reply(t('g_dbf5c9727a', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو قرد من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:MONList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:MONName:{id}')
         return await m.reply(t('g_2dbc132fe5', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من قرد\n☆', mention, k))
   
   if text == 'قائمه القرود' or text == 'قائمة القرود':
     if not await r.smembers(f'{Dev_Zaid}:MONList:{m.chat.id}'):
       return await m.reply(t('g_f903e1f613', '{0} قائمة القرود فاضية', k))
     else:
       txt = '- قائمة القرود 🐒\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:MONList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:MONName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة القرود' or text == 'مسح قائمه القرود':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:MONList:{m.chat.id}'):
         return await m.reply(t('g_f903e1f613', '{0} قائمة القرود فاضية', k))
       else:
         await m.reply(t('g_23f6be3209', '{0} ابشر مسحت قائمة القرود', k))
         for cake in await r.smembers(f'{Dev_Zaid}:MONList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:MONList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:MONName:{cake}')

   ################# MON #################
   
   ################# TES #################
   if text == 'رفع تيس':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:TESList:{m.chat.id}',id):
         return await m.reply(t('g_ad57a0b8c3', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} تيس من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:TESList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:TESName:{id}', mention)
         return await m.reply(t('g_c3ede079a0', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته تيس 🐐\n☆', mention, k))
   
   if text == 'تنزيل تيس':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:TESList:{m.chat.id}',id):
         return await m.reply(t('g_401100c373', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو تيس من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:TESList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:TESName:{id}')
         return await m.reply(t('g_fd1294eb69', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من تيس\n☆', mention, k))
   
   if text == 'قائمه التيس' or text == 'قائمة التيس':
     if not await r.smembers(f'{Dev_Zaid}:TESList:{m.chat.id}'):
       return await m.reply(t('g_88ba450d58', '{0} قائمة التيوس فاضية', k))
     else:
       txt = '- قائمة التيوس 🐐\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:TESList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:TESName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة التيس' or text == 'مسح قائمه التيس':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:TESList:{m.chat.id}'):
         return await m.reply(t('g_88ba450d58', '{0} قائمة التيوس فاضية', k))
       else:
         await m.reply(t('g_72fe138523', '{0} ابشر مسحت قائمة التيوس', k))
         for cake in await r.smembers(f'{Dev_Zaid}:TESList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:TESList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:TESName:{cake}')

   ################# TES #################
   
   
   ################# TOR #################
   if text == 'رفع ثور':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:TORList:{m.chat.id}',id):
         return await m.reply(t('g_4cb8be45a2', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ثور من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:TORList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:TORName:{id}', mention)
         return await m.reply(t('g_056ba40fce', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته ثور 🐂\n☆', mention, k))
   
   if text == 'تنزيل ثور':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:TORList:{m.chat.id}',id):
         return await m.reply(t('g_52167af941', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو ثور من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:TORList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:TORName:{id}')
         return await m.reply(t('g_46b950c9a6', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من ثور\n༄', mention, k))
   
   if text == 'قائمه الثور' or text == 'قائمة الثور':
     if not await r.smembers(f'{Dev_Zaid}:TORList:{m.chat.id}'):
       return await m.reply(t('g_dcc1851cb9', '{0} قائمة الثور فاضية', k))
     else:
       txt = '- قائمة الثور 🐂\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:TORList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:TORName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الثور' or text == 'مسح قائمه الثور':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:TORList:{m.chat.id}'):
         return await m.reply(t('g_dcc1851cb9', '{0} قائمة الثور فاضية', k))
       else:
         await m.reply(t('g_683ca017ed', '{0} ابشر مسحت قائمة الثور', k))
         for cake in await r.smembers(f'{Dev_Zaid}:TORList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:TORList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:TORName:{cake}')

   ################# TOR #################
   
   
   ################# B3S #################
   if text == 'رفع هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:B3SList:{m.chat.id}',id):
         return await m.reply(t('g_5ef382328c', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} هكر من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:B3SList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:B3SName:{id}', mention)
         return await m.reply(t('g_77ecf9f9b9', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته هكر 🏅\n☆', mention, k))
   
   if text == 'تنزيل هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:B3SList:{m.chat.id}',id):
         return await m.reply(t('g_5fe24b0ee8', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو هكر من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:B3SList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:B3SName:{id}')
         return await m.reply(t('g_755feb692e', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من هكر\n☆', mention, k))
   
   if text == 'قائمه الهكر' or text == 'قائمة الهكر':
     if not await r.smembers(f'{Dev_Zaid}:B3SList:{m.chat.id}'):
       return await m.reply(t('g_d402f8dd4d', '{0} قائمة الهكر فاضية', k))
     else:
       txt = '- قائمة الهكر 🏅\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:B3SList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:B3SName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الهكر' or text == 'مسح قائمه الهكر':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:B3SList:{m.chat.id}'):
         return await m.reply(t('g_d402f8dd4d', '{0} قائمة الهكر فاضية', k))
       else:
         await m.reply(t('g_a6805855c8', '{0} ابشر مسحت قائمة الهكر', k))
         for cake in await r.smembers(f'{Dev_Zaid}:B3SList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:B3SList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:B3SName:{cake}')

   ################# B3S #################
   
   ################# DJJ #################
   if text == 'رفع دجاجه' or text == 'رفع دجاجة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:DJJList:{m.chat.id}',id):
         return await m.reply(t('g_28f58ddf27', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} دجاجه من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:DJJList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:DJJName:{id}', mention)
         return await m.reply(t('g_97e3792900', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته دجاجه 🐓\n☆', mention, k))
   
   if text == 'تنزيل دجاجه' or text == 'تنزيل دجاجة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:DJJList:{m.chat.id}',id):
         return await m.reply(t('g_2975f7c0db', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو دجاجه من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:DJJList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:DJJName:{id}')
         return await m.reply(t('g_c241c3e452', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من دجاجه\n☆', mention, k))
   
   if text == 'قائمه الدجاج' or text == 'قائمة الدجاج':
     if not await r.smembers(f'{Dev_Zaid}:DJJList:{m.chat.id}'):
       return await m.reply(t('g_de63caee35', '{0} قائمة الدجاج فاضية', k))
     else:
       txt = '- قائمة الدجاج 🐓\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:DJJList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:DJJName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الدجاج' or text == 'مسح قائمه الدجاج':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:DJJList:{m.chat.id}'):
         return await m.reply(t('g_de63caee35', '{0} قائمة الدجاج فاضية', k))
       else:
         await m.reply(t('g_3a66a6b412', '{0} ابشر مسحت قائمة الدجاج', k))
         for cake in await r.smembers(f'{Dev_Zaid}:DJJList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:DJJList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:DJJName:{cake}')

   ################# DJJ #################
   
   ################# HTF #################
   if text == 'رفع ملكه':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:HTFList:{m.chat.id}',id):
         return await m.reply(t('g_e09fd51b68', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ملكه من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:HTFList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:HTFName:{id}', mention)
         return await m.reply(t('g_c2ee5025f0', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته ملكه 🧱\n☆', mention, k))
   
   if text == 'تنزيل ملكه':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:HTFList:{m.chat.id}',id):
         return await m.reply(t('g_fd1a944157', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو ملكه من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:HTFList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:HTFName:{id}')
         return await m.reply(t('g_4844bfe285', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من ملكه\n☆', mention, k))
   
   if text == 'قائمه الهطوف' or text == 'قائمة الهطوف':
     if not await r.smembers(f'{Dev_Zaid}:HTFList:{m.chat.id}'):
       return await m.reply(t('g_2fa574e209', '{0} قائمة الهطوف فاضية', k))
     else:
       txt = '- قائمة الهطوف 🧱\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:HTFList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:HTFName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الهطوف' or text == 'مسح قائمه الهطوف':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:HTFList:{m.chat.id}'):
         return await m.reply(t('g_2fa574e209', '{0} قائمة الهطوف فاضية', k))
       else:
         await m.reply(t('g_9c15d5e919', '{0} ابشر مسحت قائمة الهطوف', k))
         for cake in await r.smembers(f'{Dev_Zaid}:HTFList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:HTFList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:HTFName:{cake}')

   ################# HTF #################
   
   ################# SYD #################
   if text == 'رفع صياد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:SYDList:{m.chat.id}',id):
         return await m.reply(t('g_c42f4e3d9b', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} صياد من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:SYDList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:SYDName:{id}', mention)
         return await m.reply(t('g_6d7a063be3', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته صياد 🔫\n☆', mention, k))
   
   if text == 'تنزيل صياد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:SYDList:{m.chat.id}',id):
         return await m.reply(t('g_11cec78f3d', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو صياد من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:SYDList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:SYDName:{id}')
         return await m.reply(t('g_fd32690e1d', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من صياد\n☆', mention, k))
   
   if text == 'قائمه الصيادين' or text == 'قائمة الصيادين':
     if not await r.smembers(f'{Dev_Zaid}:SYDList:{m.chat.id}'):
       return await m.reply(t('g_1c87d267da', '{0} قائمة الصيادين فاضية', k))
     else:
       txt = '- قائمة الصيادين 🔫\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:SYDList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:SYDName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الصيادين' or text == 'مسح قائمه الصيادين':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:SYDList:{m.chat.id}'):
         return await m.reply(t('g_1c87d267da', '{0} قائمة الصيادين فاضية', k))
       else:
         await m.reply(t('g_8016cfa0b3', '{0} ابشر مسحت قائمة الصيادين', k))
         for cake in await r.smembers(f'{Dev_Zaid}:SYDList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:SYDList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:SYDName:{cake}')

   ################# SYD #################
   
   ################# 5RF #################
   if text == 'رفع خروف':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:5RFList:{m.chat.id}',id):
         return await m.reply(t('g_9233a0d264', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} خروف من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:5RFList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:5RFName:{id}', mention)
         return await m.reply(t('g_0e4d8f4489', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته خروف 🐏\n☆', mention, k))
   
   if text == 'تنزيل خروف':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:5RFList:{m.chat.id}',id):
         return await m.reply(t('g_1d36ee99bd', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو خروف من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:5RFList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:5RFName:{id}')
         return await m.reply(t('g_182748337c', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من خروف\n☆', mention, k))
   
   if text == 'قائمه الخرفان' or text == 'قائمة الخرفان':
     if not await r.smembers(f'{Dev_Zaid}:5RFList:{m.chat.id}'):
       return await m.reply(t('g_0a042e785b', '{0} قائمة الخرفان فاضية', k))
     else:
       txt = '- قائمة الخرفان 🐏\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:5RFList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:5RFName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الخرفان' or text == 'مسح قائمه الخرفان':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:5RFList:{m.chat.id}'):
         return await m.reply(t('g_0a042e785b', '{0} قائمة الخرفان فاضية', k))
       else:
         await m.reply(t('g_11bbbba5b6', '{0} ابشر مسحت قائمة الخرفان', k))
         for cake in await r.smembers(f'{Dev_Zaid}:5RFList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:5RFList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:5RFName:{cake}')

   ################# 5RF #################
   
   ################# TEZ #################
   if text == 'رفع هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if await r.sismember(f'{Dev_Zaid}:TEZList:{m.chat.id}',id):
         return await m.reply(t('g_5ef382328c', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} هكر من قبل\n☆', mention, k))
       else:
         await r.sadd(f'{Dev_Zaid}:TEZList:{m.chat.id}',id)
         await r.set(f'{Dev_Zaid}:TEZName:{id}', mention)
         return await m.reply(t('g_33fc9ca605', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر رفعته هكر ♕\n☆', mention, k))
   
   if text == 'تنزيل هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not await r.sismember(f'{Dev_Zaid}:TEZList:{m.chat.id}',id):
         return await m.reply(t('g_5fe24b0ee8', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} مو هكر من قبل\n☆', mention, k))
       else:
         await r.srem(f'{Dev_Zaid}:TEZList:{m.chat.id}',id)
         await r.delete(f'{Dev_Zaid}:TEZName:{id}')
         return await m.reply(t('g_755feb692e', '「 \u206a\u206c\u206a\u206c{0} 」\n{1} ابشر نزلته من هكر\n☆', mention, k))
   
   if text == 'قائمه هكر' or text == 'قائمة هكر':
     if not await r.smembers(f'{Dev_Zaid}:TEZList:{m.chat.id}'):
       return await m.reply(t('g_2a8f529077', '{0} قائمة هكر فاضية', k))
     else:
       txt = '- قائمة هكر ♕\n'
       count = 1
       for cake in await r.smembers(f'{Dev_Zaid}:TEZList:{m.chat.id}'):
          mention = await r.get(f'{Dev_Zaid}:TEZName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return await m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة هكر' or text == 'مسح قائمه هكر':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
     else:
       if not await r.smembers(f'{Dev_Zaid}:TEZList:{m.chat.id}'):
         return await m.reply(t('g_2a8f529077', '{0} قائمة هكر فاضية', k))
       else:
         await m.reply(t('g_45cc95d283', '{0} ابشر مسحت قائمة هكر', k))
         for cake in await r.smembers(f'{Dev_Zaid}:TEZList:{m.chat.id}'):
           await r.srem(f'{Dev_Zaid}:TEZList:{m.chat.id}',int(cake))
           await r.delete(f'{Dev_Zaid}:TEZName:{cake}')

   ################# TEZ #################
   
   ################# 🔮 #################
   
   if text == 'رفع لقلبي' and m.reply_to_message:
     return await m.reply('{} رفعته لقلبك\n{} اللهم حسد 😔'.format(k,k))
   
   if text == 'تنزيل من قلبي' and m.reply_to_message:
     return await m.reply(t('g_ff9f1c0f7c', 'اح اح ماتوصل'))
   
   ################# 🔮 #################
   
   
   
   
       
      
   
   
   