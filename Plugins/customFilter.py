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

import random, re, time, pytz
from datetime import datetime
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
import asyncio


@Client.on_message(filters.group, group=21)
async def addCustomReplyDone(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    await addreply2(c,m,k)
    
async def addreply2(c,m,k):
   if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return
   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   
   TIME_ZONE = "Asia/Riyadh"
   ZONE = pytz.timezone(TIME_ZONE)
   TIME = datetime.now(ZONE)
   date = TIME.strftime("%d/%m/%Y %I:%M:%S %p")
   
   if m.text:
     if m.text == 'الغاء' and await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}'):
       await r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
       await m.reply(f'{k} من عيوني لغيت اضافة الرد')
     
     if await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id, m.chat.id):
       text = await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
       await r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type=text&text={m.text.html}')
       await r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','نص')
       await r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
       await r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
       await r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
       return await m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.photo and await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id, m.chat.id):
      type = 'photo'
      photo = m.photo.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&photo={photo}&caption={caption}')
      await r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','صوره')
      await r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      await r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.video and await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id, m.chat.id):
      type = 'video'
      video = m.video.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&video={video}&caption={caption}')
      await r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','فيديو')
      await r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      await r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.animation and await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id, m.chat.id):
      type = 'animation'
      anim = m.animation.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&animation={anim}&caption={caption}')
      await r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','متحركه')
      await r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      await r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.audio and await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id, m.chat.id):
      type = 'audio'
      aud = m.audio.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&audio={aud}&caption={caption}')
      await r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','صوت')
      await r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      await r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.voice and await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id, m.chat.id):
      type = 'voice'
      voice = m.voice.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&voice={voice}&caption={caption}')
      await r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','بصمه')
      await r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      await r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.document and await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id, m.chat.id):
      type = 'doc'
      doc = m.document.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&doc={doc}&caption={caption}')
      await r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','ملف')
      await r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      await r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.sticker and await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id, m.chat.id):
      type = 'sticker'
      stic = m.sticker.file_id
      text = await r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&sticker={stic}')
      await r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','ستيكر')
      await r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      await r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      await r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   

