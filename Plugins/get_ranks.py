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

@Client.on_message(filters.text & filters.group, group=12)
async def getRanksHandler(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    channel = await r.get(f'{Dev_Zaid}:BotChannel') or 'yqyqy66'
    await get_ranks_func(c,m,k,channel)
    
async def get_ranks_func(c,m,k,channel):
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
   if text == 'قائمه Dev':
      if not await devp_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_d06463beb4', '{0} هذا الامر يخص ( Dev🎖️) بس', k))
      else:
        if not await r.smembers(f'{Dev_Zaid}DEV2'):
           return await m.reply(t('g_506d17355a', '{0} مافيه قائمة  Dev²🎖️', k))
        else:
          text = '- قائمة  Dev²🎖:\n\n'
          count = 1
          for dev2 in await r.smembers(f'{Dev_Zaid}DEV2'):
             if count == 101: break
             try:
               user = await c.get_users(int(dev2))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except Exception:
               mention = f'[@{channel}](tg://user?id={int(dev2)})'
               id = int(dev2)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          await m.reply(text)
   
   if text == 'قائمه MY':
      if not await dev2_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_2d0da46fab', '{0} هذا الامر يخص ( Dev²🎖️ وفوق ) بس', k))
      else:
        if not await r.smembers(f'{Dev_Zaid}DEV'):
          return await m.reply(t('g_d14d1150b2', '{0}  مافيه Myth🎖️ ', k))
        else:
          text = '- قائمة Myth🎖️:\n\n'
          count = 1
          for dev in await r.smembers(f'{Dev_Zaid}DEV'):
             if count == 101: break
             try:
               user = await c.get_users(int(dev))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except Exception:
               mention = f'[@{channel}](tg://user?id={int(dev)})'
               id = int(dev)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          await m.reply(text)
          
   cid = m.chat.id
   if text == 'المالكين الاساسيين':
      if not await dev_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_33cf211beb', '{0} هذا الامر يخص ( المطور وفوق ) بس', k))
      else:
        if not await r.smembers(f'{cid}:listGOWNER:{Dev_Zaid}'):
          return await m.reply(t('g_ca2842eaae', '{0} مافيه مالكين اساسيين ', k))
        else:
          text = '- المالكين الاساسيين:\n\n'
          count = 1
          for gowner in await r.smembers(f'{cid}:listGOWNER:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = await c.get_users(int(gowner))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except Exception:
               mention = f'[@{channel}](tg://user?id={int(gowner)})'
               id = int(gowner)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          await m.reply(text)
          
   if text == 'المالكين':
      if not await gowner_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_aa2b0014e0', '{0} هذا الامر يخص ( المالك الاساسي ) بس', k))
      else:
        if not await r.smembers(f'{cid}:listOWNER:{Dev_Zaid}'):
          return await m.reply(t('g_e6ce10be3b', '{0} مافيه مالكيين ', k))
        else:
          text = '- المالكيين:\n\n'
          count = 1
          for owner in await r.smembers(f'{cid}:listOWNER:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = await c.get_users(int(owner))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except Exception:
               mention = f'[@{channel}](tg://user?id={int(owner)})'
               id = int(owner)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          await m.reply(text)
   
   if text == 'المدراء':
      if not await owner_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
      else:
        if not await r.smembers(f'{cid}:listMOD:{Dev_Zaid}'):
          return await m.reply(t('g_1159ef7f2c', '{0} مافيه مدراء ', k))
        else:
          text = '- المدراء:\n\n'
          count = 1
          for mod in await r.smembers(f'{cid}:listMOD:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = await c.get_users(int(mod))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except Exception:
               mention = f'[@{channel}](tg://user?id={int(mod)})'
               id = int(mod)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          await m.reply(text)
   
   if text == 'الادمنيه':
      if not await mod_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
      else:
        if not await r.smembers(f'{cid}:listADMIN:{Dev_Zaid}'):
          return await m.reply(t('g_d39210a2d1', '{0} مافيه ادمن ', k))
        else:
          text = '- الادمنيه:\n\n'
          count = 1
          for ADM in await r.smembers(f'{cid}:listADMIN:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = await c.get_users(int(ADM))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except Exception:
               mention = f'[@{channel}](tg://user?id={int(ADM)})'
               id = int(ADM)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          await m.reply(text)
   
   if text == 'المشرفين':
      if not await owner_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k))
      else:
          text = '- المشرفين:\n\n'
          count = 1
          for mm in await m.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
            if count == 101: break
            if not mm.user.is_deleted and not mm.user.is_bot:
               id = mm.user.id
               username = mm.user.username
               if mm.user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ [@{channel}](tg://user?id={id}) ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          await m.reply(text)
   
   if text == 'المميزين':
      if not await admin_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_8bb879faee', '{0} هذا الامر يخص ( الادمن وفوق ) بس', k))
      else:
        if not await r.smembers(f'{cid}:listPRE:{Dev_Zaid}'):
          return await m.reply(t('g_5fa1935022', '{0} مافيه مميزين ', k))
        else:
          text = '- المميزين:\n\n'
          count = 1
          for PRE in await r.smembers(f'{cid}:listPRE:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = await c.get_users(int(PRE))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except Exception:
               mention = f'[@{channel}](tg://user?id={int(PRE)})'
               id = int(PRE)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          await m.reply(text)
   
   if text == 'المكتومين':
      if not await mod_pls(m.from_user.id,m.chat.id):
        return await m.reply(t('g_ab8da5b9b9', '{0} هذا الامر يخص ( المدير وفوق ) بس', k))
      else:
        if not await r.smembers(f'{cid}:listMUTE:{Dev_Zaid}'):
          return await m.reply(t('g_877c7bb23a', '{0} مافيه مكتومين ', k))
        else:
          text = '- المكتومين:\n\n'
          count = 1
          for PRE in await r.smembers(f'{cid}:listMUTE:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = await c.get_users(int(PRE))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except Exception:
               mention = f'[@{channel}](tg://user?id={PRE})'
               id = PRE
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          await m.reply(text)
   
   

             
        
        