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


@Client.on_message(filters.text & filters.group, group=35)
async def customrankHandler(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    channel = await r.get(f'{Dev_Zaid}:BotChannel') or 'yqyqy66'
    await customRankFunc(c,m,k,channel)
    
async def customRankFunc(c,m,k,channel):
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
   if text == 'الغاء':
     if await r.get(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}') or await r.get(f'{m.from_user.id}:addRank:{m.chat.id}{Dev_Zaid}') or await r.get(f'{m.from_user.id}:delRank:{m.chat.id}{Dev_Zaid}'):
        await m.reply(t('g_afe187aa48', '{0} من عيوني لغيت كل شي يخص الرتب', k))
        await r.delete(f'{m.from_user.id}:addRank:{m.chat.id}{Dev_Zaid}')
        await r.delete(f'{m.from_user.id}:delRank:{m.chat.id}{Dev_Zaid}')
        await r.delete(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}')
   
   if await r.get(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}') and await mod_pls(m.from_user.id,m.chat.id) and len(m.text) <= 20:
     rank = await r.get(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}')
     await r.delete(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}')
     if rank == 'مالك اساسي':
       if await r.get(f'{m.chat.id}:RankGowner:{Dev_Zaid}'):
         rrr = await r.get(f'{m.chat.id}:RankGowner:{Dev_Zaid}')
         await r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         await r.delete(f'{m.chat.id}:RankGowner:{Dev_Zaid}')
       await r.set(f'{m.chat.id}:RankGowner:{Dev_Zaid}',m.text)
     if rank == 'مالك':
       if await r.get(f'{m.chat.id}:RankOwner:{Dev_Zaid}'):
         rrr = await r.get(f'{m.chat.id}:RankOwner:{Dev_Zaid}')
         await r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         await r.delete(f'{m.chat.id}:RankOwner:{Dev_Zaid}')
       await r.set(f'{m.chat.id}:RankOwner:{Dev_Zaid}',m.text)
     if rank == 'مدير':
       if await r.get(f'{m.chat.id}:RankMod:{Dev_Zaid}'):
         rrr = await r.get(f'{m.chat.id}:RankMod:{Dev_Zaid}')
         await r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         await r.delete(f'{m.chat.id}:RankMod:{Dev_Zaid}')     
       await r.set(f'{m.chat.id}:RankMod:{Dev_Zaid}',m.text)
     if rank == 'ادمن':
       if await r.get(f'{m.chat.id}:RankAdm:{Dev_Zaid}'):
         rrr = await r.get(f'{m.chat.id}:RankAdm:{Dev_Zaid}')
         await r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         await r.delete(f'{m.chat.id}:RankAdm:{Dev_Zaid}')     
       await r.set(f'{m.chat.id}:RankAdm:{Dev_Zaid}',m.text)
     if rank == 'مميز':
       if await r.get(f'{m.chat.id}:RankPre:{Dev_Zaid}'):
         rrr = await r.get(f'{m.chat.id}:RankPre:{Dev_Zaid}')
         await r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         await r.delete(f'{m.chat.id}:RankPre:{Dev_Zaid}')     
       await r.set(f'{m.chat.id}:RankPre:{Dev_Zaid}',m.text)
     if rank == 'عضو':
       if await r.get(f'{m.chat.id}:RankMem:{Dev_Zaid}'):
         rrr = await r.get(f'{m.chat.id}:RankMem:{Dev_Zaid}')
         await r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         await r.delete(f'{m.chat.id}:RankMem:{Dev_Zaid}')     
       await r.set(f'{m.chat.id}:RankMem:{Dev_Zaid}',m.text)
     await r.sadd(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={m.text}')  
     return await m.reply(t('g_82a94dab62', '{0} تم غيرت الرتبه الى ( {1} )', k, m.text))
       
   
   if await r.get(f'{m.from_user.id}:addRank:{m.chat.id}{Dev_Zaid}') and await mod_pls(m.from_user.id,m.chat.id):
     await r.delete(f'{m.from_user.id}:addRank:{m.chat.id}{Dev_Zaid}')
     if not m.text in ['مالك اساسي','مالك','مدير','ادمن','مميز','عضو']:
       return await m.reply(t('g_4df992f587', '{0} ركز! الرتبه اللي كتبتها مو موجوده', k))
     else:
       await r.set(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}',m.text,ex=600)
       return await m.reply(t('g_f32e80bbc1', '{0} حلو الحين ارسل الرتبه الجديدة', k))
   
   if await r.get(f'{m.from_user.id}:delRank:{m.chat.id}{Dev_Zaid}') and await mod_pls(m.from_user.id,m.chat.id):
     await r.delete(f'{m.from_user.id}:delRank:{m.chat.id}{Dev_Zaid}')
     if not m.text in ['مالك اساسي','مالك','مدير','ادمن','مميز','عضو']:
       return await m.reply(t('g_d1ed250677', '{0} مافي رتبه زي كذا لازم تكتب الرتبه الاساسيه مثال مالك اساسي مو {1}', k, m.text[:20]))
     else:
       rank = m.text
       if rank == 'مالك اساسي':
         rank2 = await r.get(f'{m.chat.id}:RankGowner:{Dev_Zaid}')
         await r.delete(f'{m.chat.id}:RankGowner:{Dev_Zaid}')
       if rank == 'مالك':
         rank2 = await r.get(f'{m.chat.id}:RankOwner:{Dev_Zaid}')
         await r.delete(f'{m.chat.id}:RankOwner:{Dev_Zaid}')
       if rank == 'مدير':
         rank2 = await r.get(f'{m.chat.id}:RankMod:{Dev_Zaid}')
         await r.delete(f'{m.chat.id}:RankMod:{Dev_Zaid}')
       if rank == 'ادمن':
         rank2 = await r.get(f'{m.chat.id}:RankAdm:{Dev_Zaid}')
         await r.delete(f'{m.chat.id}:RankAdm:{Dev_Zaid}')
       if rank == 'مميز':
         rank2 = await r.get(f'{m.chat.id}:RankPre:{Dev_Zaid}')
         await r.delete(f'{m.chat.id}:RankPre:{Dev_Zaid}')
       if rank == 'عضو':
         rank2 = await r.get(f'{m.chat.id}:RankMem:{Dev_Zaid}')
         await r.delete(f'{m.chat.id}:RankMem:{Dev_Zaid}')
       await r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rank2}')
       return await m.reply(t('g_76488a076e', '{0} مسحت رتبه ( {1} )', k, rank2))
   
   if text == 'مسح الرتب':
     if not await mod_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
     else:
       if not await r.smembers(f'{m.chat.id}:ranklist:{Dev_Zaid}'):
         return await m.reply(t('g_b6582caddb', '{0} مافيه رتب مضافة', k))
       else:
         await m.reply(t('g_4bc412c389', '{0} مسحت كل الرتب المضافة', k))
         await r.delete(f'{m.chat.id}:RankGowner:{Dev_Zaid}')
         await r.delete(f'{m.chat.id}:RankOwner:{Dev_Zaid}')
         await r.delete(f'{m.chat.id}:RankMod:{Dev_Zaid}')
         await r.delete(f'{m.chat.id}:RankAdm:{Dev_Zaid}')
         await r.delete(f'{m.chat.id}:RankPre:{Dev_Zaid}')
         await r.delete(f'{m.chat.id}:RankMem:{Dev_Zaid}')
         return await r.delete(f'{m.chat.id}:ranklist:{Dev_Zaid}')
   
   if text == 'قائمه الرتب' or text == 'قائمة الرتب':
     if not await mod_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
     else:
       if not await r.smembers(f'{m.chat.id}:ranklist:{Dev_Zaid}'):
         return await m.reply(t('g_b6582caddb', '{0} مافيه رتب مضافة', k))
       else:
         txt = 'قائمة الرتب:\n'
         count = 1
         for rrr in await r.smembers(f'{m.chat.id}:ranklist:{Dev_Zaid}'):
            rank = rrr.split('&&newr=')
            txt += f'{count}) {rank[0]} ~ ( {rank[1]} )\n'
            count += 1
         txt += '\n☆'
         return await m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح رتبه' or text == 'مسح رتبة':
     if not await mod_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
     else:
       await r.set(f'{m.from_user.id}:delRank:{m.chat.id}{Dev_Zaid}',1,ex=600)
       return await m.reply(t('g_d44545c098', '{0} ارسل اسم الرتبه اللي تبي تمسحها الحين', k))
   
   if text == 'تغيير رتبه' or text == 'تغيير رتبة':
     if not await mod_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_198196b423', '{0} هذا الأمر يخص ( المدير وفوق ) بس', k))
     else:
       await r.set(f'{m.from_user.id}:addRank:{m.chat.id}{Dev_Zaid}',1,ex=600)
       return await m.reply(t('g_feaec2a5e9', '\n{0} ارسل الرتبه اللي تبي تغييرها\n\n{1} مالك اساسي\n{2} مالك\n{3} مدير\n{4} ادمن\n{5} مميز\n{6} عضو\n☆', k, k, k, k, k, k, k))