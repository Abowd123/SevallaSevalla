
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

@Client.on_message(filters.text & filters.group, group=999)
async def customCummandHandler(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    await addcommand(c,m,k)
   
   
async def addcommand(c,m,k):
   if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return  
   if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return
   text = m.text
   name = await r.get(f'{Dev_Zaid}:BotName') or 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if await r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = await r.get(f'Custom:{Dev_Zaid}&text={text}')
   if await isLockCommand(m.from_user.id, m.chat.id, text): return
   if await r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}')
     return await m.reply(quote=True,text=f'{k} من عيوني لغيت اضافة امر ')
   
   if await r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}')
     return await m.reply(quote=True,text=f'{k} من عيوني لغيت اضافة امر ')

   if text == 'الاوامر المضافه' or text == 'الاوامر المضافة':
      if not await owner_pls(m.from_user.id, m.chat.id):
          return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك وفوق ) وبس')
      else:
          if not await r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}'):
            return await m.reply(quote=True,text=f'{k} مافيه اوامر مضافه')
          else:
              text = 'الاوامر المضافة:\n'
              count = 0
              for cmnd in await r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}'):
                 count += 1
                 command = cmnd
                 cc = await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={command}')
                 old_c = cc
                 text += f'{count}) {command} ~ ( {old_c} )\n'
              text += '\n༄'
              return await m.reply(quote=True,text=text)
   
   if text == 'اضف امر' or text == 'تغيير امر':
     if not await r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):
       if not await owner_pls(m.from_user.id, m.chat.id):
          return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك وفوق ) وبس')
       else:
          await r.set(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}',1)
          await m.reply(quote=True,text=f'{k} تمام عيني ، ارسل الامر القديم عشان اغيره')
          return

   if await r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}') and await admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      await r.delete(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}', m.text)
      await m.reply(quote=True,text=f'{k} حلو عشان تغيير امر ( {m.text} )\n{k} ارسل الامر الجديد الحين\n☆')
      return
   
   if await r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}') and await admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      command_o = await r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}')
      command_n = m.text
      await r.delete(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={command_n}', command_o)
      await r.sadd(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}', command_n)
      await m.reply(quote=True,text=f'{k} غيرت الامر القديم {command_o}\n{k} الى الامر الجديد ( {command_n} )')
      return 


@Client.on_message(filters.text & filters.group, group=1000)
async def delCustomCommandHandler(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    await delcommand(c,m,k)
   
   
async def delcommand(c,m,k):
   if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return
   if await r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return
   text = m.text
   if await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={m.text}'):
       text = await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={m.text}')
   
   if await r.get(f'Custom:{Dev_Zaid}&text={m.text}'):
       text = await r.get(f'Custom:{Dev_Zaid}&text={m.text}')
   
   if await isLockCommand(m.from_user.id, m.chat.id, text): return
   if await r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}')
     return await m.reply(quote=True,text=f'{k} من عيوني لغيت مسح امر ')

   if text == 'مسح الاوامر' or text == 'مسح الاوامر المضافة':
     if not await mod_pls(m.from_user.id, m.chat.id):
       return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المدير وفوق ) وبس') 
     else:
       if not await r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}'):
         return await m.reply(quote=True,text=f'{k} مافيه اوامر مضافه')
       else:
         count = 0
         for cmnd in await r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}'):
           command = cmnd
           await r.delete(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={command}')
           await r.srem(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}', command)
           count += 1
         text = f'من「 {m.from_user.mention} 」\n{k} ابشر مسحت {count} أمر\n☆'
         return await m.reply(quote=True,text=text)
       
   
   if text == 'مسح امر':
     if not await r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}'):
       if not await mod_pls(m.from_user.id, m.chat.id):
          return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المدير وفوق ) وبس')
       else:
          await r.set(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}',1)
          await m.reply(quote=True,text=f'{k} ارسل الامر الحين')
          return
      

   if await r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') and await admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      await r.delete(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}')
      if not await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={m.text}'):
         return await m.reply(quote=True,text=f'{k} هذا الأمر مو مضاف')
      await r.srem(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}', m.text)
      await r.delete(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={m.text}')
      await m.reply(quote=True,text=f'{k} من「 {m.from_user.mention} 」\n{k} ابشر مسحت الأمر\n☆')
      return
   
   
      
      
############ global CustomCommand



@Client.on_message(filters.text, group=1001)
async def customCummandGlobalHandler(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    await addcommandg(c,m,k)
   
   
async def addcommandg(c,m,k):
   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return
   text = m.text
   if await r.get(f'Custom:{Dev_Zaid}&text={m.text}'):
       text = await r.get(f'Custom:{Dev_Zaid}&text={m.text}')
   
   if await r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}')
     return await m.reply(quote=True,text=f'{k} من عيوني لغيت اضف امر عام')
   
   if await r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}')
     return await m.reply(quote=True,text=f'{k} من عيوني لغيت اضف امر عام')

   if text == 'الاوامر العامه' or text == 'الاوامر المضافه العامه' and not m.chat.type == ChatType.PRIVATE:
      if not await dev_pls(m.from_user.id, m.chat.id):
          return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
      else:
          if not await r.smembers(f'listCustom:{Dev_Zaid}'):
            return await m.reply(quote=True,text=f'{k} مافيه اوامر عامه مضافه')
          else:
              text = 'الاوامر العامه:\n'
              count = 0
              for cmnd in await r.smembers(f'listCustom:{Dev_Zaid}'):
                 count += 1
                 command = cmnd
                 cc = await r.get(f'Custom:{Dev_Zaid}&text={command}')
                 old_c = cc
                 text += f'{count}) {command} ~ ( {old_c} )\n'
              text += '\n☆'
              return await m.reply(quote=True,text=text)
   
   if text == 'اضف امر عام' or text == 'تغيير امر عام':
     if not await r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):
       if not await dev_pls(m.from_user.id, m.chat.id):
          return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
       else:
          await r.set(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}',1)
          await m.reply(quote=True,text=f'{k} تمام عيني ، ارسل الامر القديم عشان اغيره')
          return

   if await r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}') and await dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      await r.delete(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}', m.text)
      await m.reply(quote=True,text=f'{k} حلو عشان تغيير امر ( {m.text} )\n{k} ارسل الامر الجديد الحين\n☆')
      return
   
   if await r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}') and await dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      command_o = await r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}')
      command_n = m.text
      await r.delete(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}')
      await r.set(f'Custom:{Dev_Zaid}&text={command_n}', command_o)
      await r.sadd(f'listCustom:{Dev_Zaid}', command_n)
      await m.reply(quote=True,text=f'{k} غيرت الامر القديم {command_o}\n{k} الى الامر الجديد ( {command_n} )')
      return 


