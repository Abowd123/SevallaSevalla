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
import asyncio


@Client.on_message(filters.group, group=24)
async def addCustomReplyG(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    await addreplyg(c,m,k)
    
async def addreplyg(c,m,k):
  if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
  if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return 
  if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
  if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
  if await r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return    
  if await r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return
  if await r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or await r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
  if m.text:
   text = m.text
   name = await r.get(f'{Dev_Zaid}:BotName') or 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if await r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = await r.get(f'Custom:{Dev_Zaid}&text={text}')
   
   if await r.get(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}')
     await m.reply(t('g_ad24f13b8e', '{0} من عيوني لغيت اضافة الرد العام', k))
     return 
   
   if await r.get(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}')
     await m.reply(t('g_d80aba7a8d', '{0} من عيوني لغيت مسح الرد العام', k))
     return 
   
   if m.text == 'الغاء' and await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}'):
       await r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
       await m.reply(t('g_ad24f13b8e', '{0} من عيوني لغيت اضافة الرد العام', k))

   if await r.get(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id,m.chat.id):
      if not await r.get(f'{m.text}:filterInfo:{Dev_Zaid}'):
        await r.delete(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}')
        return await m.reply(t('g_ff937e5102', '{0} هذا الرد مو مضاف في قائمة الردود العامه', k))
      else:
           await r.delete(f'{m.text}:filter:{Dev_Zaid}')
           await r.delete(f'{m.text}:filtertype:{Dev_Zaid}')
           await r.delete(f'{m.text}:filterInfo:{Dev_Zaid}')
           await r.srem(f'FiltersList:{Dev_Zaid}', m.text)
           await r.delete(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}')
           return await m.reply(t('g_a37ae4bd02', '( {0} )\n{1} وحذفنا الرد ياحلو', m.text, k))   

   
   if text == 'تعطيل ردود المطور':
     if not await owner_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_4a108ff756', '{0} هذا الأمر يخص ( المالك وفوق ) بس', k))
     if await r.get(f'{m.chat.id}:lock_global:{Dev_Zaid}'):
        return await m.reply(t('g_af0d177004', '{0} من「 {1} 」\n{2} ردود المطور معطله من قبل\n☆', k, m.from_user.mention, k),parse_mode=ParseMode.HTML)
     else:
        await r.set(f'{m.chat.id}:lock_global:{Dev_Zaid}',1)
        return await m.reply(t('g_1e1a1b7cae', '{0} من「 {1} 」\n{2} ابشر عطلت ردود المطور\n☆', k, m.from_user.mention, k),parse_mode=ParseMode.HTML)
   
   if text == 'تفعيل ردود المطور':
     if not await owner_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_4a108ff756', '{0} هذا الأمر يخص ( المالك وفوق ) بس', k))
     if not await r.get(f'{m.chat.id}:lock_global:{Dev_Zaid}'):
        return await m.reply(t('g_ba40930100', '{0} من「 {1} 」\n{2} ردود المطور مفعله من قبل\n☆', k, m.from_user.mention, k),parse_mode=ParseMode.HTML)
     else:
        await r.delete(f'{m.chat.id}:lock_global:{Dev_Zaid}')
        return await m.reply(t('g_d755684456', '{0} من「 {1} 」\n{2} ابشر فعلت ردود المطور\n☆', k, m.from_user.mention, k),parse_mode=ParseMode.HTML)
   
   if text == 'الردود العامه':
     if not await dev2_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_87098c46e6', '{0} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس', k))
     else:
      if not await r.smembers(f'FiltersList:{Dev_Zaid}'):
       return await m.reply(t('g_84d2f25b58', '{0} مافيه ردود عامه مضافه', k))
      else:
       text = 'ردود البوت:\n'
       count = 1
       for reply in await r.smembers(f'FiltersList:{Dev_Zaid}'):
          rep = reply
          type = await r.get(f'{rep}:filtertype:{Dev_Zaid}')
          text += f'\n{count} - ( {rep} ) ࿓ ( {type} )'
          count += 1
       text += '\n☆'
       return await m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
  
   if text == 'مسح الردود العامه':
     if not await dev2_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_87098c46e6', '{0} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس', k))
     else:
      if not await r.smembers(f'FiltersList:{Dev_Zaid}'):
        return await m.reply(t('g_84d2f25b58', '{0} مافيه ردود عامه مضافه', k))
      else:
        total = 0
        for reply in await r.smembers(f'FiltersList:{Dev_Zaid}'):
           rep = reply
           await r.delete(f'{rep}:filter:{Dev_Zaid}')
           await r.delete(f'{rep}:filtertype:{Dev_Zaid}')
           await r.delete(f'{rep}:filterInfo:{Dev_Zaid}')
           await r.srem(f'FiltersList:{Dev_Zaid}', rep)
           total += 1
        return await m.reply(t('g_db795cdd93', '{0} ابشر مسحت ( {1} ) من الردود العامه', k, total))   
     
   if text == 'مسح رد عام':
     if not await r.get(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}'):
      if not await dev2_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_87098c46e6', '{0} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس', k))
      else:
        await r.set(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}',1)
        await m.reply(t('g_231d5ef18b', '{0} تمام عيني\n{1} الحين ارسل الرد عشان امسحه\n☆', k, k),parse_mode=ParseMode.HTML)
        return 
   
   if text == 'اضف رد عام':
       if not await r.get(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}'):
         if not await dev2_pls(m.from_user.id, m.chat.id):
           return await m.reply(t('g_87098c46e6', '{0} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس', k))
         else:
           await m.reply(t('g_18ed33f0bd', '{0} حلو ، الحين ارسل الكلمة اللي تبيها', k))
           await r.set(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}',1)
           return 
   
   if await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id, m.chat.id):
       text = await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
       await r.set(f'{text}:filter:{Dev_Zaid}', f'type=text&text={m.text.html}')
       await r.set(f'{text}:filtertype:{Dev_Zaid}','نص')
       await r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
       await r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
       await r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
       return await m.reply(t('g_273ba34c68', '( {0} )\nواضفنا الرد ياحلو\n☆', text),parse_mode=ParseMode.HTML)
     
   if await r.get(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id,m.chat.id):
      await r.set(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}', m.text)
      await r.delete(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}')
      await m.reply(t('g_262068b5da', '{0} حلو الحين ارسل جواب الرد\n{1} ( نص,صوره,فيديو,متحركه,بصمه,صوت,ملف )\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄', k, k),parse_mode=ParseMode.MARKDOWN)
      return 
  
  await addreply_media(c,m,k)

