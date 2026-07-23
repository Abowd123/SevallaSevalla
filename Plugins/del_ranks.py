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


@Client.on_message(filters.text & filters.group, group=13)
async def delRanksHandler(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    await del_ranks_func(c,m,k)
    

async def del_ranks_func(c,m,k):
   if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return
   if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   
   if await r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return
   if await r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
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
   id = m.from_user.id
   cid = m.chat.id
   demoted = '''{} ابشر عيني {}
{} مسحت ( {} ) من {} 
☆
'''
   if text == 'مسح قائمه Dev':
      if not await devp_pls(id, cid):
        return await m.reply(t('g_d06463beb4', '{0} هذا الامر يخص ( Dev🎖️) بس', k))
      else:
        if not await r.smembers(f'{Dev_Zaid}DEV2'):
          return await m.reply(t('g_69e4f30913', '{0} مافيه قائمة Dev²🎖', k))
        else:
          count = 0
          for dev2 in await r.smembers(f'{Dev_Zaid}DEV2'):
             await r.srem(f'{Dev_Zaid}DEV2', int(dev2))
             await r.delete(f'{int(dev2)}:rankDEV2:{Dev_Zaid}')
             count += 1
          await m.reply(demoted.format(k,await get_rank(id,cid),k,count,'قائمة Dev'))
   
   if text == 'مسح قائمه MY':
      if not await dev2_pls(id, cid):
        return await m.reply(t('g_87098c46e6', '{0} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس', k))
      else:
        if not await r.smembers(f'{Dev_Zaid}DEV'):
          return await m.reply(t('g_ea8715d6b2', '{0} مافيه قائمة Myth🎖️', k))
        else:
          count = 0
          for dev in await r.smembers(f'{Dev_Zaid}DEV'):
             await r.srem(f'{Dev_Zaid}DEV', int(dev))
             await r.delete(f'{int(dev)}:rankDEV:{Dev_Zaid}')
             count += 1
          await m.reply(demoted.format(k,await get_rank(id,cid),k,count,'قائمة MY'))
   
   if text == 'مسح المالكين الاساسيين':
      if not await dev_pls(id, cid):
        return await m.reply(t('g_10ef84eabb', '{0} هذا الامر يخص ( Myth🎖️ مالك القروب وفوق) بس', k))
      else:
        if not await r.smembers(f'{cid}:listGOWNER:{Dev_Zaid}'):
          return await m.reply(t('g_531a942898', '{0} مافيه مالكين اساسيين', k))
        else:
          count = 0
          for gowner in await r.smembers(f'{cid}:listGOWNER:{Dev_Zaid}'):
             await r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', int(gowner))
             await r.delete(f'{cid}:rankGOWNER:{int(gowner)}{Dev_Zaid}')
             count += 1
          await m.reply(demoted.format(k,await get_rank(id,cid),k,count,'المالكين الاساسيين'))
   
   if text == 'مسح المالكين':
      if not await gowner_pls(id, cid):
        return await m.reply(t('g_ae475f0efd', '{0} هذا الأمر يخص ( المالك الاساسي وفوق ) بس', k))
      else:
        if not await r.smembers(f'{cid}:listOWNER:{Dev_Zaid}'):
          return await m.reply(t('g_48df9cf2a7', '{0} مافيه مالكين ', k))
        else:
          count = 0
          for owner in await r.smembers(f'{cid}:listOWNER:{Dev_Zaid}'):
             await r.srem(f'{cid}:listOWNER:{Dev_Zaid}', int(owner))
             await r.delete(f'{cid}:rankOWNER:{int(owner)}{Dev_Zaid}')
             count += 1
          await m.reply(demoted.format(k,await get_rank(id,cid),k,count,'المالكين'))
   
   if text == 'مسح المدراء':
      if not await owner_pls(id, cid):
        return await m.reply(t('g_4a108ff756', '{0} هذا الأمر يخص ( المالك وفوق ) بس', k))
      else:
        if not await r.smembers(f'{cid}:listMOD:{Dev_Zaid}'):
          return await m.reply(t('g_e58a368129', '{0} مافيه مدراء', k))
        else:
          count = 0
          for MOD in await r.smembers(f'{cid}:listMOD:{Dev_Zaid}'):
             await r.srem(f'{cid}:listMOD:{Dev_Zaid}', int(MOD))
             await r.delete(f'{cid}:rankMOD:{int(MOD)}{Dev_Zaid}')
             count += 1
          await m.reply(demoted.format(k,await get_rank(id,cid),k,count,'المدراء'))
   
   if text == 'مسح الادمنيه' or text == 'مسح الادمن':
      if not await mod_pls(id, cid):
        return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
      else:
        if not await r.smembers(f'{cid}:listADMIN:{Dev_Zaid}'):
          return await m.reply(t('g_983057d5b4', '{0} مافيه ادمن', k))
        else:
          count = 0
          for ADM in await r.smembers(f'{cid}:listADMIN:{Dev_Zaid}'):
             await r.srem(f'{cid}:listADMIN:{Dev_Zaid}', int(ADM))
             await r.delete(f'{cid}:rankADMIN:{int(ADM)}{Dev_Zaid}')
             count += 1
          await m.reply(demoted.format(k,await get_rank(id,cid),k,count,'الادمن'))
   
   if text == 'مسح المميزين':
      if not await mod_pls(id, cid):
        return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
      else:
        if not await r.smembers(f'{cid}:listPRE:{Dev_Zaid}'):
          return await m.reply(t('g_3a33becf02', '{0} مافيه مميزين', k))
        else:
          count = 0
          for MOD in await r.smembers(f'{cid}:listPRE:{Dev_Zaid}'):
             await r.srem(f'{cid}:listPRE:{Dev_Zaid}', int(MOD))
             await r.delete(f'{cid}:rankPRE:{int(MOD)}{Dev_Zaid}')
             count += 1
          await m.reply(demoted.format(k,await get_rank(id,cid),k,count,'المميزين'))
   
   if text == 'مسح المكتومين':
      if not await mod_pls(id, cid):
        return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
      else:
        if not await r.smembers(f'{cid}:listMUTE:{Dev_Zaid}'):
          return await m.reply(t('g_9a7eb39ce7', '{0} مافيه مكتومين', k))
        else:
          count = 0
          for MOD in await r.smembers(f'{cid}:listMUTE:{Dev_Zaid}'):
             try:
               mod = int(MOD)
             except Exception:
               mod = MOD
             await r.srem(f'{cid}:listMUTE:{Dev_Zaid}', mod)
             await r.delete(f'{mod}:mute:{cid}{Dev_Zaid}')
             count += 1
          await m.reply(demoted.format(k,await get_rank(id,cid),k,count,'المكتومين'))
   
   if text == 'مسح المكتومين عام':
      if not await dev_pls(id, cid):
        return await m.reply(t('g_68bb86e6c6', '{0} هذا الامر يخص ( Myth🎖️ وفوق ) بس', k))
      else:
        if not await r.smembers(f'listMUTE:{Dev_Zaid}'):
          return await m.reply(t('g_513d75c85d', '{0} مافيه مكتومين عام', k))
        else:
          count = 0
          for MOD in await r.smembers(f'listMUTE:{Dev_Zaid}'):
             await r.srem(f'listMUTE:{Dev_Zaid}', int(MOD))
             await r.delete(f'{int(MOD)}:mute:{Dev_Zaid}')
             count += 1
          await m.reply(demoted.format(k,await get_rank(id,cid),k,count,'المكتومين عام'))
   
   if text == 'مسح المحظورين عام':
      if not await dev_pls(id, cid):
        return await m.reply(t('g_68bb86e6c6', '{0} هذا الامر يخص ( Myth🎖️ وفوق ) بس', k))
      else:
        if not await r.smembers(f'listGBAN:{Dev_Zaid}'):
          return await m.reply(t('g_33944c2cf1', '{0} مافيه حمير محظورين', k))
        else:
          count = 0
          for MOD in await r.smembers(f'listGBAN:{Dev_Zaid}'):
             await r.srem(f'listGBAN:{Dev_Zaid}', int(MOD))
             await r.delete(f'{int(MOD)}:gban:{Dev_Zaid}')
             count += 1
          await m.reply(demoted.format(k,await get_rank(id,cid),k,count,'الحمير المحظورين عام'))
          
             
       
   
   