@Client.on_message(filters.text , group=1002)
async def delCustomCommandGHandler(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    await delcommandg(c,m,k)
   
   
async def delcommandg(c,m,k):
   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return
   if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   text = m.text
   if await r.get(f'Custom:{Dev_Zaid}&text={m.text}'):
       text = await r.get(f'Custom:{Dev_Zaid}&text={m.text}')
   
   if await r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}')
     return await m.reply(quote=True,text=f'{k} من عيوني لغيت مسح امر عام')

   if text == 'مسح الاوامر العامه':
     if not await dev_pls(m.from_user.id, m.chat.id):
       return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس') 
     else:
       if not await r.smembers(f'listCustom:{Dev_Zaid}'):
         return await m.reply(quote=True,text=f'{k} مافيه اوامر عامه مضافه')
       else:
         count = 0
         for cmnd in await r.smembers(f'listCustom:{Dev_Zaid}'):
           command = cmnd
           await r.delete(f'Custom:{Dev_Zaid}&text={command}')
           await r.srem(f'listCustom:{Dev_Zaid}', command)
           count += 1
         text = f'من「 {m.from_user.mention} 」\n{k} ابشر مسحت {count} أمر عام\n☆'
         return await m.reply(quote=True,text=text)
       
   
   if text == 'مسح امر عام':
     if not await r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):
       if not await dev_pls(m.from_user.id, m.chat.id):
          return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
       else:
          await r.set(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}',1)
          await m.reply(quote=True,text=f'{k} ارسل الامر الحين')
          return
   
   if re.match("^فتح امر ",text):
     if not await gowner_pls(m.from_user.id, m.chat.id):
       return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
     else:
       txt=text.split(None,2)[2]
       if not await r.hget(Dev_Zaid+f"locks-{m.chat.id}", txt):
         return await m.reply(t('g_919c05e513', "الامر مو مقفول من قبل"))
       await r.hdel(Dev_Zaid+f"locks-{m.chat.id}", txt)
       return await m.reply(t('g_d98ec2dccb', "تم فتح الامر بنجاح"))
   
   if text == "الاوامر المقفوله":
      if not await gowner_pls(m.from_user.id, m.chat.id):
       return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
      else:
        if not await r.hgetall(Dev_Zaid+f"locks-{m.chat.id}"):
          return await m.reply(t('g_5cc164dd2f', '{0} مافيه اوامر مقفولة', k))
        else:
          commands = await r.hgetall(Dev_Zaid+f"locks-{m.chat.id}")
          txt = "الاوامر المقفوله:\n\n"
          count = 1
          for command in commands:
            cc = int(commands[command])
            if cc == 0:
              rank = "مالك اساسي"
            elif cc == 1:
              rank = "مالك وفوق"
            elif cc == 2:
              rank = "مدير و فوق"
            elif cc == 3:
              rank = "ادمن وفوق"
            elif cc == 4:
              rank = "مميز و فوق"
            txt += f"{count} ) {command} - ( {rank} )\n"
            count += 1
          return await m.reply(txt, disable_web_page_preview=True)
   
   if text == "مسح الاوامر المقفوله":
      if not await gowner_pls(m.from_user.id, m.chat.id):
       return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
      else:
        if not await r.hgetall(Dev_Zaid+f"locks-{m.chat.id}"):
          return await m.reply(t('g_5cc164dd2f', '{0} مافيه اوامر مقفولة', k))
        else:
          count = len(list((await r.hgetall(Dev_Zaid+f"locks-{m.chat.id}")).keys()))
          await r.delete(Dev_Zaid+f"locks-{m.chat.id}")
          return await m.reply(t('g_ff50c95531', '{0} ابشر مسحت ( {1} )', k, count))
   
   if re.match("^قفل امر ",text):
     if not await gowner_pls(m.from_user.id, m.chat.id):
       return await m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
     else:
       txt=text.split(None,2)[2]
       return await m.reply(
          t('g_e112e2b3eb', '{0} حسناً عزيزي اختار نوع الرتبه :\n{1} سيتم وضع امر ↤︎( {2} ) له فقط', k, k, txt),
          reply_markup=InlineKeyboardMarkup(
            [
              [
                InlineKeyboardButton (
                   "مالك اساسي",
                   callback_data=f"gowner+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مالك",
                   callback_data=f"owner+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مدير",
                   callback_data=f"mod+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "ادمن",
                   callback_data=f"admin+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مميز",
                   callback_data=f"pre+{m.from_user.id}"
                )
              ]
            ]
          )
       )

   if await r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}') and await dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      await r.delete(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}')
      if not await r.get(f'Custom:{Dev_Zaid}&text={m.text}'):
         return await m.reply(quote=True,text=f'{k} هذا الأمر مو مضاف')
      await r.srem(f'listCustom:{Dev_Zaid}', m.text)
      await r.delete(f'Custom:{Dev_Zaid}&text={m.text}')
      await m.reply(quote=True,text=f'{k} من「 {m.from_user.mention} 」\n{k} ابشر مسحت الأمر العام\n☆')
      return
   
   
      