async def addreply_media(c,m,k):
   if m.photo and await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id, m.chat.id):
      type = 'photo'
      photo = m.photo.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&photo={photo}&caption={caption}')
      await r.set(f'{text}:filtertype:{Dev_Zaid}','صوره')
      await r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      await r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(t('g_273ba34c68', '( {0} )\nواضفنا الرد ياحلو\n☆', text),parse_mode=ParseMode.HTML)
   
   if m.video and await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id, m.chat.id):
      type = 'video'
      video = m.video.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&video={video}&caption={caption}')
      await r.set(f'{text}:filtertype:{Dev_Zaid}','فيديو')
      await r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      await r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(t('g_273ba34c68', '( {0} )\nواضفنا الرد ياحلو\n☆', text),parse_mode=ParseMode.HTML)
   
   if m.animation and await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id, m.chat.id):
      type = 'animation'
      anim = m.animation.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&animation={anim}&caption={caption}')
      await r.set(f'{text}:filtertype:{Dev_Zaid}','متحركه')
      await r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      await r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(t('g_273ba34c68', '( {0} )\nواضفنا الرد ياحلو\n☆', text),parse_mode=ParseMode.HTML)
   
   if m.audio and await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id, m.chat.id):
      type = 'audio'
      aud = m.audio.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&audio={aud}&caption={caption}')
      await r.set(f'{text}:filtertype:{Dev_Zaid}','صوت')
      await r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      await r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(t('g_273ba34c68', '( {0} )\nواضفنا الرد ياحلو\n☆', text),parse_mode=ParseMode.HTML)
   
   if m.voice and await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id, m.chat.id):
      type = 'voice'
      voice = m.voice.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&voice={voice}&caption={caption}')
      await r.set(f'{text}:filtertype:{Dev_Zaid}','بصمه')
      await r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      await r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(t('g_273ba34c68', '( {0} )\nواضفنا الرد ياحلو\n☆', text),parse_mode=ParseMode.HTML)
   
   if m.document and await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id, m.chat.id):
      type = 'doc'
      doc = m.document.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&doc={doc}&caption={caption}')
      await r.set(f'{text}:filtertype:{Dev_Zaid}','ملف')
      await r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      await r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(t('g_273ba34c68', '( {0} )\nواضفنا الرد ياحلو\n☆', text),parse_mode=ParseMode.HTML)
   
   if m.sticker and await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id, m.chat.id):
      type = 'sticker'
      stic = m.sticker.file_id
      text = await r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&sticker={stic}')
      await r.set(f'{text}:filtertype:{Dev_Zaid}','ملصق')
      await r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      await r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(t('g_273ba34c68', '( {0} )\nواضفنا الرد ياحلو\n☆', text),parse_mode=ParseMode.HTML)
   
   
   
   
   
'''
@Client.on_message(filters.group, group=25)
def addCustomReplyDoneG(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    addreply2g(c,m,k)
    
def addreply2g(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   
   
   if m.text:
     
'''     
     
   
   
   
   

