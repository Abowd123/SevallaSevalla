import logging
import random, re, time, os
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.replies import t
from helpers.Ranks import *
from helpers.get_create import get_creation_date
from pyrogram.raw.functions.users import GetFullUser
from io import BytesIO
from pyrogram.file_id import FileId, FileType, ThumbnailSource
from pyrogram.raw.functions.channels import GetFullChannel
from .games import get_emoji_bank
from helpers.Ranks import isLockCommand
import asyncio
def get_top(users):
   users = [tuple(i.items()) for i in users]
   top = sorted(users, key=lambda i: i[-1][-1], reverse=True)
   top = [dict(i) for i in top]
   return top
custom_ids = ['''
- ᴜѕᴇʀɴᴀᴍᴇ ➣ {اليوزر} .
- ᴍѕɢѕ ➣ {الرسائل} .
- ѕᴛᴀᴛѕ ➣ {الرتبه} .
- ʏᴏᴜʀ ɪᴅ ➣ {الايدي} .
- ᴇᴅɪᴛ ᴍsɢ ➣ {التعديل} .
- ᴅᴇᴛᴀɪʟs ➣ {التفاعل} .
-  ɢᴀᴍᴇ ➣ {المجوهرات} .
{البايو}
''','''
• USE 𖦹 {اليوزر}
• MSG 𖥳 {الرسائل}
• STA 𖦹 {الرتبه}
• iD 𖥳 {الايدي}
{البايو}
''','''
➞: 𝒔𝒕𝒂𓂅 {اليوزر} 𓍯
➞: 𝒖𝒔𝒆𝒓𓂅 {المعرف} 𓍯
➞: 𝒎𝒔𝒈𝒆𓂅 {الرسائل} 𓍯
➞: 𝒊𝒅 𓂅 {الايدي} 𓍯
{البايو}
''','''
♡ : 𝐼𝐷 𖠀 {الايدي} .
♡ : 𝑈𝑆𝐸𝑅 𖠀 {اليوزر} .
♡ : 𝑀𝑆𝐺𝑆 𖠀 {الرسائل} .
♡ : 𝑆𝑇𝐴𝑇𝑆 𖠀 {الرتبه} .
♡ : 𝐸𝐷𝐼𝑇  𖠀 {التعديل} .
{البايو}
''', '''
- الايـدي || {الايدي}.
• الاسـم  || {الاسم}.
• المُعرف || {اليوزر}.
• الرُتبـه || {الرتبه}.
• الرسائل || {الرسائل}.
{البايو}
''', '''
⌁ NaMe ⇨ {الاسم}
⌁ Use ⇨ {اليوزر}
⌁ Msg ⇨ {الرسائل}
⌁ Sta ⇨ {الرتبه}
⌁ iD ⇨ {الايدي}
{البايو}
''', '''
📋¦ ɴᴀᴍᴇ ➺ {الاسم}
🗞¦ ʏᴏᴜʀ ɪᴅ ➺ {الايدي}
🔦¦ ᴜѕᴇʀɴᴀᴍᴇ ➺ {اليوزر}
🕹¦ ѕᴛᴀᴛѕ ➺ {الرتبه}
🔭¦ ᴅᴇᴛᴀɪʟs ➺ {التفاعل}
📨¦  ᴍѕɢѕ ➺ {الرسائل}
🎰¦ ɢᴀᴍᴇ ➺ {المجوهرات}
{البايو}
''', '''
✾ 𝐔𝐒𝐄 ⤷ {اليوزر}
✾ 𝐌𝐒𝐆 ⤷ {الرسائل}
✾ 𝐒𝐓𝐀 ⤷ {الرتبه}
✾ 𝐈𝐃 ⤷ {الايدي}
✾ 𝐁𝐈𝐎 ⤷ {البايو}
''', '''
𓆰 𝑼𝑬𝑺 : {اليوزر}
𓆰 𝑺𝑻𝑨 : {الرتبه}
𓆰 𝑰𝑫 : {الايدي}
𓆰 𝑴𝑺𝑮 : {الرسائل}
{البايو}'''
]


comments = [
  'تيكفه لاتكتب ايدي',
  'يع',
  'جبر',
  'احلى من يكتب ايدي',
  'افخم ايدي',
  'لحد يرسل ايدي من بعده',
  'يلبييه اطلق ايدي',
  'ازق ايدي',
  'لعد تكتب ايدي',
  'للاسف ايديك تلوث بصري ):',
  'جابك الله انت وأيديك على شكل جبر خاطر لقلبّي'
]

