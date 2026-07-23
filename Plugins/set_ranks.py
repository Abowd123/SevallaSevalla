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
from helpers.Ranks import *
from helpers.Ranks import isLockCommand
import asyncio


@Client.on_message(filters.text & filters.group, group=7)
async def ranksCommandsHandler(c,m):
   k = await r.get(f'{Dev_Zaid}:botkey')
   await ranks_reply_promote(c,m,k)
   

async def ranks_reply_promote(c,m,k):
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
    if text == 'تعطيل الرفع':
      if not await owner_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
      else:
        if await r.get(f'{m.chat.id}:disableRanks:{Dev_Zaid}'):
          return await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} الرفع معطل من قبل\n☆')
        else:
          await r.set(f'{m.chat.id}:disableRanks:{Dev_Zaid}', 1)
          return await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الرفع\n☆')
    
    if text == 'تفعيل الرفع':
      if not await owner_pls(m.from_user.id, m.chat.id):
        return await m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
      else:
        if not await r.get(f'{m.chat.id}:disableRanks:{Dev_Zaid}'):
          return await m.reply(f'「 {m.from_user.mention} 」\n{k} الرفع مفعل من قبل\n☆')
        else:
          await r.delete(f'{m.chat.id}:disableRanks:{Dev_Zaid}')
          return await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الرفع\n☆')
    
    cid = m.chat.id
    
    if await r.get(f'{m.chat.id}:disableRanks:{Dev_Zaid}'):  return
    rank = await get_rank(m.from_user.id, m.chat.id)
    if text.startswith('رفع Dev '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await devp_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( Dev🎖️) بس')
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        
           
        if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} Dev²🎖 من قبل\n☆')
        else:
          await r.set(f'{id}:rankDEV2:{Dev_Zaid}', 1)
          await r.sadd(f'{Dev_Zaid}DEV2', id)
          return await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار Dev²🎖\n☆')
          if await r.get(f'{id}:mute:{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{Dev_Zaid}')
            await r.srem(f'listMUTE:{Dev_Zaid}', id)
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع Dev' and m.reply_to_message and m.reply_to_message.from_user:
        if not await devp_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( Dev🎖️) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')        
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')           
        if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} Dev²🎖 من قبل\n☆')
        else:
          await r.set(f'{id}:rankDEV2:{Dev_Zaid}', 1)
          await r.sadd(f'{Dev_Zaid}DEV2', id)
          return await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار Dev²🎖\n☆')
          if await r.get(f'{id}:mute:{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{Dev_Zaid}')
            await r.srem(f'listMUTE:{Dev_Zaid}', id)
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
          
    if text.startswith('رفع MY '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return False
        if not await dev2_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص ( Dev²🎖️ وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} Myth🎖️ من قبل\n☆')
        else:
          await r.set(f'{id}:rankDEV:{Dev_Zaid}', 1)
          await r.sadd(f'{Dev_Zaid}DEV', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار Myth🎖️\n☆')
          if await r.get(f'{id}:mute:{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{Dev_Zaid}')
            await r.srem(f'listMUTE:{Dev_Zaid}', id)
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع MY' and m.reply_to_message and m.reply_to_message.from_user:
        if not await dev2_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص ( Dev²🎖️ وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')        
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} Myth🎖️ من قبل\n☆')
        else:
          await r.set(f'{id}:rankDEV:{Dev_Zaid}', 1)
          await r.sadd(f'{Dev_Zaid}DEV', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار Myth🎖️\n☆')
          if await r.get(f'{id}:mute:{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{Dev_Zaid}')
            await r.srem(f'listMUTE:{Dev_Zaid}', id)
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    cid = m.chat.id
    
    if text.startswith('رفع مالك اساسي '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await gowner_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) بس')
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')           
        if await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مالك اساسي من قبل\n☆')
        else:
          await r.set(f'{cid}:rankGOWNER:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك اساسي\n☆')
          if await r.get(f'{id}:mute:{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{Dev_Zaid}')
            await r.srem(f'listMUTE:{Dev_Zaid}', id)
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
          return 
    
    if text == 'رفع مالك اساسي' and m.reply_to_message and m.reply_to_message.from_user:
        if not await gowner_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص (المالك الاساسي وفوق) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention       
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')           
        if await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مالك اساسي من قبل\n☆')
        else:
          await r.set(f'{cid}:rankGOWNER:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك اساسي\n☆')
          if await r.get(f'{id}:mute:{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{Dev_Zaid}')
            await r.srem(f'listMUTE:{Dev_Zaid}', id)
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
          return 
    
    if text.startswith('رفع مالك '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await gowner_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( المالك الاساسي ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مالك من قبل\n☆')
        else:
          await r.set(f'{cid}:rankOWNER:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listOWNER:{Dev_Zaid}', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك\n☆')
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع مالك' and m.reply_to_message and m.reply_to_message.from_user:
        if not await gowner_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( المالك الاساسي ) بس')
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مالك من قبل\n☆')
        else:
          await r.set(f'{cid}:rankOWNER:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listOWNER:{Dev_Zaid}', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك\n☆')
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    
    if text.startswith('رفع مدير '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await owner_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')           
        if await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مدير من قبل\n☆')
        else:
          await r.set(f'{cid}:rankMOD:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listMOD:{Dev_Zaid}', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مدير\n☆')
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع مدير' and m.reply_to_message and m.reply_to_message.from_user:
        if not await owner_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')           
        if await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مدير من قبل\n☆')
        else:
          await r.set(f'{cid}:rankMOD:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listMOD:{Dev_Zaid}', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مدير\n☆')
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text.startswith('رفع ادمن '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await mod_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
           
        if await r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} ادمن من قبل\n☆')
        else:
          await r.set(f'{cid}:rankADMIN:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listADMIN:{Dev_Zaid}', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار ادمن\n☆')
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع ادمن' and m.reply_to_message and m.reply_to_message.from_user:        
        if not await mod_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
           
        if await r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} ادمن من قبل\n☆')
        else:
          await r.set(f'{cid}:rankADMIN:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listADMIN:{Dev_Zaid}', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار ادمن\n☆')
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text.startswith('رفع مميز '):
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not await admin_pls(m.from_user.id,m.chat.id):
        return await m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
      else:
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if await r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مميز من قبل\n☆')
        else:
          await r.set(f'{cid}:rankPRE:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listPRE:{Dev_Zaid}', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مميز\n☆')
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع مميز' and m.reply_to_message and m.reply_to_message.from_user:
      if not await admin_pls(m.from_user.id,m.chat.id):
        return await m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
      else:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return await m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if await r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مميز من قبل\n☆')
        else:
          await r.set(f'{cid}:rankPRE:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listPRE:{Dev_Zaid}', id)
          await m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مميز\n☆')
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
          
    
    
    
@Client.on_message(filters.text & filters.group, group=8)
async def ranksCommandsHandlerDemote(c,m):
   k = await r.get(f'{Dev_Zaid}:botkey')
   await ranks_reply_demote(c,m,k)


async def ranks_reply_demote(c,m,k):
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
    rank = await get_rank(m.from_user.id, m.chat.id)
    cid = m.chat.id
    
    if text == 'تنزيل Dev' and m.reply_to_message and m.reply_to_message.from_user:
        if not await devp_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص ( Dev🎖️) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention     
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')           
        if not await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو Dev²🎖\n☆')
        else:
          await r.delete(f'{id}:rankDEV2:{Dev_Zaid}')
          await r.srem(f'{Dev_Zaid}DEV2', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من Dev²🎖\n☆')
    
    if text.startswith('تنزيل Dev '):
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not await devp_pls(m.from_user.id,m.chat.id):
        return await m.reply(f'{k} هذا الامر يخص ( Dev🎖️) بس')
      else:
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')           
        if not await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو Dev²🎖\n☆')
        else:
          await r.delete(f'{id}:rankDEV2:{Dev_Zaid}')
          await r.srem(f'{Dev_Zaid}DEV2', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من Dev²🎖\n☆')
          
    if text == 'تنزيل MY'  and m.reply_to_message and m.reply_to_message.from_user:
        if not await dev2_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( Dev²🎖️ وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')        
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')           
        if not await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو Myth🎖️ من قبل\n☆')
        else:
          await r.delete(f'{id}:rankDEV:{Dev_Zaid}')
          await r.srem(f'{Dev_Zaid}DEV', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من Myth🎖️\n☆')
    
    if text.startswith('تنزيل MY '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await dev2_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( Dev²🎖️ وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')
        
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
           
        if not await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو Myth🎖️ من قبل\n☆')
        else:
          await r.delete(f'{id}:rankDEV:{Dev_Zaid}')
          await r.srem(f'{Dev_Zaid}DEV', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من Myth🎖️\n☆')
    
    
    
    if text == 'تنزيل مالك اساسي' and m.reply_to_message and m.reply_to_message.from_user:
        if not await gowner_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص (المالك الاساسي وفوق) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention        
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')
        if not await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو مالك اساسي\n☆')
        else:
          await r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من المالك الاساسي\n☆')
    
    if text.startswith('تنزيل مالك اساسي '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await gowner_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص (المالك الاساسي وفوق) بس')
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')
        if not await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو مالك اساسي\n☆')
        else:
          await r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من المالك الاساسي\n☆')
    
    
    if text.startswith('تنزيل مالك '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await gowner_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص ( المالك الاساسي ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')        
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''        
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')        
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')        
        if not await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو مالك من قبل\n☆')
        else:
          await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من المالك \n☆')
    
    if text == 'تنزيل مالك' and m.reply_to_message and m.reply_to_message.from_user:    
        
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention     
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')        
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')        
        if not await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو مالك من قبل\n☆')
        else:
          await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من المالك \n☆')

    if text.startswith('تنزيل مدير '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not await owner_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')
        
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
           
        if not await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو مدير من قبل\n☆')
        else:
          await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من رتبة المدير \n☆')
    
    if text == 'تنزيل مدير' and m.reply_to_message and m.reply_to_message.from_user:
        if not await owner_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')
        
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
           
        if not await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو مدير من قبل\n☆')
        else:
          await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من رتبة المدير \n☆')
    
    if text.startswith('تنزيل ادمن '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not await mod_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if not await r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو ادمن من قبل\n☆')
        else:
          await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من رتبة الادمن \n☆')
    
    if text == 'تنزيل ادمن' and m.reply_to_message and m.reply_to_message.from_user:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if not await r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو ادمن من قبل\n☆')
        else:
          await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من رتبة الادمن \n☆')
    
    if text.startswith('تنزيل مميز '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not await admin_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
        
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if not await r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو مميز من قبل\n☆')
        else:
          await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من المميزين \n☆')
    
    if text == 'تنزيل مميز' and m.reply_to_message and m.reply_to_message.from_user:
        if not await admin_pls(m.from_user.id,m.chat.id):
           return await m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
        if not await r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return await m.reply(f'「 {mention} 」\n{k} مو مميز من قبل\n☆')
        else:
          await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
          return await m.reply(f'「 {mention} 」\n{k} نزلته من المميزين \n☆')
    
    if text.startswith('تنزيل الكل '):
       if not '@' in text and not re.findall('[0-9]+', text):
          return 
       if not await mod_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
       
       if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(f'{k} مافيه عضو بهذا الآيدي')
       
       if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
       if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')
       if await devp_pls(m.from_user.id,m.chat.id):
          rank = await get_rank(id,cid)
          if id == m.from_user.id:
             return await m.reply(f'{k} مافيك تنزل نفسك')
          if not rank == 'عضو' and not id in [6168217372]:
              await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              await r.delete(f'{id}:rankDEV2:{Dev_Zaid}')
              await r.srem(f'{Dev_Zaid}DEV2', id)
              await r.delete(f'{id}:rankDEV:{Dev_Zaid}')
              await r.srem(f'{Dev_Zaid}DEV', id)
              await r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887]:
              return await m.reply(f'{k} مايمديك تستخدم الأمر على مبرمج السورس')
          else:
              return await m.reply(f'{k} ماله رتبة')
       
       if await dev2_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372]:
              await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              await r.delete(f'{id}:rankDEV:{Dev_Zaid}')
              await r.srem(f'{Dev_Zaid}DEV', id)
              await r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')):
              return await m.reply(f'{k} رتبته اعلى منك')
          else:
              return await m.reply(f'{k} ماله رتبة')

       if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
               f'{id}:rankDEV2:{Dev_Zaid}'):
           await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
           await r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
           await r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
           await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
           await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
           await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
           await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
           await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
           await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
           await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
           await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
           return
       if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or not await r.get(
               f'{id}:rankDEV2:{Dev_Zaid}'):
           return await m.reply(f'{k} رتبته اعلى منك')
       else:
           return await m.reply(f'{k} ماله رتبة')
       
       if await gowner_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
              await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') or await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
              return await m.reply(f'{k} رتبته اعلى منك')
          else:
              return await m.reply(f'{k} ماله رتبة')
       
       if await owner_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') or await r.get(f'{id}:rankDEV:{Dev_Zaid}') or await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              return await m.reply(f'{k} رتبته اعلى منك')
          else:
              return await m.reply(f'{k} ماله رتبة')
       
       if await mod_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') or await r.get(f'{id}:rankDEV:{Dev_Zaid}') or await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              return await m.reply(f'{k} رتبته اعلى منك')
          else:
              return await m.reply(f'{k} ماله رتبة')
       
       if await admin_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}') and not await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
              await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') or await r.get(f'{id}:rankDEV:{Dev_Zaid}') or await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}') or await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
              return await m.reply(f'{k} رتبته اعلى منك')
          else:
              return await m.reply(f'{k} ماله رتبة')
    
    
    if text == 'تنزيل الكل' and m.reply_to_message and m.reply_to_message.from_user:
       if not await owner_pls(m.from_user.id,m.chat.id):
          return await m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
       
       id = m.reply_to_message.from_user.id
       mention= m.reply_to_message.from_user.mention
       
       if rank == await get_rank(id, cid):
           return await m.reply('نفس رتبتك ترا')
       if id == int(Dev_Zaid):
           return await m.reply('ركز حبيبي كيف انزل نفسي')
       if await devp_pls(m.from_user.id,m.chat.id):
          rank = await get_rank(id,cid)
          if id == m.from_user.id:
             return await m.reply(f'{k} مافيك تنزل نفسك')
          if not rank == 'عضو' and not id in [6168217372]:
              await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              await r.delete(f'{id}:rankDEV2:{Dev_Zaid}')
              await r.srem(f'{Dev_Zaid}DEV2', id)
              await r.delete(f'{id}:rankDEV:{Dev_Zaid}')
              await r.srem(f'{Dev_Zaid}DEV', id)
              await r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887]:
              return await m.reply(f'{k} مايمديك تستخدم الأمر على مبرمج السورس')
          else:
             return await m.reply(f'{k} ماله رتبة')
       
       if await dev2_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372]:
              await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              await r.delete(f'{id}:rankDEV:{Dev_Zaid}')
              await r.srem(f'{Dev_Zaid}DEV', id)
              await r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')):
              return await m.reply(f'{k} رتبته اعلى منك')
          else:
              return await m.reply(f'{k} ماله رتبة')
       
       if await dev_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}'):
              await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              await r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}'):
              return await m.reply(f'{k} رتبته اعلى منك')
          else:
              return await m.reply(f'{k} ماله رتبة')

       if await gowner_pls(m.from_user.id, m.chat.id):
           rank = await get_rank(id, cid)
           if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [
               6168217372] and not await r.get(f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
               await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
               await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
               await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
               await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
               await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
               await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
               await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
               await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
               await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
               return
           if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or not await r.get(
                   f'{id}:rankDEV2:{Dev_Zaid}') or await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
               return await m.reply(f'{k} رتبته اعلى منك')
           else:
               return await m.reply(f'{k} ماله رتبة')
       
       if await owner_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') or await r.get(f'{id}:rankDEV:{Dev_Zaid}') or await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              return await m.reply(f'{k} رتبته اعلى منك')
          else:
              return await m.reply(f'{k} ماله رتبة')

       if await mod_pls(m.from_user.id, m.chat.id):
           rank = await get_rank(id, cid)
           if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [
               6168217372] and not await r.get(f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(
                   f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}') and not await r.get(
                   f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
               await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
               await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
               await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
               await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
               await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
               return
           if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or not await r.get(
                   f'{id}:rankDEV2:{Dev_Zaid}') or await r.get(f'{id}:rankDEV:{Dev_Zaid}') or await r.get(
                   f'{cid}:rankGOWNER:{id}{Dev_Zaid}') or await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
               return await m.reply(f'{k} رتبته اعلى منك')
           else:
               return await m.reply(f'{k} ماله رتبة')

       if await admin_pls(m.from_user.id, m.chat.id):
           rank = await get_rank(id, cid)
           if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [
               6168217372] and not await r.get(f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(
                   f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}') and not await r.get(
                   f'{cid}:rankOWNER:{id}{Dev_Zaid}') and not await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
               await m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
               await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
               await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
               return
           if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or await r.get(
                   f'{id}:rankDEV2:{Dev_Zaid}') or await r.get(f'{id}:rankDEV:{Dev_Zaid}') or await r.get(
                   f'{cid}:rankGOWNER:{id}{Dev_Zaid}') or await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}') or await r.get(
                   f'{cid}:rankMOD:{id}{Dev_Zaid}'):
               return await m.reply(f'{k} رتبته اعلى منك')
           else:
               return await m.reply(f'{k} ماله رتبة')