@Client.on_message(filters.group & filters.text, group=26)
async def addCustomReplyRandomG(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    await addreplyrandomg(c,m,k)
   

async def addreplyrandomg(c,m,k):
   if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return
   if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or await r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = await r.get(f'{Dev_Zaid}:BotName') or 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if await r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = await r.get(f'Custom:{Dev_Zaid}&text={text}')

   if await r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}')
     await m.reply(t('g_2f64295f19', '{0} من عيوني لغيت اضافة الرد المتعدد عام', k))
     return 
   
   if await r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     rep = await r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}')
     await r.delete(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}')
     await r.delete(f'{rep.decode("utf-8")}:randomfilter:{Dev_Zaid}')
     await m.reply(t('g_d2df00e4ce', '{0} من عيوني لغيت اضافه الرد المتعدد عام', k))
     return 
     
   if await r.get(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}')
     return await m.reply(t('g_0dd3f703df', '{0} من عيوني لغيت مسح الرد المتعدد العام', k))
   
   if await r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}') and text == 'تم':
     text = await r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}')
     count = len(await r.smembers((f'{text}:randomfilter:{Dev_Zaid}')))
     await r.set(f'{text}:randomFilter:{Dev_Zaid}', 1)
     await r.sadd(f'RFiltersList:{Dev_Zaid}', text)
     await r.delete(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}')
     return await m.reply(t('g_f3be120990', '{0} تم اضافه الرد المتعدد ( {1} )\n{2} بـ ( {3} ) جواب رد\n☆', k, text, k, count),parse_mode=ParseMode.HTML)
   
   if await r.get(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id,m.chat.id):
     if not await r.get(f'{m.text}:randomFilter:{Dev_Zaid}'):
       await r.delete(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}')
       return await m.reply(t('g_badad1372d', '{0} هذا الرد مو مضاف في قائمة الردود', k))
     else:
       await r.delete(f'{m.text}:randomFilter:{Dev_Zaid}')
       await r.delete(f'{m.text}:randomfilter:{Dev_Zaid}')
       await r.delete(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}')
       await r.srem(f'RFiltersList:{Dev_Zaid}',m.text)
       return await m.reply(t('g_a4f3413a50', '{0} ابشر مسحت الرد المتعدد ', k))
       
   
   if await r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id,m.chat.id):
     await r.delete(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}')
     await r.set(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}',m.text)
     return await m.reply(t('g_0a542c5376', '{0} حلو الحين ارسل اجوبة الرد\n{1} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄', k, k),parse_mode=ParseMode.MARKDOWN)
   
   if await r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}') and await dev2_pls(m.from_user.id,m.chat.id):
     text = await r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}')
     await r.sadd(f'{text}:randomfilter:{Dev_Zaid}', m.text.html)
     return await m.reply(t('g_5cdabc3b9a', '{0} حلو ضفت هذا الرد\n{1} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄', k, k),parse_mode=ParseMode.MARKDOWN)
     
   if text == 'الردود المتعدده العامه':
     if not await dev2_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_87098c46e6', '{0} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس', k))
     else:
      if not await r.smembers(f'RFiltersList:{Dev_Zaid}'):
       return await m.reply(t('g_a2e9b9ee0f', '{0} مافيه ردود عشوائيه عامة', k))
      else:
       text = 'الردود المتعدده:\n'
       count = 1
       for reply in await r.smembers(f'RFiltersList:{Dev_Zaid}'):
          rep = reply
          ttt = len(await r.smembers(f'{rep}:randomfilter:{Dev_Zaid}'))
          text += f'\n{count} - ( {rep} ) ࿓ ( {ttt} )'
          count += 1
       text += '\n☆'
       return await m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
   
   if text == 'مسح الردود المتعدده العامه':
     if not await dev2_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_87098c46e6', '{0} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس', k))
     else:
       if not await r.smembers(f'RFiltersList:{Dev_Zaid}'):
         return await m.reply(t('g_a2e9b9ee0f', '{0} مافيه ردود عشوائيه عامة', k))
       else:
         count = 0
         for reply in await r.smembers(f'RFiltersList:{Dev_Zaid}'):
            rep = reply
            await r.delete(f'{rep}:randomfilter:{Dev_Zaid}')
            await r.srem(f'RFiltersList:{Dev_Zaid}', rep)
            await r.delete(f'{rep}:randomFilter:{Dev_Zaid}')
            count += 1
         return await m.reply(t('g_bed8a13150', '{0} ابشر مسحت ( {1} ) رد متعدد ', k, count))
            
            
   
   if text == 'اضف رد متعدد عام' and not await r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}') and not await r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}'):
     if not await dev2_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_87098c46e6', '{0} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس', k))
     else:
       await r.set(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}',1)
       return await m.reply(t('g_b9f0553ff0', '{0} حلو ، ارسل الحين الكلمة الي تبيها', k))
   
   if text == 'مسح رد متعدد عام' and not await r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}'):
     if not await dev2_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_87098c46e6', '{0} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس', k))
     else:
       await r.set(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}',1)
       return await m.reply(t('g_231d5ef18b', '{0} تمام عيني\n{1} الحين ارسل الرد عشان امسحه\n☆', k, k),parse_mode=ParseMode.HTML)
   
   
     
     
     