@Client.on_message(filters.text & filters.group, group=22)
async def addCustomReply(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    await addreply(c,m,k)
    
async def addreply(c,m,k):
   if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return
   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
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
   if await isLockCommand(m.from_user.id, m.chat.id, text): return
   if await r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}')
     await m.reply(f'{k} من عيوني لغيت اضافة الرد')
     return 
   
   if await r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}')
     await m.reply(f'{k} من عيوني لغيت مسح الرد')
     return 

   if await r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id,m.chat.id):
      if not await r.get(f'{m.text}:filterInfo:{m.chat.id}{Dev_Zaid}'):
        await r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}')
        return await m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود')
      else:
           await r.delete(f'{m.text}:filter:{Dev_Zaid}{m.chat.id}')
           await r.delete(f'{m.text}:filtertype:{m.chat.id}{Dev_Zaid}')
           await r.delete(f'{m.text}:filterInfo:{m.chat.id}{Dev_Zaid}')
           await r.srem(f'{m.chat.id}:FiltersList:{Dev_Zaid}', m.text)
           await r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}')
           return await m.reply(f'( {m.text} )\n{k} وحذفنا الرد ياحلو')

   if await r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id,m.chat.id):
      await r.set(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}', m.text)
      await r.delete(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}')
      await m.reply(f'{k} حلو الحين ارسل جواب الرد\n{k} ( نص,صوره,فيديو,متحركه,بصمه,صوت,ملف )\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
      return 

   if text.startswith('الرد ') and len(m.text.split()) > 1 and await mod_pls(m.from_user.id,m.chat.id):
      reply = m.text.split(None,1)[1]
      if not await r.get(f'{reply}:filterInfo:{m.chat.id}{Dev_Zaid}'):
        return await m.reply(f'{k} الرد مو مضاف')
      else:
        get = await r.get(f'{reply}:filterInfo:{m.chat.id}{Dev_Zaid}')
        split = get.split('by=')[1]
        by = split.split('&date=')[0]
        date = split.split('&date=')[1]
        type = await r.get(f'{reply}:filtertype:{m.chat.id}{Dev_Zaid}')
        text = f'{k} الرد ↢ [{reply}](tg://user?id={by})\n{k} تاريخ الاضافة ↢\n( {date} )\n{k} نوع الرد {type}\n☆'
        await m.reply(text)
        return 
   
   if text == 'تعطيل الردود':
     if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if await r.get(f'{m.chat.id}:lock_filter:{Dev_Zaid}'):
        return await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} الردود معطله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        await r.set(f'{m.chat.id}:lock_filter:{Dev_Zaid}',1)
        return await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الردود\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'تفعيل الردود':
     if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if not await r.get(f'{m.chat.id}:lock_filter:{Dev_Zaid}'):
        return await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} الردود مفعله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        await r.delete(f'{m.chat.id}:lock_filter:{Dev_Zaid}')
        return await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الردود\n☆',parse_mode=ParseMode.HTML)
  
   if text == 'تعطيل ردود الاعضاء':
     if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if await r.get(f'{m.chat.id}:lock_filterMEM:{Dev_Zaid}'):
        return await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود الاعضاء معطله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        await r.set(f'{m.chat.id}:lock_filterMEM:{Dev_Zaid}',1)
        return await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت ردود الاعضاء\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'تفعيل ردود الاعضاء':
     if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if not await r.get(f'{m.chat.id}:lock_filterMEM:{Dev_Zaid}'):
        return await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود الاعضاء مفعله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        await r.delete(f'{m.chat.id}:lock_filterMEM:{Dev_Zaid}')
        return await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت ردود الاعضاء\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'ردود الاعضاء':
     if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not await r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}'):
       return await m.reply(f'{k} مافيه ردود اعضاء مضافه')
      else:
       text = 'ردود الاعضاء:\n'
       count = 1
       for reply in await r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}'):
          rep = reply.split("&&&&")[0]
          type = reply.split("&&&&")[1]
          try:
            mention=await c.get_users(int(type)).mention
          except Exception:
            mention=f'<a href="tg://user?id={type}">{type}</a>'
          text += f'\n{count} - ( {rep} ) ࿓ ( {mention} )'
          count += 1
       text += '\n☆'
       return await m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
   
   if text == 'مسح ردود الاعضاء':
     if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not await r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}'):
        return await m.reply(f'{k} مافيه ردود اعضاء مضافه')
      else:
        total = 0
        for reply in await r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}'):
           rep = reply
           await r.delete(f'{rep}:filterMEM:{Dev_Zaid}{m.chat.id}')
           await r.srem(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}', rep)
           await r.delete(f"{rep.split('&&&&')[1]}:FILT:{m.chat.id}{Dev_Zaid}")
           total += 1
        return await m.reply(f'{k} ابشر مسحت ( {total} ) من ردود الاعضاء')
   
   if text == 'الردود':
     if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not await r.smembers(f'{m.chat.id}:FiltersList:{Dev_Zaid}'):
       return await m.reply(f'{k} مافيه ردود مضافه')
      else:
       text = 'ردود المجموعه:\n'
       count = 1
       for reply in await r.smembers(f'{m.chat.id}:FiltersList:{Dev_Zaid}'):
          rep = reply
          type = await r.get(f'{rep}:filtertype:{m.chat.id}{Dev_Zaid}')
          text += f'\n{count} - ( {rep} ) ࿓ ( {type} )'
          count += 1
       text += '\n☆'
       return await m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
  
   if text == 'مسح الردود':
     if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not await r.smembers(f'{m.chat.id}:FiltersList:{Dev_Zaid}'):
        return await m.reply(f'{k} مافيه ردود مضافه')
      else:
        total = 0
        for reply in await r.smembers(f'{m.chat.id}:FiltersList:{Dev_Zaid}'):
           rep = reply
           await r.delete(f'{rep}:filter:{Dev_Zaid}{m.chat.id}')
           await r.delete(f'{rep}:filtertype:{m.chat.id}{Dev_Zaid}')
           await r.delete(f'{rep}:filterInfo:{m.chat.id}{Dev_Zaid}')
           await r.srem(f'{m.chat.id}:FiltersList:{Dev_Zaid}', rep)
           total += 1
        return await m.reply(f'{k} ابشر مسحت ( {total} ) من الردود')
   
   if text == 'اضف ردي':
      if await r.get(f'{m.chat.id}:lock_filterMEM:{Dev_Zaid}'):
        return await m.reply(f'{k} تم تعطيل ردود الأعضاء')
      if await r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}"):
        name = await r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}")
        return await m.reply(f"{k} عندك رد مضاف من قبل و هو ( {name} )")
      else:
        await m.reply(f'{k} حلو ، الحين ارسل اسمك')
        await r.set(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_Zaid}',1,ex=600)
        return 
   
   if await r.get(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_Zaid}') and text == "الغاء":
     await r.delete(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_Zaid}')
     return await m.reply(f"{k} ابشر لغيت اضافة ردك")
     
   
   if await r.get(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_Zaid}') and len(m.text) <= 50:
     name = m.text
     if await r.sismember(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}',name):
       return await m.reply(f"{k} هذا الإسم محجوز")
     else:
       await r.sadd(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}',f"{name}&&&&{m.from_user.id}")
       await r.sadd(f'{m.chat.id}:FiltersListMEMM:{Dev_Zaid}',m.from_user.id)
       await r.set(f'{name}:filterMEM:{Dev_Zaid}{m.chat.id}',m.from_user.id)
       await r.set(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}",name)
       await r.delete(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_Zaid}')
       return await m.reply(f"{k} ابشر ضفت ردك ( {name} )")
   
   if text == 'مسح ردي':
     if await r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}"):
       rep=await r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}")
       await r.delete(f'{rep}:filterMEM:{Dev_Zaid}{m.chat.id}')
       await r.srem(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}', f"{rep}&&&&{m.from_user.id}")
       await r.delete(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}")
       return await m.reply(f"{k} ابشر مسحت ردك ( {rep} )")
     else:
       return await m.reply(f"{k} ماعندك رد")
        
   if text == 'اضف رد':
     if not await r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}'):
      if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        await m.reply(f'{k} حلو ، الحين ارسل الكلمة اللي تبيها')
        await r.set(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}',1)
        return 
        
   if text == 'مسح رد':
     if not await r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}'):
      if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        await r.set(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}',1)
        await m.reply(f'{k} تمام عيني\n{k} الحين ارسل الرد عشان امسحه\n☆',parse_mode=ParseMode.HTML)
        return 
   
   
   
   
   

   

