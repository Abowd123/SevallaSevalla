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

import random, re, time, os, sys
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
import asyncio


@Client.on_message(filters.text & filters.group, group=36)
async def replaceCode(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    channel = await r.get(f'{Dev_Zaid}:BotChannel') or 'yqyqy66'
    await raplaceCodefunc(c,m,k,channel)
    
async def raplaceCodefunc(c,m,k,channel):
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
       
   '''
   if text == 'الملفات':
     if m.from_user.id == 6168217372:
        text = '——— ملفات السورس ———'
        a = os.listdir('Plugins')
        a.sort()
        count = 1
        for file in a:
          if file.endswith('.py'):
            text += f'\n{count}) `{file}`'
            count += 1
        text += f'\n——— @{channel} ———'
        return await m.reply(text, disable_web_page_preview=True)
   '''
   if await r.get(f'{m.chat.id}:replace:{m.from_user.id}{Dev_Zaid}') or await r.get(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}') or await r.get(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}'):
     if text == 'الغاء':
       await r.delete(f'{m.chat.id}:replace:{m.from_user.id}{Dev_Zaid}')
       await r.delete(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}')
       await r.delete(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}')
       return await m.reply(f'{k} من عيوني لغيت استبدال كلمة ')
      
   if text == 'استبدال كلمه' or text == 'استبدال كلمة':
      if not await devp_pls(m.from_user.id,m.chat.id):
         return await m.reply(f'{k} هذا الأمر يخص ( مبرمج السورس ) بس')
      else:
         await r.set(f'{m.chat.id}:replace:{m.from_user.id}{Dev_Zaid}',1,ex=600)
         return await m.reply(f'{k} ارسل الكلمة القديمة الآن')
   
   if await r.get(f'{m.chat.id}:replace:{m.from_user.id}{Dev_Zaid}') and await devp_pls(m.from_user.id,m.chat.id):
      await r.set(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}',m.text,ex=600)
      await r.delete(f'{m.chat.id}:replace:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(f'{k} ارسل الكلمة الجديدة الحين')
   
   if await r.get(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}') and await devp_pls(m.from_user.id,m.chat.id):
      txt = await r.get(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}')
      await r.delete(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}',f'{txt}&&new&&{m.text}',ex=600)
      a = os.listdir('Plugins')
      a.sort()
      txt = f'{k} ارسل اسم الملف الي تبي تعدل فيه الحين:'
      count = 1
      txt += '\n\n——— ملفات السورس ———'
      for file in a:
          if file.endswith('.py'):
            txt += f'\n{count}) `{file}`'
            count += 1
      txt += f'\n——— @{channel} ———'
      return await m.reply(txt)
   
   if await r.get(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}') and await devp_pls(m.from_user.id,m.chat.id) and m.text in os.listdir('Plugins'):
      mm = await m.reply(f'{k} جاريع تعديل الملف')
      get = await r.get(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}')
      old = get.split('&&new&&')[0]
      new = get.split('&&new&&')[1]
      await r.delete(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}')
      with open(f'Plugins/{m.text}','r') as Read:
         old_confing = Read.read()
         await mm.edit(f'{k} تم فتح الملف وقرائته')
      with open(f'Plugins/{m.text}','w+') as Write:
         await mm.edit(f'{k} تم فتح الملف جاري كتابة الكود مع استبدال الكلمة')
         Write.write(old_confing.replace(old,new))
      await mm.edit(f'{k} تم فتح الملف `{m.text}` وتعديله\n{k} تم استبدال الكلمة القديمة ( {old} ) بالكلمة الجديدة ( {new} )')
      python = sys.executable
      os.execl(python, python, *sys.argv)
      
      
      
      
      
   