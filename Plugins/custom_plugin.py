'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy6"}

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


@Client.on_message(filters.text & filters.group, group=31)
async def addPluginHandler(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    await plugin_func(c,m,k)
    
async def plugin_func(c,m,k):
   if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
        return
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
   
   if await r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}') or await r.get(f'{m.from_user.id}:setAddP:{m.chat.id}{Dev_Zaid}') or await r.get(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}') or await r.get(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}') or await r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}') or await r.get(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}'):
     if text == 'الغاء':
       await m.reply(t('g_134b4d36e5', '{0} ابشر ياعيني لغيت كلشي', k))
       await r.delete(f'{m.from_user.id}:setAddP:{m.chat.id}{Dev_Zaid}')
       await r.delete(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}')
       await r.delete(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}')
       await r.delete(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}')
       await r.delete(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}')
       return 
     
   if text == 'اضف ميزة' or text == 'اضف ميزه':
     if await devp_pls(m.from_user.id,m.chat.id):
        await r.set(f'{m.from_user.id}:setAddP:{m.chat.id}{Dev_Zaid}',1)
        return await m.reply(t('g_ee49bbfb0e', '{0} هلا عيني ارسل اسم الميزة الحين', k))
   
   if await r.get(f'{m.from_user.id}:setAddP:{m.chat.id}{Dev_Zaid}') and await devp_pls(m.from_user.id,m.chat.id) and len(m.text.split()) == 1:
      await r.delete(f'{m.from_user.id}:setAddP:{m.chat.id}{Dev_Zaid}')
      await r.set(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}',m.text)
      return await m.reply(t('g_3c565f3d4b', '{0} تمام عيني ارسل نوع الميزة الحين ( صوره,فيديو,متحركه,بصمه,صوت)\n☆', k))
   
   if text in ['صوره','فيديو','متحركه','بصمه','صوت'] and await r.get(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}') and await devp_pls(m.from_user.id,m.chat.id):
      miza = await r.get(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}')
      await r.delete(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}')
      await r.set(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}',f'miza={miza}&&type={m.text}')
      return await m.reply(t('g_764855275f', '{0} ارسل يوزر القناة الحين', k))
   
   if await r.get(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}') and await devp_pls(m.from_user.id,m.chat.id):
      miza = await r.get(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}')
      miza += f'&&channel={m.text.replace("@","")}'
      await r.delete(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}')
      await r.set(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}', miza)
      return await m.reply(t('g_074f06ce04', '{0} ارسل الحين ايديات الرسايل العشوائية\n{1} مثال 1 - 100', k, k))
   
   if await r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}') and await devp_pls(m.from_user.id,m.chat.id):
      miza = await r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}')
      id1 = int(m.text.split('-')[0])
      id2 = int(m.text.split('-')[1])
      await r.delete(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}')
      miza_name = miza.split('miza=')[1].split('&&')[0]
      miza_type = miza.split('&&type=')[1].split('&&')[0]
      miza_channel = miza.split('&&channel=')[1].split('&&')[0]
      await r.set(f'{miza_name}:customPlugin:{Dev_Zaid}', f'type={miza_type}&&channel={miza_channel}&&random={id1}_{id2}')
      await r.sadd(f'customPlugins:{Dev_Zaid}', miza_name)
      return await m.reply(t('g_ce95d82d67', '{0} ابشر ضفت الميزة ( {1} )\n{2} نوع الميزة {3}\n{4} قناة الميزة ( @{5} )', k, miza_name, k, miza_type, k, miza_channel))
   
   if text == 'مسح ميزة' or text == 'مسح ميزه':
     if await devp_pls(m.from_user.id,m.chat.id):
        await r.set(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}',1)
        return await m.reply(t('g_ee49bbfb0e', '{0} هلا عيني ارسل اسم الميزة الحين', k))
        
   if await r.get(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}') and await devp_pls(m.from_user.id,m.chat.id):
     if not await r.get(f'{m.text}:customPlugin:{Dev_Zaid}'):
       await r.delete(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}')
       return await m.reply(t('g_cf61f5ad52', '{0} مافي ميزة بهالأسم', k))
     else:
       await r.srem(f'customPlugins:{Dev_Zaid}', m.text)
       await r.delete(f'{m.text}:customPlugin:{Dev_Zaid}')
       await r.delete(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}')
       await r.delete(f'{m.text}:customPluginD:{Dev_Zaid}{m.chat.id}')
       return await m.reply(t('g_e30d0b5195', '{0} الميزة ( {1} ) مسحتها .', k, m.text))
   
   if text == 'المميزات المضافه':
     if await devp_pls(m.from_user.id,m.chat.id):
       if not await r.smembers(f'customPlugins:{Dev_Zaid}'):
         return await m.reply(t('g_2b3b02c0ea', '{0} مافي ولا ميزة مضافة', k))
       else:
         text = 'المميزات المضافه:\n\n'
         count = 1
         for miza in await r.smembers(f'customPlugins:{Dev_Zaid}'):
            text += f'{count}) - {miza}\n'
            count += 1
         text += '\n☆'
         return await m.reply(text)
   
   if await r.get(f'{m.text}:customPlugin:{Dev_Zaid}'):
      if await r.get(f'{m.text}:customPluginD:{Dev_Zaid}{m.chat.id}'):
         return
      else:
         miza = await r.get(f'{m.text}:customPlugin:{Dev_Zaid}')
         type = miza.split('type=')[1].split('&&')[0]
         channel = miza.split('&&channel=')[1].split('&&')[0]
         random1 = int(miza.split('&&random=')[1].split('_')[0])
         random2 = int(miza.split('&&random=')[1].split('_')[1])
         rand = random.randint(random1,random2)
         if type == 'صوره':
            await m.reply_photo(f'https://t.me/{channel}/{rand}')
         
         if type == 'فيديو':
            await m.reply_video(f'https://t.me/{channel}/{rand}')
        
         if type == 'متحركه':
            await m.reply_animation(f'https://t.me/{channel}/{rand}')
         
         if type == 'بصمه':
            await m.reply_voice(f'https://t.me/{channel}/{rand}')
         
         if type == 'صوت':
            await m.reply_audio(f'https://t.me/{channel}/{rand}')
   
   if text.startswith('تعطيل ') and len(text.split()) == 2:
      miza = text.split()[1]
      if await r.get(f'{miza}:customPlugin:{Dev_Zaid}'):
        if not await owner_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k)) 
        else:
          if await r.get(f'{miza}:customPluginD:{Dev_Zaid}{m.chat.id}'):
            return await m.reply(t('g_43f63cb74b', '{0} من「 {1} 」\n{2} ميزة {3} معطله من قبل\n☆', k, m.from_user.mention, k, miza))
          else:
            await r.set(f'{miza}:customPluginD:{Dev_Zaid}{m.chat.id}',1)
            return await m.reply(t('g_17ded0c134', 'من「 {0} 」\n{1} ابشر عطلت ميزة {2}\n☆', m.from_user.mention, k, miza))
   
   if text.startswith('تفعيل ') and len(text.split()) == 2:
      miza = text.split()[1]
      if await r.get(f'{miza}:customPlugin:{Dev_Zaid}'):
        if not await owner_pls(m.from_user.id,m.chat.id):
          return await m.reply(t('g_48f04e3277', '{0} هذا الامر يخص ( المالك وفوق ) بس', k)) 
        else:
          if not await r.get(f'{miza}:customPluginD:{Dev_Zaid}{m.chat.id}'):
            return await m.reply(t('g_bd1a2ca7a0', '{0} من「 {1} 」\n{2} ميزة {3} مفعله من قبل\n☆', k, m.from_user.mention, k, miza))
          else:
            await r.delete(f'{miza}:customPluginD:{Dev_Zaid}{m.chat.id}')
            return await m.reply(t('g_c4945f41fe', 'من「 {0} 」\n{1} ابشر فعلت ميزة {2}\n☆', m.from_user.mention, k, miza))
   
            
            
          
   
   
   
   
      
   