@Client.on_message(filters.group & filters.text, group=23)
async def addCustomReplyRandom(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    await addreplyrandom(c,m,k)
   

async def addreplyrandom(c,m,k):
   if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return
   if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
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

   if await r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}')
     await m.reply(f'{k} من عيوني لغيت اضافة الرد المميز')
     return 
   
   if await r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     rep = await r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}')
     await r.delete(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}')
     await r.delete(f'{rep}:randomfilter:{m.chat.id}{Dev_Zaid}')
     await m.reply(f'{k} من عيوني لغيت اضافه الرد المميز')
     return 
     
   if await r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}')
     return await m.reply(f'{k} من عيوني لغيت مسح الرد المميز')
   
   if await r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}') and text == 'تم':
     text = await r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}')
     count = len(await r.smembers((f'{text}:randomfilter:{m.chat.id}{Dev_Zaid}')))
     await r.set(f'{text}:randomFilter:{m.chat.id}{Dev_Zaid}', 1)
     await r.sadd(f'{m.chat.id}:RFiltersList:{Dev_Zaid}', text)
     await r.delete(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}')
     return await m.reply(f'{k} تم اضافه الرد المميز ( {text} )\n{k} بـ ( {count} ) جواب رد\n☆',parse_mode=ParseMode.HTML)
   
   if await r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id,m.chat.id):
     if not await r.get(f'{m.text}:randomFilter:{m.chat.id}{Dev_Zaid}'):
       await r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}')
       return await m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود')
     else:
       await r.delete(f'{m.text}:randomFilter:{m.chat.id}{Dev_Zaid}')
       await r.delete(f'{m.text}:randomfilter:{m.chat.id}{Dev_Zaid}')
       await r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}')
       await r.srem(f'{m.chat.id}:RFiltersList:{Dev_Zaid}',m.text)
       return await m.reply(f'{k} ابشر مسحت الرد العشوائي ')
       
   
   if await r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id,m.chat.id):
     await r.delete(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}')
     await r.set(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}',m.text)
     return await m.reply(f'{k} حلو الحين ارسل اجوبة الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
   
   if await r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id,m.chat.id):
     text = await r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}')
     await r.sadd(f'{text}:randomfilter:{m.chat.id}{Dev_Zaid}', m.text.html)
     return await m.reply(f'{k} حلو ضفت هذا الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
     
   if text == 'الردود المميزه':
     if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not await r.smembers(f'{m.chat.id}:RFiltersList:{Dev_Zaid}'):
       return await m.reply(f'{k} مافيه ردود عشوائيه مضافه')
      else:
       text = 'الردود المميزه:\n'
       count = 1
       for reply in await r.smembers(f'{m.chat.id}:RFiltersList:{Dev_Zaid}'):
          rep = reply
          ttt = len(await r.smembers(f'{rep}:randomfilter:{m.chat.id}{Dev_Zaid}'))
          text += f'\n{count} - ( {rep} ) ☆ ( {ttt} )'
          count += 1
       text += '\n☆'
       return await m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
   
   if text == 'مسح الردود المميزه':
     if not await mod_pls(m.from_user.id,m.chat.id):
       return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       if not await r.smembers(f'{m.chat.id}:RFiltersList:{Dev_Zaid}'):
         return await m.reply(f'{k} مافيه ردود مميزه مضافه')
       else:
         count = 0
         for reply in await r.smembers(f'{m.chat.id}:RFiltersList:{Dev_Zaid}'):
            rep = reply
            await r.delete(f'{rep}:randomfilter:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:RFiltersList:{Dev_Zaid}', rep)
            await r.delete(f'{rep}:randomFilter:{m.chat.id}{Dev_Zaid}')
            count += 1
         return await m.reply(f'{k} ابشر مسحت ( {count} ) رد مميز ')
            
   if text == 'اضف رد مميز' and not await r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}') and not await r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}'):
     if not await mod_pls(m.from_user.id,m.chat.id):
       return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       await r.set(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}',1)
       return await m.reply(f'{k} حلو ، ارسل الحين الكلمة الي تبيها')
   
   if text == 'مسح رد مميز' and not await r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}'):
     if not await mod_pls(m.from_user.id,m.chat.id):
       return await m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       await r.set(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}',1)
       return await m.reply(f'{k} تمام عيني\n{k} الحين ارسل الرد عشان امسحه\n☆',parse_mode=ParseMode.HTML)
   
   
     
     
     
