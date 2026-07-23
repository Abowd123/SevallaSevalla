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
        return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
      else:
        if await r.get(f'{m.chat.id}:disableRanks:{Dev_Zaid}'):
          return await m.reply(t('g_c8d1335edc', '{0} من「 {1} 」\n{2} الرفع معطل من قبل\n☆', k, m.from_user.mention, k))
        else:
          await r.set(f'{m.chat.id}:disableRanks:{Dev_Zaid}', 1)
          return await m.reply(t('g_c1d38bede0', '{0} من「 {1} 」\n{2} ابشر عطلت الرفع\n☆', k, m.from_user.mention, k))
    
    if text == 'تفعيل الرفع':
      if not await owner_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
      else:
        if not await r.get(f'{m.chat.id}:disableRanks:{Dev_Zaid}'):
          return await m.reply(t('g_1fd1a94c79', '「 {0} 」\n{1} الرفع مفعل من قبل\n☆', m.from_user.mention, k))
        else:
          await r.delete(f'{m.chat.id}:disableRanks:{Dev_Zaid}')
          return await m.reply(t('g_c1bcf0939a', '{0} من「 {1} 」\n{2} ابشر فعلت الرفع\n☆', k, m.from_user.mention, k))
    
    cid = m.chat.id
    
    if await r.get(f'{m.chat.id}:disableRanks:{Dev_Zaid}'):  return
    rank = await get_rank(m.from_user.id, m.chat.id)
    if text.startswith('رفع Dev '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await devp_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_d06463beb4', '{0} هذا الامر يخص ( Dev🎖️) بس', k))
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        
           
        if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return await m.reply(t('g_5c9e27517a', '「 {0} 」\n{1} Dev²🎖 من قبل\n☆', mention, k))
        else:
          await r.set(f'{id}:rankDEV2:{Dev_Zaid}', 1)
          await r.sadd(f'{Dev_Zaid}DEV2', id)
          return await m.reply(t('g_829dd3963f', '{0} الحلو 「 {1} 」\n{2} رفعته صار Dev²🎖\n☆', k, mention, k))
          if await r.get(f'{id}:mute:{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{Dev_Zaid}')
            await r.srem(f'listMUTE:{Dev_Zaid}', id)
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع Dev' and m.reply_to_message and m.reply_to_message.from_user:
        if not await devp_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_d06463beb4', '{0} هذا الامر يخص ( Dev🎖️) بس', k))
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))        
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))           
        if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return await m.reply(t('g_5c9e27517a', '「 {0} 」\n{1} Dev²🎖 من قبل\n☆', mention, k))
        else:
          await r.set(f'{id}:rankDEV2:{Dev_Zaid}', 1)
          await r.sadd(f'{Dev_Zaid}DEV2', id)
          return await m.reply(t('g_829dd3963f', '{0} الحلو 「 {1} 」\n{2} رفعته صار Dev²🎖\n☆', k, mention, k))
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
           return await m.reply(t('g_2d0da46fab', '{0} هذا الامر يخص ( Dev²🎖️ وفوق ) بس', k))
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return await m.reply(t('g_b9af552aa8', '「 {0} 」\n{1} Myth🎖️ من قبل\n☆', mention, k))
        else:
          await r.set(f'{id}:rankDEV:{Dev_Zaid}', 1)
          await r.sadd(f'{Dev_Zaid}DEV', id)
          await m.reply(t('g_86011969b5', '{0} الحلو 「 {1} 」\n{2} رفعته صار Myth🎖️\n☆', k, mention, k))
          if await r.get(f'{id}:mute:{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{Dev_Zaid}')
            await r.srem(f'listMUTE:{Dev_Zaid}', id)
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع MY' and m.reply_to_message and m.reply_to_message.from_user:
        if not await dev2_pls(m.from_user.id,m.chat.id):
           return await m.reply(t('g_2d0da46fab', '{0} هذا الامر يخص ( Dev²🎖️ وفوق ) بس', k))
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))        
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return await m.reply(t('g_b9af552aa8', '「 {0} 」\n{1} Myth🎖️ من قبل\n☆', mention, k))
        else:
          await r.set(f'{id}:rankDEV:{Dev_Zaid}', 1)
          await r.sadd(f'{Dev_Zaid}DEV', id)
          await m.reply(t('g_86011969b5', '{0} الحلو 「 {1} 」\n{2} رفعته صار Myth🎖️\n☆', k, mention, k))
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
          return await m.reply(t('g_db1ebb0f5c', '{0} هذا الامر يخص ( المالك الاساسي وفوق ) بس', k))
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))           
        if await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return await m.reply(t('g_a94d894974', '「 {0} 」\n{1} مالك اساسي من قبل\n☆', mention, k))
        else:
          await r.set(f'{cid}:rankGOWNER:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          await m.reply(t('g_889c1333c1', '{0} الحلو 「 {1} 」\n{2} رفعته صار مالك اساسي\n☆', k, mention, k))
          if await r.get(f'{id}:mute:{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{Dev_Zaid}')
            await r.srem(f'listMUTE:{Dev_Zaid}', id)
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
          return 
    
    if text == 'رفع مالك اساسي' and m.reply_to_message and m.reply_to_message.from_user:
        if not await gowner_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_a89f267049', '{0} هذا الامر يخص (المالك الاساسي وفوق) بس', k))
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention       
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))           
        if await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return await m.reply(t('g_a94d894974', '「 {0} 」\n{1} مالك اساسي من قبل\n☆', mention, k))
        else:
          await r.set(f'{cid}:rankGOWNER:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          await m.reply(t('g_889c1333c1', '{0} الحلو 「 {1} 」\n{2} رفعته صار مالك اساسي\n☆', k, mention, k))
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
          return await m.reply(t('g_aa2b0014e0', '{0} هذا الامر يخص ( المالك الاساسي ) بس', k))
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return await m.reply(t('g_6b6e9e6087', '「 {0} 」\n{1} مالك من قبل\n☆', mention, k))
        else:
          await r.set(f'{cid}:rankOWNER:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listOWNER:{Dev_Zaid}', id)
          await m.reply(t('g_06dbadaa84', '{0} الحلو 「 {1} 」\n{2} رفعته صار مالك\n☆', k, mention, k))
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع مالك' and m.reply_to_message and m.reply_to_message.from_user:
        if not await gowner_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_aa2b0014e0', '{0} هذا الامر يخص ( المالك الاساسي ) بس', k))
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return await m.reply(t('g_6b6e9e6087', '「 {0} 」\n{1} مالك من قبل\n☆', mention, k))
        else:
          await r.set(f'{cid}:rankOWNER:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listOWNER:{Dev_Zaid}', id)
          await m.reply(t('g_06dbadaa84', '{0} الحلو 「 {1} 」\n{2} رفعته صار مالك\n☆', k, mention, k))
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    
    if text.startswith('رفع مدير '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await owner_pls(m.from_user.id,m.chat.id):
           return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))           
        if await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return await m.reply(t('g_42b9731ec3', '「 {0} 」\n{1} مدير من قبل\n☆', mention, k))
        else:
          await r.set(f'{cid}:rankMOD:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listMOD:{Dev_Zaid}', id)
          await m.reply(t('g_806eac6208', '{0} الحلو 「 {1} 」\n{2} رفعته صار مدير\n☆', k, mention, k))
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع مدير' and m.reply_to_message and m.reply_to_message.from_user:
        if not await owner_pls(m.from_user.id,m.chat.id):
           return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))           
        if await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return await m.reply(t('g_42b9731ec3', '「 {0} 」\n{1} مدير من قبل\n☆', mention, k))
        else:
          await r.set(f'{cid}:rankMOD:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listMOD:{Dev_Zaid}', id)
          await m.reply(t('g_806eac6208', '{0} الحلو 「 {1} 」\n{2} رفعته صار مدير\n☆', k, mention, k))
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text.startswith('رفع ادمن '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await mod_pls(m.from_user.id,m.chat.id):
           return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
           
        if await r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return await m.reply(t('g_6c1a6ae809', '「 {0} 」\n{1} ادمن من قبل\n☆', mention, k))
        else:
          await r.set(f'{cid}:rankADMIN:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listADMIN:{Dev_Zaid}', id)
          await m.reply(t('g_3a563daaad', '{0} الحلو 「 {1} 」\n{2} رفعته صار ادمن\n☆', k, mention, k))
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع ادمن' and m.reply_to_message and m.reply_to_message.from_user:        
        if not await mod_pls(m.from_user.id,m.chat.id):
           return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
           
        if await r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return await m.reply(t('g_6c1a6ae809', '「 {0} 」\n{1} ادمن من قبل\n☆', mention, k))
        else:
          await r.set(f'{cid}:rankADMIN:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listADMIN:{Dev_Zaid}', id)
          await m.reply(t('g_3a563daaad', '{0} الحلو 「 {1} 」\n{2} رفعته صار ادمن\n☆', k, mention, k))
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text.startswith('رفع مميز '):
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not await admin_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
      else:
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if await r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return await m.reply(t('g_e400bde8aa', '「 {0} 」\n{1} مميز من قبل\n☆', mention, k))
        else:
          await r.set(f'{cid}:rankPRE:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listPRE:{Dev_Zaid}', id)
          await m.reply(t('g_0c9f6fa3ef', '{0} الحلو 「 {1} 」\n{2} رفعته صار مميز\n☆', k, mention, k))
          if await r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            await r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            await r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع مميز' and m.reply_to_message and m.reply_to_message.from_user:
      if not await admin_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
      else:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply(t('g_36dbf38a47', 'ركز حبيبي كيف ارفع نفسي'))
        if id == m.from_user.id:
           return await m.reply(t('g_9d9d6762b3', '{0} هطف تبي ترفع نفسك؟', k))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if await r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return await m.reply(t('g_e400bde8aa', '「 {0} 」\n{1} مميز من قبل\n☆', mention, k))
        else:
          await r.set(f'{cid}:rankPRE:{id}{Dev_Zaid}', 1)
          await r.sadd(f'{cid}:listPRE:{Dev_Zaid}', id)
          await m.reply(t('g_0c9f6fa3ef', '{0} الحلو 「 {1} 」\n{2} رفعته صار مميز\n☆', k, mention, k))
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
           return await m.reply(t('g_d06463beb4', '{0} هذا الامر يخص ( Dev🎖️) بس', k))
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention     
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))           
        if not await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return await m.reply(t('g_870d93cbec', '「 {0} 」\n{1} مو Dev²🎖\n☆', mention, k))
        else:
          await r.delete(f'{id}:rankDEV2:{Dev_Zaid}')
          await r.srem(f'{Dev_Zaid}DEV2', id)
          return await m.reply(t('g_b1f29d2d97', '「 {0} 」\n{1} نزلته من Dev²🎖\n☆', mention, k))
    
    if text.startswith('تنزيل Dev '):
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not await devp_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_d06463beb4', '{0} هذا الامر يخص ( Dev🎖️) بس', k))
      else:
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))           
        if not await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return await m.reply(t('g_870d93cbec', '「 {0} 」\n{1} مو Dev²🎖\n☆', mention, k))
        else:
          await r.delete(f'{id}:rankDEV2:{Dev_Zaid}')
          await r.srem(f'{Dev_Zaid}DEV2', id)
          return await m.reply(t('g_b1f29d2d97', '「 {0} 」\n{1} نزلته من Dev²🎖\n☆', mention, k))
          
    if text == 'تنزيل MY'  and m.reply_to_message and m.reply_to_message.from_user:
        if not await dev2_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_2d0da46fab', '{0} هذا الامر يخص ( Dev²🎖️ وفوق ) بس', k))
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))        
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))           
        if not await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return await m.reply(t('g_c6b8e3159b', '「 {0} 」\n{1} مو Myth🎖️ من قبل\n☆', mention, k))
        else:
          await r.delete(f'{id}:rankDEV:{Dev_Zaid}')
          await r.srem(f'{Dev_Zaid}DEV', id)
          return await m.reply(t('g_b26ba9b09d', '「 {0} 」\n{1} نزلته من Myth🎖️\n☆', mention, k))
    
    if text.startswith('تنزيل MY '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await dev2_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_2d0da46fab', '{0} هذا الامر يخص ( Dev²🎖️ وفوق ) بس', k))
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))
        
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
           
        if not await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return await m.reply(t('g_c6b8e3159b', '「 {0} 」\n{1} مو Myth🎖️ من قبل\n☆', mention, k))
        else:
          await r.delete(f'{id}:rankDEV:{Dev_Zaid}')
          await r.srem(f'{Dev_Zaid}DEV', id)
          return await m.reply(t('g_b26ba9b09d', '「 {0} 」\n{1} نزلته من Myth🎖️\n☆', mention, k))
    
    
    
    if text == 'تنزيل مالك اساسي' and m.reply_to_message and m.reply_to_message.from_user:
        if not await gowner_pls(m.from_user.id,m.chat.id):
           return await m.reply(t('g_a89f267049', '{0} هذا الامر يخص (المالك الاساسي وفوق) بس', k))
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention        
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))
        if not await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return await m.reply(t('g_e53546a10d', '「 {0} 」\n{1} مو مالك اساسي\n☆', mention, k))
        else:
          await r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          return await m.reply(t('g_c924fc24b0', '「 {0} 」\n{1} نزلته من المالك الاساسي\n☆', mention, k))
    
    if text.startswith('تنزيل مالك اساسي '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await gowner_pls(m.from_user.id,m.chat.id):
           return await m.reply(t('g_a89f267049', '{0} هذا الامر يخص (المالك الاساسي وفوق) بس', k))
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))
        if not await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return await m.reply(t('g_e53546a10d', '「 {0} 」\n{1} مو مالك اساسي\n☆', mention, k))
        else:
          await r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          return await m.reply(t('g_c924fc24b0', '「 {0} 」\n{1} نزلته من المالك الاساسي\n☆', mention, k))
    
    
    if text.startswith('تنزيل مالك '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not await gowner_pls(m.from_user.id,m.chat.id):
           return await m.reply(t('g_aa2b0014e0', '{0} هذا الامر يخص ( المالك الاساسي ) بس', k))
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))        
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''        
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))        
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))        
        if not await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return await m.reply(t('g_88f11bbcce', '「 {0} 」\n{1} مو مالك من قبل\n☆', mention, k))
        else:
          await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
          return await m.reply(t('g_d20f15a2c7', '「 {0} 」\n{1} نزلته من المالك \n☆', mention, k))
    
    if text == 'تنزيل مالك' and m.reply_to_message and m.reply_to_message.from_user:    
        
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention     
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))        
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))        
        if not await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return await m.reply(t('g_88f11bbcce', '「 {0} 」\n{1} مو مالك من قبل\n☆', mention, k))
        else:
          await r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
          return await m.reply(t('g_d20f15a2c7', '「 {0} 」\n{1} نزلته من المالك \n☆', mention, k))

    if text.startswith('تنزيل مدير '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not await owner_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))
        
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
           
        if not await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return await m.reply(t('g_1e9f7ed68a', '「 {0} 」\n{1} مو مدير من قبل\n☆', mention, k))
        else:
          await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
          return await m.reply(t('g_d97b9e8e28', '「 {0} 」\n{1} نزلته من رتبة المدير \n☆', mention, k))
    
    if text == 'تنزيل مدير' and m.reply_to_message and m.reply_to_message.from_user:
        if not await owner_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))
        
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
           
        if not await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return await m.reply(t('g_1e9f7ed68a', '「 {0} 」\n{1} مو مدير من قبل\n☆', mention, k))
        else:
          await r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
          return await m.reply(t('g_d97b9e8e28', '「 {0} 」\n{1} نزلته من رتبة المدير \n☆', mention, k))
    
    if text.startswith('تنزيل ادمن '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not await mod_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if not await r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return await m.reply(t('g_c91c36701c', '「 {0} 」\n{1} مو ادمن من قبل\n☆', mention, k))
        else:
          await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
          return await m.reply(t('g_26c9f64dd9', '「 {0} 」\n{1} نزلته من رتبة الادمن \n☆', mention, k))
    
    if text == 'تنزيل ادمن' and m.reply_to_message and m.reply_to_message.from_user:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if not await r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return await m.reply(t('g_c91c36701c', '「 {0} 」\n{1} مو ادمن من قبل\n☆', mention, k))
        else:
          await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
          return await m.reply(t('g_26c9f64dd9', '「 {0} 」\n{1} نزلته من رتبة الادمن \n☆', mention, k))
    
    if text.startswith('تنزيل مميز '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not await admin_pls(m.from_user.id,m.chat.id):
           return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
        
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if not await r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return await m.reply(t('g_c6de30fb09', '「 {0} 」\n{1} مو مميز من قبل\n☆', mention, k))
        else:
          await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
          return await m.reply(t('g_5fb7617d6c', '「 {0} 」\n{1} نزلته من المميزين \n☆', mention, k))
    
    if text == 'تنزيل مميز' and m.reply_to_message and m.reply_to_message.from_user:
        if not await admin_pls(m.from_user.id,m.chat.id):
           return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))
        if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
        if not await r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return await m.reply(t('g_c6de30fb09', '「 {0} 」\n{1} مو مميز من قبل\n☆', mention, k))
        else:
          await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
          await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
          return await m.reply(t('g_5fb7617d6c', '「 {0} 」\n{1} نزلته من المميزين \n☆', mention, k))
    
    if text.startswith('تنزيل الكل '):
       if not '@' in text and not re.findall('[0-9]+', text):
          return 
       if not await mod_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
       
       if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = await c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_06f49e9528', '{0} مافيه عضو بهذا اليوزر', k))
           else:
              try:
                 get = await c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except Exception:
                 return await m.reply(t('g_8f8455f6e7', '{0} مافيه عضو بهذا الآيدي', k))
       
       if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
       if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))
       if await devp_pls(m.from_user.id,m.chat.id):
          rank = await get_rank(id,cid)
          if id == m.from_user.id:
             return await m.reply(t('g_9d256dbe6c', '{0} مافيك تنزل نفسك', k))
          if not rank == 'عضو' and not id in [6168217372]:
              await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
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
              return await m.reply(t('g_dbd0ab4ab0', '{0} مايمديك تستخدم الأمر على مبرمج السورس', k))
          else:
              return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))
       
       if await dev2_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372]:
              await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
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
              return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
          else:
              return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))

       if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
               f'{id}:rankDEV2:{Dev_Zaid}'):
           await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
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
           return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
       else:
           return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))
       
       if await gowner_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
              await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
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
              return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
          else:
              return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))
       
       if await owner_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
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
              return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
          else:
              return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))
       
       if await mod_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
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
              return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
          else:
              return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))
       
       if await admin_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}') and not await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
              await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
              await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') or await r.get(f'{id}:rankDEV:{Dev_Zaid}') or await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}') or await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
              return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
          else:
              return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))
    
    
    if text == 'تنزيل الكل' and m.reply_to_message and m.reply_to_message.from_user:
       if not await owner_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
       
       id = m.reply_to_message.from_user.id
       mention= m.reply_to_message.from_user.mention
       
       if rank == await get_rank(id, cid):
           return await m.reply(t('g_865a3247b8', 'نفس رتبتك ترا'))
       if id == int(Dev_Zaid):
           return await m.reply(t('g_7e38b4205e', 'ركز حبيبي كيف انزل نفسي'))
       if await devp_pls(m.from_user.id,m.chat.id):
          rank = await get_rank(id,cid)
          if id == m.from_user.id:
             return await m.reply(t('g_9d256dbe6c', '{0} مافيك تنزل نفسك', k))
          if not rank == 'عضو' and not id in [6168217372]:
              await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
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
              return await m.reply(t('g_dbd0ab4ab0', '{0} مايمديك تستخدم الأمر على مبرمج السورس', k))
          else:
             return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))
       
       if await dev2_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372]:
              await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
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
              return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
          else:
              return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))
       
       if await dev_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}'):
              await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
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
              return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
          else:
              return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))

       if await gowner_pls(m.from_user.id, m.chat.id):
           rank = await get_rank(id, cid)
           if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [
               6168217372] and not await r.get(f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
               await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
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
               return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
           else:
               return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))
       
       if await owner_pls(m.from_user.id, m.chat.id):
          rank = await get_rank(id,cid)
          if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not await r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
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
              return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
          else:
              return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))

       if await mod_pls(m.from_user.id, m.chat.id):
           rank = await get_rank(id, cid)
           if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [
               6168217372] and not await r.get(f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(
                   f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}') and not await r.get(
                   f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
               await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
               await r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
               await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
               await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
               await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
               return
           if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or not await r.get(
                   f'{id}:rankDEV2:{Dev_Zaid}') or await r.get(f'{id}:rankDEV:{Dev_Zaid}') or await r.get(
                   f'{cid}:rankGOWNER:{id}{Dev_Zaid}') or await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
               return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
           else:
               return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))

       if await admin_pls(m.from_user.id, m.chat.id):
           rank = await get_rank(id, cid)
           if not rank == 'عضو' and not id == int(await r.get(f'{Dev_Zaid}botowner')) and not id in [
               6168217372] and not await r.get(f'{id}:rankDEV2:{Dev_Zaid}') and not await r.get(
                   f'{id}:rankDEV:{Dev_Zaid}') and not await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}') and not await r.get(
                   f'{cid}:rankOWNER:{id}{Dev_Zaid}') and not await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
               await m.reply(t('g_9b93ecaee5', '「 {0} 」\n{1} نزلته من {2} \n☆', mention, k, rank))
               await r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
               await r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
               return
           if id in [6168217372, 5117901887] or id == int(await r.get(f'{Dev_Zaid}botowner')) or await r.get(
                   f'{id}:rankDEV2:{Dev_Zaid}') or await r.get(f'{id}:rankDEV:{Dev_Zaid}') or await r.get(
                   f'{cid}:rankGOWNER:{id}{Dev_Zaid}') or await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}') or await r.get(
                   f'{cid}:rankMOD:{id}{Dev_Zaid}'):
               return await m.reply(t('g_ba17565345', '{0} رتبته اعلى منك', k))
           else:
               return await m.reply(t('g_d7c80ccd5e', '{0} ماله رتبة', k))