@Client.on_message(filters.group, group=9)
async def addmsgCount(c,m):

   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return
   if not await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'):
      await r.set(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}', 1)
   else:
      get = int(await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'))
      await r.set(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}', get+1)
   await r.set(f"{m.from_user.id}:bankName", m.from_user.first_name[:25])

@Client.on_edited_message(filters.group, group=10)
async def addeditedmsgCount(c,m):

   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return
   if not await r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'):
      await r.set(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}', 1)
   else:
      get = int(await r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'))
      await r.set(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}', get+1)

@Client.on_message(filters.text & filters.group, group=11)
async def rankGetHandler(c,m):
   k = await r.get(f'{Dev_Zaid}:botkey')
   await get_my_rank(c,m,k)



async def get_my_rank(c,m,k):
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
   if text == 'مجموعاتي':
     if not await r.smembers(f'{m.from_user.id}:groups'):
       return await m.reply(t('g_b17d9a2a3c', '{0} ماعندك مجموعات', k))
     else:
       groups = len(await r.smembers(f'{m.from_user.id}:groups'))
       return await m.reply(t('g_23b8ebbbb5', '{0} عدد مجموعاتك ↼ ( {1} )', k, groups))

   if text == 'انشائي':
      create_date = await get_creation_date(m.from_user.id)
      return await m.reply(t('g_7d07b32098', '{0} الانشاء ( {1} )', k, create_date))

   if text == 'الانشاء' and not m.reply_to_message:
      create_date = await get_creation_date(m.from_user.id)
      return await m.reply(t('g_7d07b32098', '{0} الانشاء ( {1} )', k, create_date))

   if (text == 'الانشاء' or text == 'انشائه') and m.reply_to_message:
      create_date = await get_creation_date(m.reply_to_message.from_user.id)
      return await m.reply(t('g_7d07b32098', '{0} الانشاء ( {1} )', k, create_date))

   if text == 'اسمي':
     return await m.reply(m.from_user.first_name, disable_web_page_preview=True)

   if text == 'معلوماتي':
      msgs = int(await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'))
      if msgs > 50:
        tfa3l = 'شد حيلك'
      if msgs > 500:
        tfa3l = 'يجي منك'
      if msgs > 750:
        tfa3l = 'تفاعل متوسط'
      if msgs > 2500:
        tfa3l = 'متفاعل'
      if msgs > 5000:
        tfa3l = 'اسطورة التفاعل'
      if msgs > 10000:
        tfa3l = 'كنق التلي'
      else:
        tfa3l = 'تفاعل صفر'
      if not await r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'):
         edits = 0
      else:
         edits= int(await r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'))
      if not await r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'):
         contacts = 0
      else:
         contacts = int(await r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'))
      if m.from_user.username:
         username = f'@{m.from_user.username}'
      if m.from_user.usernames:
         username = ''
         for i in m.from_user.usernames: username += f"@{i.username} "
      else:
         username = 'مافي يوزر'
      rank = await get_rank(m.from_user.id,m.chat.id)
      text = f'''
⚘ المعلومات
❁ الاسم ↼ {m.from_user.mention}
❁ اليوزر ↼ {username}
❁ الايدي  ↼ {m.from_user.id}
❁ الرتبه ↼ {rank}
┄─┅═ـ═┅─┄
⚘ احصائيات الرسايل
❁ الرسايل ↼ {msgs}
❁ التعديل ↼ {edits}
❁ التفاعل ↼ {tfa3l}
'''
      return await m.reply(text)

   if text == 'بايو' and m.reply_to_message and m.reply_to_message.from_user:
      if await r.get(f'{m.chat.id}:disableBio:{Dev_Zaid}'):  return
      get = await c.get_chat(m.reply_to_message.from_user.id)
      if not get.bio:
        return await m.reply(t('g_a19f7bb52b', '{0} ماعنده بايو', k))
      else:
        return await m.reply(t('g_39f77e8fb4', '`{0}`', get.bio))

   if text == 'بايو' and not m.reply_to_message:
      if await r.get(f'{m.chat.id}:disableBio:{Dev_Zaid}'):  return
      get = await c.get_chat(m.from_user.id)
      if not get.bio:
        return await m.reply(t('g_9e31ab6d85', '{0} ماعندك بايو', k))
      else:
        return await m.reply(t('g_39f77e8fb4', '`{0}`', get.bio))


   if text == 'المجموعه' or text == 'المجموعة':
      get = c.invoke(GetFullChannel(channel=c.resolve_peer(m.chat.id)))
      if get.full_chat.exported_invite:
        link = get.full_chat.exported_invite.link
      else:
        link = 'مافي رابط'
      admins = get.full_chat.admins_count
      kicked = get.full_chat.kicked_count
      count = get.full_chat.participants_count
      if m.chat.photo:
        type = 'photo'
        if m.chat.username:
          photo = f'https://t.me/{m.chat.username}'
        else:
          photo = await c.download_media(m.chat.photo.big_file_id)
      else:
        type = 'text'
      text = f'معلومات المجموعة:\n\n{k} الاسم ↢ {m.chat.title}\n{k} الايدي ↢ {m.chat.id}\n{k} عدد الاعضاء ↢ ( {count} )\n{k} عدد المشرفين ↢ ( {admins} )\n{k} عدد المحظورين ↢ ( {kicked} )\n{k} الرابط ↢ {link} '
      if type == 'photo':
         await m.reply_photo(photo, caption=text)
         try:
           os.remove(photo)
         except Exception:
           pass
         return
      else:
         return await m.reply(text, disable_web_page_preview=True)

   if text == 'جهاتي':
     if not await r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'):
       contacts = 0
     else:
       contacts = int(await r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'))
     return await m.reply(t('g_04fadd0f9c', '{0} عدد جهاتك ↢ {1}', k, contacts))

   if text == 'افتاري':
     if await r.get(f'{m.chat.id}:disableAV:{Dev_Zaid}'): return False
     if not m.from_user.photo:
       return await m.reply(t('g_16c96dd262', '{0} ماقدر اجيب افتارك ارسل نقطه خاص وارجع جرب', k))
     else:
       if m.from_user.username:
         photo = f'http://t.me/{m.from_user.username}'
       else:
         for p in c.get_chat_photos(m.from_user.id,limit=1):
           photo = p.file_id
       get_bio = await c.get_chat(m.from_user.id).bio
       if not get_bio:
         caption=None
       else:
         caption = f'`{get_bio}`'
       return await m.reply_photo(photo,caption=caption)

   if text == 'افتار' and m.reply_to_message and m.reply_to_message.from_user:
     if await r.get(f'{m.chat.id}:disableAV:{Dev_Zaid}'): return False
     if not m.reply_to_message.from_user.photo:
       return await m.reply(t('g_70a3c023c8', '{0} مقدر اجيب افتاره يمكن حاظرني', k))
     else:
       if m.reply_to_message.from_user.username:
         photo = f'http://t.me/{m.reply_to_message.from_user.username}'
       else:
         for p in c.get_chat_photos(m.reply_to_message.from_user.id,limit=1):
           photo = p.file_id
       get_bio = await c.get_chat(m.reply_to_message.from_user.id).bio
       if not get_bio:
         caption=None
       else:
         caption = f'`{get_bio}`'
       return await m.reply_photo(photo,caption=caption)

   if text == 'ايديي':
     return await m.reply(t('g_1011bf4024', '( `{0}` )', m.from_user.id))

   if text.startswith('افتار') and len(text.split()) == 2:
     if await r.get(f'{m.chat.id}:disableAV:{Dev_Zaid}'): return False
     try:
       user = int(text.split()[1])
     except Exception:
       user = text.split()[1]
     try:
       get = await c.get_chat(user)
       if get.photo:
         for p in c.get_chat_photos(get.id,limit=1):
           photo = p.file_id
         if get.bio:
           caption = f'`{get.bio}`'
         else:
           caption = None
         return await m.reply_photo(photo,caption=caption)
     except Exception as e:
       print (e)
       return


   if text == 'رتبتي':
      rank = await get_rank(m.from_user.id, m.chat.id)
      await m.reply(t('g_98d0a08d2b', '{0} رتبتك ↢ {1}', k, rank))

   if text == 'مسح رسائلي' or text == 'مسح رسايلي':
      msgs = int(await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'))
      await r.delete(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}')
      return await m.reply(t('g_6a9527e50d', '{0} ابشر مسحت ( {1} ) من رسائلك', k, msgs))

   if text == 'مسح تكليجاتي':
      if not await r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'):
        return await m.reply(t('g_439fbb532a', '{0} عدد تكليجاتك ↢ 0', k))
      msgs = int(await r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'))
      await r.delete(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}')
      return await m.reply(t('g_d31c762d7d', '{0} ابشر مسحت ( {1} ) من تكليجاتك', k, msgs))

   if text == 'تكليجاتي' or text == 'تعديلاتي':
      if not await r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'):
        return await m.reply(t('g_439fbb532a', '{0} عدد تكليجاتك ↢ 0', k))
      msgs = int(await r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'))
      return await m.reply(t('g_229fed32e8', '{0} عدد تكليجاتك ↢ {1}', k, msgs))

   if text == 'رسايلي' or text == 'رسائلي':
      msgs = int(await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'))
      return await m.reply(t('g_81f3e34918', '{0} عدد رسايلك ↢ {1}', k, msgs))
      
   if (text == 'رسايله' or text == 'رسائلة') and m.reply_to_message and m.reply_to_message.from_user:
      msgs = int(await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.reply_to_message.from_user.id}'))
      return await m.reply(t('g_57583828fb', '{0} عدد رسايله ↢ {1}', k, msgs))




   if text == 'رتبته' and m.reply_to_message and m.reply_to_message.from_user:
      rank = await get_rank(m.reply_to_message.from_user.id, m.chat.id)
      status = await m.chat.get_member(m.reply_to_message.from_user.id).status
      if status == ChatMemberStatus.OWNER:
        rank2 = 'المالك'
      if status == ChatMemberStatus.ADMINISTRATOR:
        rank2 = 'مشرف'
      if status == ChatMemberStatus.RESTRICTED:
        rank2 = 'مقيد'
      if status == ChatMemberStatus.LEFT:
        rank2 = 'طالع'
      if status == ChatMemberStatus.MEMBER:
        rank2 = 'عضو'
      if status == ChatMemberStatus.BANNED:
        rank2 = 'لاقم حظر'
      await m.reply(t('g_99571139ef', 'رتبته:\n{0} في البوت ( {1} )\n{2} في المجموعة ( {3} )\n-', k, rank, k, rank2))

   if text == 'نقل ملكية' or text == 'نقل ملكيه':
     if await r.get(f'{m.chat.id}:rankGOWNER:{m.from_user.id}{Dev_Zaid}'):
       status = await m.chat.get_member(m.from_user.id).status
       if status == ChatMemberStatus.OWNER:
          return await m.reply(t('g_808e54aa7b', '{0} انت مالك القروب', k))
       else:
          for member in await m.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
            if member.status == ChatMemberStatus.OWNER:
              if member.user.is_deleted:
                return await m.reply(t('g_3b68c90d28', '{0} حساب المالك محذوف', k))
              else:
                await r.delete(f'{m.chat.id}:rankGOWNER:{m.from_user.id}{Dev_Zaid}')
                await r.srem(f'{m.chat.id}:listGOWNER:{Dev_Zaid}', m.from_user.id)
                await r.set(f'{m.chat.id}:rankGOWNER:{member.user.id}{Dev_Zaid}')
                await r.sadd(f'{m.chat.id}:listGOWNER:{Dev_Zaid}', member.user.id)
                return await m.reply(t('g_5fa216b231', '「 {0} 」\n{1} نقلت له ملكية المجموعة', member.user.mention, k))

   if text == "مسح المتفاعلين" or text == "تصفير المتفاعلين":
     if not await owner_pls(m.from_user.id, m.chat.id):
       return await m.reply(t('g_7d3d10fef1', '{0} عذراً الامر يخص ↤〖 المالك 〗فقط .', k))
     else:
       keys = await r.keys(f"{Dev_Zaid}{m.chat.id}:TotalMsgs:*")
       for _ in keys: await r.delete(_)
       return await m.reply(t('g_e19ddff65f', '{0} ابشر مسحت كل المتفاعلين', k))

   if text == "مسح القروبات" or text == "تصفير القروبات":
     if not await devp_pls(m.from_user.id, m.chat.id):
       return await m.reply(t('g_2aac5c8b2a', '{0} عذراً الامر يخص ↤〖 Dev🎖️ 〗فقط .', k))
     else:
       keys = await r.keys(f"{Dev_Zaid}:TotalGroupMsgs:*")
       for _ in keys: await r.delete(_)
       return await m.reply(t('g_69a116311e', '{0} ابشر مسحت توب القروبات', k))

   if text == "ترتيبي" or text == "تفاعلي":
     users = await r.keys(f"{Dev_Zaid}{m.chat.id}:TotalMsgs:*")
     jj = []
     for user in users:
          try:
            id = int(user.split("TotalMsgs:")[1])
            msgs = await r.get(user)
            jj.append({"id": id, "msgs": int(msgs)})
          except Exception:
            pass
     top = get_top(jj)
     ids = [i["id"] for i in top]
     rank = ids.index(m.from_user.id) + 1
     msgs = int(await r.get(f"{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}"))
     return await m.reply(t('g_75b4928da7', '{0} ترتيبك بالمتفاعلين ↢ {1}\n{2} رسائلك بالتفاعل ↢ {3:,}\n-', k, rank, k, msgs))

   if text == "المتفاعلين" or text == "توب المتفاعلين":
        users = await r.keys(f"{Dev_Zaid}{m.chat.id}:TotalMsgs:*")
        # print(users)
        jj = []
        for user in users:
                  try:
                    id = int(user.split("TotalMsgs:")[1])
                    # print(id)
                    msgs = await r.get(user)
                    name = await r.get(f"{id}:bankName") or str(id)
                    jj.append({"name": name, "id": id, "msgs": int(msgs)})
                  except Exception:
                    pass
        top = get_top(jj)
        text = "- توب اكثر 20 متفاعل :\n━━━━━━━━━\n"
        count = 1
        for i in top:
            if count == 21: break
            emoji = get_emoji_bank(count)
            text += f"{emoji}{i['msgs']:,} l [{i['name']}](tg://user?id={i['id']})\n"
            count +=1
        return await c.send_message(m.chat.id, text, disable_web_page_preview=True, reply_to_message_id=m.id)

   if text == "القروبات" or text == "توب القروبات":
        groups = await r.keys(f"{Dev_Zaid}:TotalGroupMsgs:*")
        result = []

        for group in groups:
            try:
                chat_id = int(group.split("TotalGroupMsgs:")[1])
                msgs = await r.get(group)
                group_title = await c.get_chat(chat_id).title
                result.append({"group_title": group_title, "chat_id": chat_id, "msgs": int(msgs)})
            except Exception:
                pass

        top_groups = get_top(result)
        response_text = "- توب اكثر 20 قروب متفاعل:\n━━━━━━━━━\n"
        count = 1

        for group in top_groups:
            if count == 21:
                break
            emoji = get_emoji_bank(count)
            response_text += f"{emoji}{group['msgs']:,} l {group['group_title']}\n"
            count += 1

        return await c.send_message(m.chat.id, response_text, disable_web_page_preview=True, reply_to_message_id=m.id)


   if text == 'كشف' and m.reply_to_message and m.reply_to_message.from_user:
       try:
           get = await m.chat.get_member(m.reply_to_message.from_user.id)
           rank = await get_rank(m.reply_to_message.from_user.id, m.chat.id)
           name = m.reply_to_message.from_user.first_name
           msgs = int(await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.reply_to_message.from_user.id}'))
           id = m.reply_to_message.from_user.id
           if m.reply_to_message.from_user.username:
               username = f'@{m.reply_to_message.from_user.username}'
           elif m.reply_to_message.from_user.usernames:
               username = ''
               for i in m.reply_to_message.from_user.usernames: username += f"@{i.username} "
           else:
               username = 'مافي يوزر'
           status = await m.chat.get_member(m.reply_to_message.from_user.id).status
           if status == ChatMemberStatus.OWNER:
               rank2 = 'المالك'
           if status == ChatMemberStatus.ADMINISTRATOR:
               rank2 = 'مشرف'
           if status == ChatMemberStatus.RESTRICTED:
               rank2 = 'مقيد'
           if status == ChatMemberStatus.LEFT:
               rank2 = 'طالع'
           if status == ChatMemberStatus.MEMBER:
               rank2 = 'عضو'
           if status == ChatMemberStatus.BANNED:
               rank2 = 'لاقم حظر'
           text = f'''
{k} الاسم ↢ {name}
{k} الايدي ↢ {id}
{k} اليوزر : ( {username} ) 
{k} الرتبه ↢ ( {rank} )
{k} الرسائل ↢ ( {msgs} )
{k} بالمجموعة ↢ ( {rank2} )
{k} نوع الكشف ↢ بالرد
-
'''
           return await m.reply(text, disable_web_page_preview=True)
       except Exception:
           return await m.reply(t('g_92eb0a0d77', '{0} العضو مو بالمجموعة', k))

   if text.startswith('كشف') and len(text.split()) > 1 and 'tg://user?id=' in m.text.html:
       logging.debug(m.text.html)
       user = user = int(re.search(r'href="([^"]+)', m.text.html).group(1).split('=')[1])
       ks = 'بالمنشن'
       try:
           get = await m.chat.get_member(user)
           name = get.user.first_name
           id = get.user.id
           msgs = int(await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{get.user.id}'))
           if get.user.username:
               username = f'@{get.user.username}'
           elif get.user.usernames:
               username = ""
               for i in get.user.usernames: username += f"@{i.username} "
           else:
               username = 'ماعنده يوزر'
           status = get.status
           if status == ChatMemberStatus.OWNER:
               rank = 'المالك'
           if status == ChatMemberStatus.ADMINISTRATOR:
               rank = 'مشرف'
           if status == ChatMemberStatus.RESTRICTED:
               rank = 'مقيد'
           if status == ChatMemberStatus.LEFT:
               rank = 'طالع'
           if status == ChatMemberStatus.MEMBER:
               rank = 'عضو'
           if status == ChatMemberStatus.BANNED:
               rank = 'لاقم حظر'
       except Exception:
           rank = 'طالع'
           try:
               get = await c.get_chat(user)
               name = get.first_name
               id = get.id
               msgs = int(await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{get.id}'))
               if get.user.username:
                   username = f'@{get.user.username}'
               if get.user.usernames:
                   username = ""
                   for i in get.user.usernames: username += f"@{i.username} "
               else:
                   username = 'ماعنده يوزر'
           except Exception as e:
               logging.exception(e)
               return
       rank2 = await get_rank(id, m.chat.id)
       text = f'''
{k} الاسم ↢ {name}
{k} الايدي ↢{id}
{k} اليوزر : ↢ ( {username} )
{k} الرتبه ↢ ({rank2} )
{k} الرسائل ↢ ( {msgs} )
{k} بالمجموعة ↢ ( {rank} )
{k} نوع الكشف ↢ {ks}
-
        '''
       return await m.reply(text, disable_web_page_preview=True)

   if text.startswith('كشف') and len(text.split()) == 2:
       try:
           user = int(text.split()[1])
           ks = 'بالايدي'
       except Exception:
           user = text.split()[1].replace('@', '')
           ks = 'باليوزر'
       try:
           get = await m.chat.get_member(user)
           name = get.user.first_name
           id = get.user.id
           msgs = int(await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{get.user.id}'))
           if get.user.username:
               username = f'@{get.user.username}'
           elif get.user.usernames:
               username = ""
               for i in get.user.usernames: username += f"@{i.username} "
           else:
               username = 'ماعنده يوزر'
           status = get.status
           if status == ChatMemberStatus.OWNER:
               rank = 'المالك'
           if status == ChatMemberStatus.ADMINISTRATOR:
               rank = 'مشرف'
           if status == ChatMemberStatus.RESTRICTED:
               rank = 'مقيد'
           if status == ChatMemberStatus.LEFT:
               rank = 'طالع'
           if status == ChatMemberStatus.MEMBER:
               rank = 'عضو'
           if status == ChatMemberStatus.BANNED:
               rank = 'لاقم حظر'
       except Exception:
           rank = 'طالع'
           try:
               get = await c.get_chat(user)
               name = get.first_name
               id = get.id
               msgs = int(await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{get.id}'))
               if get.user.username:
                   username = f'@{get.user.username}'
               if get.user.usernames:
                   username = ""
                   for i in get.user.usernames: username += f"@{i.username} "
               else:
                   username = 'ماعنده يوزر'
           except Exception as e:
               logging.exception(e)
               return
       rank2 = await get_rank(id, m.chat.id)
       text = f'''
{k} الاسم ↢ {name}
{k} الايدي ↢{id}
{k} اليوزر : ↢ ( {username} )
{k} الرتبه ↢ ({rank2} )
{k} الرسائل ↢ ( {msgs} )
{k} بالمجموعة ↢ ( {rank} )
{k} نوع الكشف ↢ {ks}
-
        '''
       return await m.reply(text, disable_web_page_preview=True)


   if text == 'صلاحياته' and m.reply_to_message and m.reply_to_message.from_user:
      get = await m.chat.get_member(m.reply_to_message.from_user.id)
      if not get.status in [ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER]:
         return await m.reply(t('g_f787994acb', '{0} هو العضو وما عنده صلاحيات', k))
      if get.status == ChatMemberStatus.OWNER:
         return await m.reply(t('g_0f3b500d8d', '{0} هو المالك وعنده كل الصلاحيات', k))
      if get.status == ChatMemberStatus.ADMINISTRATOR:
         p = get.privileges
         p1 = "✔️" if p.can_manage_chat else "✖️"
         p2 = "✔️" if p.can_delete_messages else "✖️"
         p3 = "✔️" if p.can_manage_video_chats else "✖️"
         p4 = "✔️" if p.can_restrict_members else "✖️"
         p5 = "✔️" if p.can_promote_members else "✖️"
         p6 = "✔️" if p.can_change_info else "✖️"
         p7 = "✔️" if p.can_pin_messages else "✖️"
         text = f'''
{k} هو مشرف وهذي صلاحياته :

1) - ادارة المجموعة ↼ ( {p1} )
2) - مسح الرسائل ↼ ( {p2} )
3) - ادارة مكالمات ↼ ( {p3} )
4) - تقييد الأعضاء وحظرهم ↼ ( {p4} )
5) - رفع المشرفين ↼ ( {p5} )
6) - تعديل معلومات المجموعة ↼ ( {p6} )
7) - تثبيت الرسايل ↼ ( {p7} )


'''
         return await m.reply(text)

   if text == 'صلاحياتي':
      get = await m.chat.get_member(m.from_user.id)
      if not get.status in [ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER]:
         return await m.reply(t('g_c06e442e14', '{0} انت العضو وماعندك صلاحيات', k))
      if get.status == ChatMemberStatus.OWNER:
         return await m.reply(t('g_d24c5b9032', '{0} انت المالك وعندك كل الصلاحيات', k))
      if get.status == ChatMemberStatus.ADMINISTRATOR:
         p = get.privileges
         p1 = "✔️" if p.can_manage_chat else "✖️"
         p2 = "✔️" if p.can_delete_messages else "✖️"
         p3 = "✔️" if p.can_manage_video_chats else "✖️"
         p4 = "✔️" if p.can_restrict_members else "✖️"
         p5 = "✔️" if p.can_promote_members else "✖️"
         p6 = "✔️" if p.can_change_info else "✖️"
         p7 = "✔️" if p.can_pin_messages else "✖️"
         text = f'''
{k} انت مشرف وهذي صلاحياتك :

1) - ادارة المجموعة ↼ ( {p1} )
2) - مسح الرسائل ↼ ( {p2} )
3) - ادارة مكالمات ↼ ( {p3} )
4) - تقييد الأعضاء وحظرهم ↼ ( {p4} )
5) - رفع المشرفين ↼ ( {p5} )
6) - تعديل معلومات المجموعة ↼ ( {p6} )
7) - تثبيت الرسايل ↼ ( {p7} )


'''
         return await m.reply(text)


   if await r.get(f'{m.chat.id}:addCustomID:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:addCustomID:{m.from_user.id}{Dev_Zaid}')
     await m.reply(t('g_5df0efa0b7', '{0} ابشر تم الغاء تعيين الايدي ', k))
     return

   if await r.get(f'{m.chat.id}:addCustomIDG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     await r.delete(f'{m.chat.id}:addCustomIDG:{m.from_user.id}{Dev_Zaid}')
     await m.reply(t('g_78226bb60a', '{0} ابشر تم الغاء تعيين الايدي عام', k))
     return

   if await r.get(f'{m.chat.id}:addCustomIDG:{m.from_user.id}{Dev_Zaid}') and await dev_pls(m.from_user.id, m.chat.id):
      await r.set(f'customID:{Dev_Zaid}', m.text)
      await m.reply(t('g_2e4b47b06e', '{0} وسوينا الايدي العام\n{1} يمديك تجرب شكل الايدي الجديد الحين', k, k))
      await r.delete(f'{m.chat.id}:addCustomIDG:{m.from_user.id}{Dev_Zaid}')
      return

   if await r.get(f'{m.chat.id}:addCustomID:{m.from_user.id}{Dev_Zaid}') and await mod_pls(m.from_user.id, m.chat.id):
      await r.set(f'{m.chat.id}:customID:{Dev_Zaid}', m.text)
      await m.reply(t('g_f2aaf84ac3', '{0} وسوينا الايدي\n{1} يمديك تجرب شكل الايدي الجديد الحين', k, k))
      await r.delete(f'{m.chat.id}:addCustomID:{m.from_user.id}{Dev_Zaid}')
      return

   if text == 'مسح الايدي':
      if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_d69076d2ab', '{0} عذراً الامر يخص ↤〖 المدير 〗فقط .', k))
      if not await r.get(f'{m.chat.id}:customID:{Dev_Zaid}'):
        return await m.reply(t('g_204d412e25', '{0} الايدي مو معدل', k))
      else:
        await m.reply(t('g_bd3fe2a91f', '{0} ابشر مسحت الايدي', k))
        await r.delete(f'{m.chat.id}:customID:{Dev_Zaid}')
        return

   if text == 'مسح الايدي العام' or text == 'مسح الايدي عام':
      if not await dev2_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_1b5bc04eb0', '{0} عذراً الامر يخص ↤〖 Dev²🎖 〗فقط .', k))
      if not await r.get(f'customID:{Dev_Zaid}'):
        return await m.reply(t('g_ca89e0772c', '{0} الايدي العام مو معدل', k))
      else:
        await m.reply(t('g_3823cfcccc', '{0} ابشر مسحت الايدي العام', k))
        await r.delete(f'customID:{Dev_Zaid}')

   if text == 'الايدي':
      if not await mod_pls(m.from_user.id, m.chat.id):
        return
      if not await r.get(f'{m.chat.id}:customID:{Dev_Zaid}'):
        return await m.reply(t('g_204d412e25', '{0} الايدي مو معدل', k))
      else:
        id = await r.get(f'{m.chat.id}:customID:{Dev_Zaid}')
        return await m.reply(t('g_39f77e8fb4', '`{0}`', id))

   if text == 'الايدي العام':
      if not await dev2_pls(m.from_user.id, m.chat.id):
        return
      if not await r.get(f'customID:{Dev_Zaid}'):
        return await m.reply(t('g_ca89e0772c', '{0} الايدي العام مو معدل', k))
      else:
        id = await r.get(f'customID:{Dev_Zaid}')
        return await m.reply(t('g_39f77e8fb4', '`{0}`', id))

   if text == 'تغيير الايدي':
      if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_d69076d2ab', '{0} عذراً الامر يخص ↤〖 المدير 〗فقط .', k))
      else:
        id = random.choice(custom_ids)
        await r.set(f'{m.chat.id}:customID:{Dev_Zaid}', id)
        await m.reply(t('g_f2aaf84ac3', '{0} وسوينا الايدي\n{1} يمديك تجرب شكل الايدي الجديد الحين', k, k))

   if text == 'تعيين الايدي':
      if not await mod_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_d69076d2ab', '{0} عذراً الامر يخص ↤〖 المدير 〗فقط .', k))
      reply = '''
تمام , الحين ارسل شكل الايدي الجديد

- الاختصارات:

{الاسم} ↼ يطلع اسم الشخص
{الايدي} ↼ يطلع ايدي الشخص
{اليوزر} ↼ يطلع يوزر الشخص
{الرتبه} ↼ يطلع رتبته الشخص
{التفاعل} ↼ يطلع تفاعل الشخص
{الرسائل} ↼ يطلع كم رسالة عند الشخص
{التعديل} ↼ يطلع كم مره عدل الشخص
{البايو} ↼ يطلع البايو اللي كاتبه
{تعليق} ↼ يطلع تعليق عشوائي
{الانشاء} ↼ يطلع انشاء الحساب

قناة اشكال الايدي https://t.me/EFFB0T/187

'''
      await m.reply(reply)
      await r.set(f'{m.chat.id}:addCustomID:{m.from_user.id}{Dev_Zaid}', 1)
      return
   if text == 'تعيين الايدي عام':
      if not await dev2_pls(m.from_user.id, m.chat.id):
        return await m.reply(t('g_1b5bc04eb0', '{0} عذراً الامر يخص ↤〖 Dev²🎖 〗فقط .', k))
      reply = '''
تمام , الحين ارسل شكل الايدي الجديد

- الاختصارات:

{الاسم} ↼ يطلع اسم الشخص
{الايدي} ↼ يطلع ايدي الشخص
{اليوزر} ↼ يطلع يوزر الشخص
{الرتبه} ↼ يطلع رتبته الشخص
{التفاعل} ↼ يطلع تفاعل الشخص
{الرسائل} ↼ يطلع كم رسالة عند الشخص
{التعديل} ↼ يطلع كم مره عدل الشخص
{البايو} ↼ يطلع البايو اللي كاتبه
{تعليق} ↼ يطلع تعليق عشوائي
{الانشاء} ↼ يطلع انشاء الحساب

قناة اشكال الايدي https://t.me/EFFB0T/187
'''
      await m.reply(reply)
      await r.set(f'{m.chat.id}:addCustomIDG:{m.from_user.id}{Dev_Zaid}', 1)
      return True


   if text == 'تفعيل الايدي':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_55e29cfbc8', '{0} عذراً الامر يخص ↤〖 الادمن 〗فقط .', k))
     else:
       if not await r.get(f'{m.chat.id}:disableID:{Dev_Zaid}'):
         return await m.reply(t('g_c74d5eec57', '{0} بواسطة ↤ {1}\n{2} الايدي مفعل من قبل', k, m.from_user.mention, k))
       else:
         await r.delete(f'{m.chat.id}:disableID:{Dev_Zaid}')
         return await m.reply(t('g_0250851c06', '{0} بواسطة ↤ {1}\n{2} ابشر فعلت الايدي', k, m.from_user.mention, k))

   if text == 'تعطيل الايدي':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_55e29cfbc8', '{0} عذراً الامر يخص ↤〖 الادمن 〗فقط .', k))
     else:
       if await r.get(f'{m.chat.id}:disableID:{Dev_Zaid}'):
         return await m.reply(t('g_e542510cc5', '{0} بواسطة ↤ {1}\n{2} الايدي معطل من قبل', k, m.from_user.mention, k))
       else:
         await r.set(f'{m.chat.id}:disableID:{Dev_Zaid}',1)
         return await m.reply(t('g_c95c6cb8ea', '{0} بواسطة ↤ {1}\n{2} ابشر عطلت الايدي', k, m.from_user.mention, k))

   if text == 'تفعيل افتاري':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_55e29cfbc8', '{0} عذراً الامر يخص ↤〖 الادمن 〗فقط .', k))
     else:
       if not await r.get(f'{m.chat.id}:disableAV:{Dev_Zaid}'):
         return await m.reply(t('g_c652426ea1', '{0} بواسطة ↤ {1}\n{2} افتار مفعل من قبل', k, m.from_user.mention, k))
       else:
         await r.delete(f'{m.chat.id}:disableAV:{Dev_Zaid}')
         return await m.reply(t('g_c37982b6dc', '{0} بواسطة ↤ {1}\n{2} ابشر فعلت افتار', k, m.from_user.mention, k))

   if text == 'تعطيل افتاري':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_55e29cfbc8', '{0} عذراً الامر يخص ↤〖 الادمن 〗فقط .', k))
     else:
       if await r.get(f'{m.chat.id}:disableAV:{Dev_Zaid}'):
         return await m.reply(t('g_e492ba4d6c', '{0} بواسطة ↤ {1}\n{2} افتار معطل من قبل', k, m.from_user.mention, k))
       else:
         await r.set(f'{m.chat.id}:disableAV:{Dev_Zaid}',1)
         return await m.reply(t('g_bfa0eb0499', '{0} بواسطة ↤ {1}\n{2} ابشر عطلت افتار', k, m.from_user.mention, k))

   if text == 'تعطيل الايدي بالصوره':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_55e29cfbc8', '{0} عذراً الامر يخص ↤〖 الادمن 〗فقط .', k))
     else:
       if await r.get(f'{m.chat.id}:disableIDPHOTO:{Dev_Zaid}'):
         return await m.reply(t('g_6581dd60c3', '{0} بواسطة ↤ {1}\n{2} الايدي بالصوره معطل من قبل', k, m.from_user.mention, k))
       else:
         await r.set(f'{m.chat.id}:disableIDPHOTO:{Dev_Zaid}',1)
         return await m.reply(t('g_fa4cc8a59b', '{0} بواسطة ↤ {1}\n{2} ابشر عطلت الايدي بالصوره', k, m.from_user.mention, k))

   if text == 'تفعيل الايدي بالصوره':
     if not await admin_pls(m.from_user.id,m.chat.id):
       return await m.reply(t('g_55e29cfbc8', '{0} عذراً الامر يخص ↤〖 الادمن 〗فقط .', k))
     else:
       if not await r.get(f'{m.chat.id}:disableIDPHOTO:{Dev_Zaid}'):
         return await m.reply(t('g_b44ca3a7ea', '{0} بواسطة ↤ {1}\n{2} الايدي بالصوره مفعل من قبل', k, m.from_user.mention, k))
       else:
         await r.delete(f'{m.chat.id}:disableIDPHOTO:{Dev_Zaid}')
         return await m.reply(t('g_6716cad386', '{0} بواسطة ↤ {1}\n{2} ابشر فعلت الايدي بالصوره', k, m.from_user.mention, k))

   if text == "لقبي":
     title = await m.chat.get_member(m.from_user.id).custom_title
     if not title:
       return await m.reply(t('g_ea97b2f4f2', '{0} ماعندك لقب', k))
     else:
       return await m.reply(t('g_ceede6f110', '{0} لقبك ↢ ( {1} )', k, title))

   if (text == 'ايدي' or text.lower() == 'ا') and m.reply_to_message and m.reply_to_message.from_user:
       return await m.reply(t('g_ec9bcb6b4f', 'الايدي ↢ ( `{0}` )', m.reply_to_message.from_user.id))

   if (text == 'ايدي' or text.lower() == 'id') and not m.reply_to_message:
      if await r.get(f'{m.chat.id}:disableID:{Dev_Zaid}'):  return
      if await r.get(f'{m.chat.id}:customID:{Dev_Zaid}'):
         id = await r.get(f'{m.chat.id}:customID:{Dev_Zaid}')
      else:
         if await r.get(f'customID:{Dev_Zaid}'):
           id = await r.get(f'customID:{Dev_Zaid}')
         else:
           id = '''
𖡋 𝐔𝐒𝐄 ⌯  {اليوزر}
𖡋 𝐌𝐒𝐆 ⌯  {الرسائل}
𖡋 𝐒𝐓𝐀 ⌯  {الرتبه}
𖡋 𝐈𝐃 ⌯  {الايدي}
𖡋 𝐄𝐃𝐈𝐓 ⌯  {التعديل}
𖡋 𝐂𝐑  ⌯  {الانشاء}
{البايو}'''
      if m.from_user.usernames:
         username = ''
         for i in m.from_user.usernames: username += f"@{i.username} "
      elif m.from_user.username:
         username = f'@{m.from_user.username}'
      else:
         username = 'مافي يوزر'
      rank = await get_rank(m.from_user.id, m.chat.id)
      msg = int(await r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'))
      msgs = f"{msg}"
      iD = f'`{m.from_user.id}`'
      if not await r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'):
         edits = 0
      else:
         edit= int(await r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'))
         edits = f"{edit}"
      name = m.from_user.first_name
      create = await get_creation_date(m.from_user.id)
      get_chat = await c.get_chat(m.from_user.id)
      if get_chat.bio :
         bio = get_chat.bio
      else:
         bio = 'مافي بايو'
      if msg > 50:
        tfa3l = 'شد حيلك'
      if msg > 500:
        tfa3l = 'يجي منك'
      if msg > 750:
        tfa3l = 'تفاعل متوسط'
      if msg > 2500:
        tfa3l = 'متفاعل'
      if msg > 5000:
        tfa3l = 'اسطورة التفاعل'
      if msg > 10000:
        tfa3l = 'اسطورة التلي'
      else:
        tfa3l = 'تفاعل صفر'
      comment = random.choice(comments)
      text = id.replace('{الاسم}', name).replace('{اليوزر}', username).replace('{الرسائل}',str(msgs)).replace('{التعديل}', str(edits)).replace('{الانشاء}', create).replace('{البايو}', f'{bio}').replace('{الايدي}', iD).replace('{الرتبه}', rank).replace('{التفاعل}', tfa3l).replace('{تعليق}', comment)
      if await r.get(f'{m.chat.id}:disableIDPHOTO:{Dev_Zaid}'):
         return await m.reply(text, disable_web_page_preview=True)
      else:
         if m.from_user.photo:
           get_user = c.invoke(GetFullUser(id=(c.resolve_peer(m.from_user.id))))
           photo = get_user.full_user.profile_photo
           video = photo.video_sizes
           if video:
             if len(video) == 3:
               video = video[-2]
             else:
               video = video[-1]
           if video:
              file = BytesIO()
              hash = photo.access_hash
              if await r.get(f"{hash}:{m.from_user.id}"):
                return await m.reply_animation(await r.get(f"{hash}:{m.from_user.id}"), caption=text)
              for byte in c.stream_media(
                message=FileId(
                  file_type=FileType.PHOTO,
                  dc_id=photo.dc_id, media_id=photo.id,
                  access_hash=photo.access_hash,
                  file_reference=photo.file_reference,
                  thumbnail_source=ThumbnailSource.THUMBNAIL,
                  thumbnail_file_type=FileType.PHOTO,
                  thumbnail_size=video.type,
                  volume_id=0, local_id=0
                ).encode()
              ):
                file.write(byte)
              file.name = f'{m.from_user.id}vid{m.chat.id}.mp4'
              send = await m.reply_animation(file, caption=text)
              await r.set(f"{hash}:{m.from_user.id}",send.animation.file_id,ex=3600)
              return True
           else:
              file_id=FileId(
                        file_type=FileType.PHOTO,
                        dc_id=photo.dc_id,
                        media_id=photo.id,
                        access_hash=photo.access_hash,
                        file_reference=photo.file_reference,
                        thumbnail_source=ThumbnailSource.THUMBNAIL,
                        thumbnail_file_type=FileType.PHOTO,
                        thumbnail_size=photo.sizes[0].type,
                        volume_id=0,
                        local_id=0
                    ).encode()
              return await m.reply_photo(file_id, caption=text)
         else:
           return await m.reply(text, disable_web_page_preview=True)


@Client.on_message(filters.new_chat_members, group=1)
async def addContact(c,m):
  for me in m.new_chat_members:
    if not m.from_user.id == me.id:
      if not await r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'):
        await r.set(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}',1)
      else:
        co = int(await r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'))
        await r.set(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}',co+1)


'''

@Client.on_message(filters.text & filters.group, group=17)
def setIDHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    set_id(c,m,k)


def set_id(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return
   text = m.text
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')

'''



