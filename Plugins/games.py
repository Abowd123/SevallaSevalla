import logging
'''


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''
import random,re, time, akinator, string
from threading import Thread 
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.games import *
from helpers.Ranks import isLockCommand
import asyncio
users_demon = {}
def is_what_percent_of(num_a, num_b):
    return (num_a / num_b) * 100

def get_top(users):
   users = [tuple(i.items()) for i in users]
   top = sorted(users, key=lambda i: i[-1][-1], reverse=True)
   top = [dict(i) for i in top]
   return top

@Client.on_message(filters.text & filters.group, group=33)
async def gamesHandler(c,m):
    k = await r.get(f'{Dev_Zaid}:botkey')
    channel = await r.get(f'{Dev_Zaid}:BotChannel') or 'yqyqy66'
    await gamesFunc(c,m,k,channel)

@Client.on_message(filters.dice & filters.group, group=45)
async def diceFunc(c,m):
   if await r.get(f'{m.chat.id}:disableGames:{Dev_Zaid}'):  return False
   if m.dice.emoji == "🎲":
     k = await r.get(f'{Dev_Zaid}:botkey')
     if m.dice.value == 6:
        await asyncio.sleep(3)
        ra = 100
        if await r.get(f'{m.from_user.id}:Floos'):
           get = int(await r.get(f'{m.from_user.id}:Floos'))
           await r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(await r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           await r.set(f'{m.from_user.id}:Floos',ra)
        return await m.reply(f'''
صح عليك فزت **[بالنرد]({m.link})** ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
💸فلوسك: `{floos}` ريال
☆
''', disable_web_page_preview=True)
     else:
        await asyncio.sleep(3)
        return await m.reply(f"{k} للأسف خسرت بالنرد")
   

async def gamesFunc(c,m,k,channel):
   if not await r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
       return
   if await r.get(f'{m.from_user.id}:gbangames:{Dev_Zaid}'):  return 
   if await r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or await r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if await r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not await admin_pls(m.from_user.id,m.chat.id):  return
   if await r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   text = m.text
   name = await r.get(f'{Dev_Zaid}:BotName') or 'فوق'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
     text = await r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if await r.get(f'Custom:{Dev_Zaid}&text={text}'):
     text = await r.get(f'Custom:{Dev_Zaid}&text={text}')
   if await r.get(f'{m.chat.id}:disableGames:{Dev_Zaid}'):  return
   
   if await r.get(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}'):
      if not re.findall('[0-9]+', text): 
        await r.delete(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}')
        return await m.reply(f'{k} لازم يكون ارقام')
      acc_id = int(re.findall('[0-9]+', text)[0])
      acc_id_from = int(await r.get(f'{m.from_user.id}:bankID'))
      if acc_id == acc_id_from:
        await r.delete(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}')
        return await m.reply(f'{k} مافيك تحول لنفسك')
      floos_to_trans = int(await r.get(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}'))
      await r.delete(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}')
      if not await r.sismember('BankList', m.from_user.id):
        return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
      if not await r.get(f'{m.from_user.id}:Floos'):
        floos = 0
      else:
        floos = int(await r.get(f'{m.from_user.id}:Floos'))
      if floos_to_trans > floos:
        return await m.reply(f'{k} فلوسك ماتكفي')
      else:
        if not await r.get(f'{acc_id}:getAccBank'):
          return await m.reply(f'{k} مافي حساب بنكي كذا')
        else:
          id_to = int(await r.get(f'{acc_id}:getAccBank'))
          if not await r.sismember('BankList', id_to):
            return await m.reply(f'{k} ماعنده حساب بأي بنك')
          if await r.get(f'{id_to}:bankName'):
            name_to = await r.get(f'{id_to}:bankName')[:10]
          else:
            gett = await c.get_users(int(await r.get(f'{acc_id}:getAccBank')))
            name_to = gett.first_name[:10]
            await r.set(f'{id_to}:bankName',name_to)
          if floos_to_trans == floos:
            await r.delete(f'{m.from_user.id}:Floos')
          else:
            await r.set(f'{m.from_user.id}:Floos',floos-floos_to_trans)
          bank_to = await r.get(f'{id_to}:bankType')
          bank_from = await r.get(f'{m.from_user.id}:bankType')
          name_from = await r.get(f'{m.from_user.id}:bankName')[:10] or m.from_user.first_name[:10]
          mention_from = f'[{name_from}](tg://user?id={m.from_user.id})'
          mention_to = f'[{name_to}](tg://user?id={id_to})'
          if not await r.get(f'{id_to}:Floos'):
            floos_to = 0
          else:
            floos_to = int(await r.get(f'{id_to}:Floos'))
          txt = 'حوالة صادرة\n\nمن: {}\nحساب رقم: {}\nبنك: {}\nالى: {}\nحساب رقم: {}\nبنك: {}'.format(mention_from,acc_id_from,bank_from,mention_to,acc_id,bank_to)
          if bank_from != bank_to:
             floos_to_tran = int(floos_to_trans-floos_to_trans/10)
             txt += '\nخصمت 10% ضريبة بنك الى بنك'
             txt += f'\nالمبلغ: {floos_to_tran} ريال 💸'
          else:
             floos_to_tran = floos_to_trans
             txt += f'\nالمبلغ: {floos_to_tran} ريال 💸'
          await r.set(f'{id_to}:Floos',floos_to+floos_to_tran)
          return await m.reply(txt, disable_web_page_preview=True)

   if await r.get(f'{m.from_user.id}:createBank:{m.chat.id}'):
     await r.delete(f'{m.from_user.id}:createBank:{m.chat.id}')
     if await r.get(f'{m.from_user.id}:bankID'):
       id = int(await r.get(f'{m.from_user.id}:bankID'))
       floos_to_add = 0
     else:
       id = '4'
       floos_to_add = 2000
       for a in range(15):
         id += str(random.randint(1,9))
     if not await r.get(f'{m.from_user.id}:Floos'):
       floos = 0
     else:
       floos = int(await r.get(f'{m.from_user.id}:Floos'))
     '''
     if not text in ['الاهلي','راجحي', 'الانماء','عبد الفتاح السيسي']:
       return await m.reply(f'{k} مافيه بنك بهالاسم')
     '''
     if not text in ['الاهلي','راجحي', 'الانماء']:
       return await m.reply(f'{k} مافيه بنك بهالاسم')
     card = random.choice(['الاهلي كارد','الراجحي كارد','الإنماء كارد','مدى كارد'])
     if text == 'الاهلي':
        await r.set(f'{m.from_user.id}:bankType', 'الاهلي')
        await r.set(f'{m.from_user.id}:bankID', int(id))
        await r.set(f'{m.from_user.id}:bankCard',card)
     if text == 'راجحي':
        await r.set(f'{m.from_user.id}:bankType', 'راجحي')
        await r.set(f'{m.from_user.id}:bankID', int(id))
        await r.set(f'{m.from_user.id}:bankCard',card)
     if text == 'الانماء':
        await r.set(f'{m.from_user.id}:bankType', 'الانماء')
        await r.set(f'{m.from_user.id}:bankID', int(id))
        await r.set(f'{m.from_user.id}:bankCard',card)
     '''
     if text == 'عبد الفتاح السيسي':
        await r.set(f'{m.from_user.id}:bankType', 'بلحة الدولي')
        await r.set(f'{m.from_user.id}:bankID', int(id))
        await r.set(f'{m.from_user.id}:bankCard','بطاقة تموين')
        card = 'بطاقة تموين'
        await r.sadd('BankList', m.from_user.id)
        await r.set(f'{id}:getAccBank', m.from_user.id)
        fff = floos + floos_to_add
        await r.set(f'{m.from_user.id}:Floos',fff)
        await r.set(f'{m.from_user.id}:bankName',m.from_user.first_name)
        await m.reply(f'• وسوينا لك حساب في بنك {text}\n\n{k} رقم حسابك ↢ ( `{id}` )\n{k} نوع البطاقة ↢ ( {card} )\n{k} فلوسك ↢ ( {fff} ريال 💸 )\n\n{k} هتدفع!! هتشوف الي مشفتهوش، دا لو هتدفع!، انما ببلاش دا انا معرفش حاجة اسمها ببلاش')
        if await r.get(f'DevGroup:{Dev_Zaid}'):
          return await c.send_message(int(await r.get(f'DevGroup:{Dev_Zaid}')),
           f' ⟨ {m.from_user.mention} ⟩\n{k} سوى حساب بالبنك\n{k} رقم حسابه ( `{id}` )')
        else:
          return 
     '''
     await r.sadd('BankList', m.from_user.id)
     await r.set(f'{id}:getAccBank', m.from_user.id)
     fff = floos + floos_to_add
     await r.set(f'{m.from_user.id}:Floos',fff)
     await r.set(f'{m.from_user.id}:bankName',m.from_user.first_name)
     await m.reply(f'• وسوينا لك حساب في بنك {text}\n\n{k} رقم حسابك ↢ ( `{id}` )\n{k} نوع البطاقة ↢ ( {card} )\n{k} فلوسك ↢ ( {fff} ريال 💸 )')
     if await r.get(f'DevGroup:{Dev_Zaid}'):
         await c.send_message(int(await r.get(f'DevGroup:{Dev_Zaid}')),
           f' ⟨ {m.from_user.mention} ⟩\n{k} سوى حساب بالبنك\n{k} رقم حسابه ( `{id}` )')
   
   if text == 'توب' or text == 'التوب':
     await m.reply(f'{k} اهلين فيك في قوائم التوب\nللاستفسار - @{channel}',
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('توب الفلوس 💸', callback_data=f'topfloos:{m.from_user.id}'),
         InlineKeyboardButton ('توب الحرامية 💰', callback_data=f'topzrf:{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('🧚‍♀️',url=f't.me/{channel}')
       ]
       ]
     ))
   
   if text == 'توب الفلوس':
     if not await r.smembers('BankList'):
       return await m.reply(f'{k} مافيه حسابات بالبنك')
     else:
       rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
       )
       if await r.get('BankTop'):
          text = await r.get('BankTop')
          if not await r.get(f'{m.from_user.id}:Floos'):
            floos = 0
          else:
            floos = int(await r.get(f'{m.from_user.id}:Floos'))
          get = await r.ttl('BankTop')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {floos:,} 💸 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          return await m.reply(text, disable_web_page_preview=True,reply_markup=rep)
       else:
          users = []
          ccc = 0
          for user in await r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if await r.get(f'{id}:bankName'):
              name = await r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = await c.get_chat(id).first_name
                await r.set(f'{id}:bankName',name)
              except Exception:
                name = 'INVALID_NAME'
                await r.set(f'{id}:bankName',name)
            if not await r.get(f'{id}:Floos'):
              floos = 0
            else:
              floos = int(await r.get(f'{id}:Floos'))
            users.append({'name':name, 'money':floos})
          top = get_top(users)
          text = 'توب 20 اغنى اشخاص:\n\n'
          count = 0
          for user in top:
            count += 1
            if count == 21:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'**{emoji}{floos:,}** 💸 l {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
          await r.set('BankTop',text,ex=300)
          if not await r.get(f'{m.from_user.id}:Floos'):
            floos_from_user = 0
          else:
            floos_from_user = int(await r.get(f'{m.from_user.id}:Floos'))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {floos_from_user:,} 💸 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          get = await r.ttl('BankTop')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          return await m.reply(text,disable_web_page_preview=True,reply_markup=rep)
   
   
   if text == 'توب الحراميه' or text == 'توب الحرامية' or text == 'توب الزرف':
     if not await r.smembers('BankList'):
       return await m.reply(f'{k} مافيه حسابات بالبنك')
     else:
       rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
       )
       if await r.get('BankTopZRF'):
          text = await r.get('BankTopZRF')
          if not await r.get(f'{m.from_user.id}:Zrf'):
            zrf = 0
          else:
            zrf = int(await r.get(f'{m.from_user.id}:Zrf'))
          get = await r.ttl('BankTopZRF')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {zrf:,} 💰 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          return await m.reply(text, disable_web_page_preview=True,reply_markup=rep)
       else:
          users = []
          ccc = 0
          for user in await r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if await r.get(f'{id}:bankName'):
              name = await r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = await c.get_chat(id).first_name
                await r.set(f'{id}:bankName',name)
              except Exception:
                name = 'INVALID_NAME'
                await r.set(f'{id}:bankName',name)
            if not await r.get(f'{id}:Zrf'):
              zrf = 0
            else:
              zrf = int(await r.get(f'{id}:Zrf'))
            users.append({'name':name, 'money':zrf})
          top = get_top(users)
          text = 'توب 20 اكثر الحراميه زرفًا:\n\n'
          count = 0
          for user in top:
            count += 1
            if count == 21:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'**{emoji}{floos:,}** 💰 l⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
          await r.set('BankTopZRF',text,ex=300)
          if not await r.get(f'{m.from_user.id}:Zrf'):
            floos_from_user = 0
          else:
            floos_from_user = int(await r.get(f'{m.from_user.id}:Zrf'))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {floos_from_user:,} 💰 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          get = await r.ttl('BankTopZRF')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          await m.reply(text,disable_web_page_preview=True,reply_markup=rep)
   
   if text == 'زواجات' or text == 'توب زواجات' or text == 'توب الزواجات':
     if not await r.smembers(f'{m.chat.id}:zwag:{Dev_Zaid}'):
        return await m.reply(f'{k} محد متزوج بالقروب')
     else:
        #await r.sadd(f'{m.chat.id}:zwag:{Dev_Zaid}', f'{m.reply_to_message.from_user.id}--{m.from_user.id}&&floos={floos}')
        users = []
        ccc = 0
        for marriage in await r.smembers(f'{m.chat.id}:zwag:{Dev_Zaid}'):
           user_id_1 = int(marriage.split('--')[0])
           user_id_2 = int(marriage.split('--')[1].split('&&')[0])
           money = int(marriage.split('&&floos=')[1])
           ccc += 1
           if await r.get(f'{user_id_1}:bankName'):
              name_1 = await r.get(f'{user_id_1}:bankName')[:10]
           else:
              try:
                name_1 = await c.get_chat(id).first_name[:10]
                await r.set(f'{user_id_1}:bankName',name_1)
              except Exception:
                name_1 = 'INVALID_NAME'
                await r.set(f'{user_id_1}:bankName',name_1)
           if await r.get(f'{user_id_2}:bankName'):
              name_2 = await r.get(f'{user_id_2}:bankName')[:10]
           else:
              try:
                name_2 = await c.get_chat(id).first_name[:10]
                await r.set(f'{user_id_2}:bankName',name_2)
              except Exception:
                name_2 = 'INVALID_NAME'
                await r.set(f'{user_id_2}:bankName',name_2)
           users.append({'name_1':name_1, 'name_2':name_2,'money':money})
        top = get_top(users)
        text = 'توب 20 اغلى زواجات بالقروب:\n\n'
        count = 0
        for user in top:
          count += 1
          if count == 21:
            break 
          emoji = get_emoji_bank(count)
          money = user['money']
          name_1 = user['name_1']
          name_2 = user['name_2']
          text += f'**{emoji}**👫 ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name_1} 💕 {name_2} |\n**💸 {money:,}**\n'
        text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
        return await m.reply(text, disable_web_page_preview=True)
           
   
   '''
   if text == 'تصفير التوب':
     if devp_pls(m.from_user.id,m.chat.id):
       if not await r.get('BankTop'):
         return await m.reply('اكتب توب الفلوس وارجع حاول')
       if not await r.get('BankTopZRF'):
         return await m.reply('اكتب توب الحراميه وارجع حاول')
       else:
         await m.reply(f'{k} ابشر صفرت التوب')
         users = []
         ccc = 0
         for user in await r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if await r.get(f'{id}:bankName'):
              name = await r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = await c.get_chat(id).first_name
                await r.set(f'{id}:bankName',name)
              except Exception:
                name = 'INVALID_NAME'
                await r.set(f'{id}:bankName',name)
            if not await r.get(f'{id}:Zrf'):
              zrf = 0
            else:
              zrf = int(await r.get(f'{id}:Zrf'))
            users.append({'name':name, 'money':zrf})
         top = get_top(users)
         text = ''
         count = 0
         for user in top:
            count += 1
            if count == 3:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'{emoji}{floos} 💰 l {name}\n'
         await r.set(f'BankTopLastZrf',text)
         users = []
         ccc = 0
         for user in await r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if await r.get(f'{id}:bankName'):
              name = await r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = await c.get_chat(id).first_name
                await r.set(f'{id}:bankName',name)
              except Exception:
                name = 'INVALID_NAME'
                await r.set(f'{id}:bankName',name)
            if not await r.get(f'{id}:Floos'):
              floos = 0
            else:
              floos = int(await r.get(f'{id}:Floos'))
         users.append({'name':name, 'money':floos})
         top = get_top(users)
         text = ''
         count = 0
         for user in top:
            count += 1
            if count == 3:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'**{emoji}{floos}** 💸 l {name}\n'
         await r.set(f'BankTopLast',text)
         keys = await r.keys('*:Floos')
         for a in keys:
           await r.delete(a)
   '''
   
   if text == 'حسابي':
     if not await r.sismember('BankList', m.from_user.id):
       return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     else:
       card = await r.get(f'{m.from_user.id}:bankCard')
       id = int(await r.get(f'{m.from_user.id}:bankID'))
       bank = await r.get(f'{m.from_user.id}:bankType')
       if not await r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(await r.get(f'{m.from_user.id}:Floos'))
       if await r.get(f'{m.from_user.id}:bankName'):
         name = await r.get(f'{m.from_user.id}:bankName')
       else:
         name = m.from_user.first_name
       await m.reply(f'''{k} الاسم ↢ ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
{k} الحساب ↢ `{id}`
{k} بنك ↢ ( {bank} )
{k} نوع ↢ ( {card} )
{k} الرصيد ↢ ( {floos} ريال 💸 )
☆''')
   
   if text == 'انشاء حساب بنكي':
     if await r.sismember('BankList', m.from_user.id):
       bank = await r.get(f'{m.from_user.id}:bankType')
       acc_id = int(await r.get(f'{m.from_user.id}:bankID'))
       return await m.reply(f'{k} عندك حساب في بنك {bank}\n\n{k} لتفاصيل اكثر اكتب\n{k} `حساب {acc_id}`')
     else:
       await r.set(f'{m.from_user.id}:createBank:{m.chat.id}',1,ex=300)
       '''
       return await m.reply(f'– عشان تسوي حساب لازم تختار بنك\n\n{k} `الاهلي`\n{k} `راجحي`\n{k} `الانماء`\n{k} `عبد الفتاح السيسي`\n\n- اضغط للنسخ')
       '''
       return await m.reply(f'– عشان تسوي حساب لازم تختار بنك\n\n{k} `الاهلي`\n{k} `راجحي`\n{k} `الانماء`\n\n- اضغط للنسخ')
       
   
   if text == 'مسح حسابي':
     if not await r.sismember('BankList', m.from_user.id):
       return await m.reply(f'{k} ماعندك حساب بنكي')
     else:
       await r.srem('BankList', m.from_user.id)
       await m.reply(f'{k} تم حذف حسابك البنكي')
   
   if text.startswith('حساب ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
      acc_id = int(re.findall('[0-9]+', text)[0])
      if await r.get(f'{acc_id}:getAccBank'):
         id = int(await r.get(f'{acc_id}:getAccBank'))
         if await r.get(f'{id}:bankName'):
           name = await r.get(f'{id}:bankName')[:10]
         else:
           gett = await c.get_users(int(await r.get(f'{acc_id}:getAccBank')))
           name = gett.first_name
           await r.set(f'{id}:bankName',name)
         bank = await r.get(f'{id}:bankType')
         card = await r.get(f'{id}:bankCard')
         if not await r.get(f'{id}:Floos'):
           floos = 0
         else:
           floos = int(await r.get(f'{id}:Floos'))
         await m.reply(f'''
{k} الاسم ↢ ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
{k} الحساب ↢ `{acc_id}`
{k} بنك ↢ ( {bank} )
{k} نوع ↢ ( {card} )
{k} الرصيد ↢ ( `{floos}` ريال 💸 )
☆
''')
   
   if text.startswith('تحويل ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
      floos_to_trans = int(re.findall('[0-9]+', text)[0])
      if not await r.get(f'{m.from_user.id}:Floos'):
        floos = 0
      else:
        floos = int(await r.get(f'{m.from_user.id}:Floos'))
      if floos_to_trans < 200:
        return await m.reply(f'{k} الحد الادنى المسموح هو 200 ريال')
      else:
        if floos_to_trans > floos:
          return await m.reply(f'{k} فلوسك ماتكفي')
        if not await r.sismember('BankList', m.from_user.id):
          return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
        else:
          await r.set(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}',floos_to_trans, ex=600)
          return await m.reply(f'{k} ارسل الحين رقم حساب البنكي الي تبي تحول له')
   
      
      
   if text.startswith('حظ ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
     if not await r.sismember('BankList', m.from_user.id):
       return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if await r.get(f'{m.from_user.id}:BankWaitHZ'):
       get = await r.ttl(f'{m.from_user.id}:BankWaitHZ')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return await m.reply(f'{k} مايمديك تلعب لعبة الحظ الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not await r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(await r.get(f'{m.from_user.id}:Floos'))
       floos_to_hz = int(re.findall('[0-9]+', text)[0])
       if floos_to_hz == 0:
         return await m.reply(f'{k} مايمدي تلعب بالصفر')
       if floos_to_hz > floos:
         return await m.reply(f'{k} فلوسك ماتكفي')
       else:
         await r.set(f'{m.from_user.id}:BankWaitHZ',1,ex=600)
         hzz = random.choice(['yes','no'])
         if hzz == 'yes':
           fls = floos_to_hz
           floos_com = floos+fls
           await r.set(f'{m.from_user.id}:Floos', floos+fls)
           return await m.reply(f'{k} مبروك فزت بالحظ !\n{k} فلوسك قبل ↢ ( **{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{floos_com}** ريال 💸 )')
         else:
           fls = floos-floos_to_hz
           if fls == 0:
              await r.delete(f'{m.from_user.id}:Floos')
           else:
              await r.set(f'{m.from_user.id}:Floos', fls)
           return await m.reply(f'{k} للأسف خسرت بالحظ !\n{k} فلوسك قبل ↢ ( **{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{fls}** ريال 💸 )')
   
   
   if text == "حظ فلوسي":
     if not await r.sismember('BankList', m.from_user.id):
       return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if await r.get(f'{m.from_user.id}:BankWaitHZ'):
       get = await r.ttl(f'{m.from_user.id}:BankWaitHZ')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return await m.reply(f'{k} مايمديك تلعب لعبة الحظ الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not await r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(await r.get(f'{m.from_user.id}:Floos'))
       floos_to_hz = floos
       if floos_to_hz == 0:
         return await m.reply(f'{k} مايمدي تلعب بالصفر')
       else:
         await r.set(f'{m.from_user.id}:BankWaitHZ',1,ex=600)
         hzz = random.choice(['yes','no'])
         if hzz == 'yes':
           fls = floos_to_hz
           floos_com = floos+fls
           await r.set(f'{m.from_user.id}:Floos', floos+fls)
           return await m.reply(f'{k} مبروك فزت بالحظ !\n{k} فلوسك قبل ↢ ( **{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{floos_com}** ريال 💸 )')
         else:
           fls = floos-floos_to_hz
           if fls == 0:
              await r.delete(f'{m.from_user.id}:Floos')
           else:
              await r.set(f'{m.from_user.id}:Floos', fls)
           return await m.reply(f'{k} للأسف خسرت بالحظ !\n{k} فلوسك قبل ↢ ( "**{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{fls}** ريال 💸 )')

   if text == 'عجله' or text == 'عجلة':
     if not await r.sismember('BankList', m.from_user.id):
       return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     else:
       if await r.get(f'{m.from_user.id}:BankWait3JL'):
         get = await r.ttl(f'{m.from_user.id}:BankWait3JL')
         wait = time.strftime('%M:%S', time.gmtime(get))
         return await m.reply(f'{k} مايمديك تلعب عجلة الحين ! \n{k} تعال بعد {wait} دقيقة')
       else:
         await r.set(f'{m.from_user.id}:BankWait3JL',1,ex=300)
         rep = await m.reply(f'{k} حلف العجلة بعد ٣ ثواني',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('³',callback_data='None')]]))
         await asyncio.sleep(1)
         await rep.edit_text(f'{k} حلف العجلة بعد ثانيتين',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('²',callback_data='None')]]))
         await asyncio.sleep(1)
         await rep.edit_text(f'{k} حلف العجلة بعد ثانية',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('¹',callback_data='None')]]))
         await asyncio.sleep(1)
         emojis_3jl = [
         '💸','💸','💸','💸','💸','💸','💸',
         '💸','💸','💸','💸','💸','💸','💸',
         '⚡','⚡','⚡','⚡','⚡','⚡','⚡',
         '⚡','⚡','⚡','⚡','⚡','⚡','⚡',
         '💣','💣','💣','💣','💣','💣','💣',
         '💣','💣','💣','💣','💣','💣','💣',
         '🍒','🍒','🍒','🍒','🍒','🍒','🍒',
         '🍒','🍒','🍒','🍒','🍒','🍒','🍒',
         '💎','💎','💎','💎','💎','💎','💎',
         '💎','💎','💎','💎','💎','💎','💎'
         ]
         emoji1 = random.choice(emojis_3jl)
         emoji2 = random.choice(emojis_3jl)
         emoji3 = random.choice(emojis_3jl)
         reply_ma = InlineKeyboardMarkup (
           [
             [
               InlineKeyboardButton (emoji1, callback_data='None'),
               InlineKeyboardButton (emoji2, callback_data='None'),
               InlineKeyboardButton (emoji3, callback_data='None'),
             ],
             [
               InlineKeyboardButton ('🫦', url=f't.me/{channel}')
             ]
           ]
         )
         if emoji1 == emoji2 and emoji2 == emoji3:
            chance = random.choice([100000, 200000, 300000])
            if not await r.get(f'{m.from_user.id}:Floos'):
              floos = 0
            else:
              floos = int(await r.get(f'{m.from_user.id}:Floos'))
            await rep.edit_text(f'{k} فزت بعجلة الحظ!\n\n{k} مبلغ الربح ( {chance} ريال 💸 )\n{k} فلوسك قبل ( `{floos}` ريال 💸 )\n{k} فلوسك الحين ( `{floos+chance}` ريال 💸 )',reply_markup=reply_ma)
            await r.set(f'{m.from_user.id}:Floos', floos+chance)
         else:
            chance = random.randint(100,1000)
            if not await r.get(f'{m.from_user.id}:Floos'):
              floos = 0
            else:
              floos = int(await r.get(f'{m.from_user.id}:Floos'))
            await rep.edit_text(f'{k} للأسف خسرت بعجلة الحظ!\n\n{k} خذ {chance} ريال عشان ماتصيح\n{k} فلوسك قبل ( `{floos}` ريال 💸 )\n{k} فلوسك الحين ( `{floos+chance}` ريال 💸 )',reply_markup=reply_ma)
            await r.set(f'{m.from_user.id}:Floos', floos+chance)
           
   if text.startswith('استثمار ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
     if not await r.sismember('BankList', m.from_user.id):
       return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if await r.get(f'{m.from_user.id}:BankWaitEST'):
       get = await r.ttl(f'{m.from_user.id}:BankWaitEST')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return await m.reply(f'{k} مايمديك تستثمر الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not await r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(await r.get(f'{m.from_user.id}:Floos'))
       floos_to_est = int(re.findall('[0-9]+', text)[0])
       if floos_to_est == 0:
         return await m.reply(f'{k} مايمدي تلعب بالصفر')
       if floos_to_est > floos:
         return await m.reply(f'{k} فلوسك ماتكفي')
       if floos_to_est < 2000:
         return await m.reply(f'{k} للأسف لازم تستثمر ب 2000 ريال عالأقل')
       else:
         await r.set(f'{m.from_user.id}:BankWaitEST',1,ex=300)
         one = int(floos_to_est/random.randint(1,9))
         rb7 = int(is_what_percent_of(one,floos_to_est))
         await r.set(f'{m.from_user.id}:Floos',floos+one)
         await m.reply(f'''
{k}  استثمار ناجح!
{k} نسبة الربح ↢ {rb7}%
{k} مبلغ الربح ↢ ( `{one}` ريال )
{k} فلوسك صارت ↢ ( `{floos+one}` ريال 💸 )
''')
   
   if text == "استثمار فلوسي":
     if not await r.sismember('BankList', m.from_user.id):
       return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if await r.get(f'{m.from_user.id}:BankWaitEST'):
       get = await r.ttl(f'{m.from_user.id}:BankWaitEST')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return await m.reply(f'{k} مايمديك تستثمر الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not await r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(await r.get(f'{m.from_user.id}:Floos'))
       floos_to_est = floos
       if floos_to_est == 0:
         return await m.reply(f'{k} مايمدي تستثمر بالصفر')
       if floos_to_est < 2000:
         return await m.reply(f'{k} للأسف لازم تستثمر ب 2000 ريال عالأقل')
       else:
         await r.set(f'{m.from_user.id}:BankWaitEST',1,ex=300)
         one = int(floos_to_est/random.randint(1,9))
         rb7 = int(is_what_percent_of(one,floos_to_est))
         await r.set(f'{m.from_user.id}:Floos',floos+one)
         await m.reply(f'''
{k}  استثمار ناجح!
{k} نسبة الربح ↢ {rb7}%
{k} مبلغ الربح ↢ ( `{one}` ريال )
{k} فلوسك صارت ↢ ( `{floos+one}` ريال 💸 )
''')
   
   if text == 'كنز':
     if not await r.sismember('BankList', m.from_user.id):
       return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if await r.get(f'{m.from_user.id}:BankWaitKNZ'):
       get = await r.ttl(f'{m.from_user.id}:BankWaitKNZ')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return await m.reply(f'{k} كنزك بينزل بعد {wait} دقيقة')
     else:
       if not await r.get(f'{m.from_user.id}:Floos'):
          floos = 0
       else:
          floos = int(await r.get(f'{m.from_user.id}:Floos'))
       knz = random.choice(knzs)
       money = knz['credit']
       name = knz['name']
       await r.set(f'{m.from_user.id}:BankWaitKNZ',1, ex=600)
       await r.set(f'{m.from_user.id}:Floos', floos+money)
       fls = floos+money
       return await m.reply(f'اشعار ايداع {m.from_user.mention(m.from_user.first_name[:10])}⁪⁬⁪⁬⁮⁪⁬⁪\nالمبلغ: **{money}** ريال\nالكنز: {name}\nنوع العملية: ربح كنز\nرصيدك الحين: **{fls}** ريال 💸')

   if text == 'بخشيش':
     if not await r.sismember('BankList', m.from_user.id):
       return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if await r.get(f'{m.from_user.id}:BankWaitB5'):
       get = await r.ttl(f'{m.from_user.id}:BankWaitB5')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return await m.reply(f'{k} مايمدي اعطيك بخشيش الحين\n{k} تعال بعد {wait} دقيقة')
     else:
       b5 = random.randint(5,1000)
       await r.set(f'{m.from_user.id}:BankWaitB5',1, ex=300)
       if not await r.get(f'{m.from_user.id}:Floos'):
          floos = 0
       else:
          floos = int(await r.get(f'{m.from_user.id}:Floos'))
       await r.set(f'{m.from_user.id}:Floos', floos+b5)
       await m.reply(f'{k} دلعتك وعطيتك {b5} ريال 💸')
       
   if text == 'راتب':
     if not await r.sismember('BankList', m.from_user.id):
       return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if await r.get(f'{m.from_user.id}:BankWait'):
       get = await r.ttl(f'{m.from_user.id}:BankWait')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return await m.reply(f'{k} راتبك بينزل بعد {wait} دقيقة')
     else:
       job = random.choice(jobs)
       money = job['credit']
       name = job['name']
       await r.set(f'{m.from_user.id}:BankWait',1, ex=300)
       if not await r.get(f'{m.from_user.id}:Floos'):
          floos = 0
       else:
          floos = int(await r.get(f'{m.from_user.id}:Floos'))
       await r.set(f'{m.from_user.id}:Floos', floos+money)
       fls = floos+money
       await m.reply(f'اشعار ايداع⁪⁬⁪⁬⁮⁪⁬⁪ {m.from_user.mention(m.from_user.first_name[:10])}\nالمبلغ: **{money}** ريال\nوظيفتك: {name}\nنوع العملية: اضافة راتب\nرصيدك الحين: **{fls}** ريال 💸')
   
   if text == 'زرف' and m.reply_to_message and m.reply_to_message.from_user:
     if m.reply_to_message.from_user.id == int(Dev_Zaid):
       return await m.reply('?')
     if not await r.sismember('BankList', m.from_user.id):
       return await m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if not await r.sismember('BankList', m.reply_to_message.from_user.id):
       return await m.reply(f'{k} ماعنده حساب بنكي')
     if m.reply_to_message.from_user.id == m.from_user.id:
       return await m.reply('تبي تزرف نفسك؟')
     if await r.get(f'{m.from_user.id}:BankWaitZRF'):
       get = await r.ttl(f'{m.from_user.id}:BankWaitZRF')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return await m.reply(f'{k} يولد انحش الشرطة للحين تدور عنك\n{k} يمديك تزرف مره ثانيه بعد {wait}')
     if await r.get(f'{m.reply_to_message.from_user.id}:BankWaitMZROF'):
       get = await r.ttl(f'{m.reply_to_message.from_user.id}:BankWaitMZROF')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return await m.reply(f'{k} ذا المسكين مزروف قبل شوي\n{k} يمديك تزرفه بعد {wait}')
     if not await r.get(f'{m.reply_to_message.from_user.id}:Floos'):
       return await m.reply(f'{k} مطفر مامعه ولا ريال')
     if int(await r.get(f'{m.reply_to_message.from_user.id}:Floos')) < 2000:
       return await m.reply(f'{k} مايمديك تزرفه لان فلوسه اقل من 2000 ريال')
     else:
       zrf = random.randint(50,1000)
       await r.set(f'{m.from_user.id}:BankWaitZRF',1,ex=300)
       await r.set(f'{m.reply_to_message.from_user.id}:BankWaitMZROF',1,ex=300)
       floos = int(await r.get(f'{m.reply_to_message.from_user.id}:Floos'))
       await r.set(f'{m.reply_to_message.from_user.id}:Floos',floos-zrf)
       await m.reply(f'{k} خذ يالحرامي زرفته {zrf} ريال 💸')
       if not await r.get(f'{m.from_user.id}:Floos'):
         floos_from_user = 0
       else:
         floos_from_user = int(await r.get(f'{m.from_user.id}:Floos'))
       await r.set(f'{m.from_user.id}:Floos',floos_from_user+zrf)
       await r.sadd('BankZrf',m.from_user.id)
       if await r.get(f'{m.from_user.id}:Zrf'):
          zrff = int(await r.get(f'{m.from_user.id}:Zrf'))
       else:
          zrff = 0
       await r.set(f'{m.from_user.id}:Zrf',zrff+zrf)
       try:
         await c.send_message(
           m.reply_to_message.from_user.id,
           f'الحق الحق حلالك!!\nذا الحرامي {m.from_user.mention}\nسرق منك ( {zrf} ريال 💸 )\n༄',
           reply_markup=InlineKeyboardMarkup (
             [[
               InlineKeyboardButton (m.chat.title, url=m.link)
             ]]
           )
           )
       except Exception:
         pass
       
  
   if text == 'تصفير البنك':
     if await devp_pls(m.from_user.id,m.chat.id):
        return await m.reply(f'{k} متأكد تبي تصفر البنك ؟',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('اي', callback_data='yes:del:bank')],[InlineKeyboardButton ('لا', callback_data='no:del:bank')]]))
   
   if text == 'فلوسي':
     if not await r.get(f'{m.from_user.id}:Floos'):
        await m.reply(f'{k} ماعندك فلوس ارسل الالعاب وابدا جمع الفلوس')
     else:
        floos = int(await r.get(f'{m.from_user.id}:Floos'))
        return await m.reply(f'{k} فلوسك `{floos}` ريال 💸')
   
   if text == 'فلوس':
     if not m.reply_to_message:
       if not await r.get(f'{m.from_user.id}:Floos'):
         return await m.reply(f'{k} ماعندك فلوس ارسل الالعاب وابدا جمع الفلوس')
       else:
         floos = int(await r.get(f'{m.from_user.id}:Floos'))
       return await m.reply(f'{k} فلوسك `{floos}` ريال 💸')
     else:
       if not await r.get(f'{m.reply_to_message.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(await r.get(f'{m.reply_to_message.from_user.id}:Floos'))
       return await m.reply(f'{k} فلوسه ↢ ( {floos} ريال 💸 )')
   
   if text.startswith('بيع فلوسي ') and len(text.split()) == 3 and re.findall('[0-9]+', text):
     if not await r.get(f'{m.from_user.id}:Floos'):
        await m.reply(f'{k} للاسف انت مطفر عندك 0 ريال')
     else:
        floos_to_sale = int(re.findall('[0-9]+', text)[0])
        floos = int(await r.get(f'{m.from_user.id}:Floos'))
        if floos_to_sale == 0:
         return await m.reply(f'{k} مايمدي تبيع صفر')
        if floos_to_sale > floos:
          return await m.reply(f'{k} للاسف انت مطفر عندك {floos} ريال')
        if floos_to_sale == floos:
           await r.delete(f'{m.from_user.id}:Floos')
        else:
           await r.set(f'{m.from_user.id}:Floos',floos-floos_to_sale)
        get = int(await r.get(f'{m.chat.id}:TotalMsgs:{m.from_user.id}{Dev_Zaid}'))
        rsayl = floos_to_sale * 20
        await r.set(f'{m.chat.id}:TotalMsgs:{m.from_user.id}{Dev_Zaid}', get+rsayl)
        await m.reply(f'{k} بعت ( {floos_to_sale} ريال 💸 ) من فلوسك\n{k} مجموع رسايلك الحين ( {get + rsayl} )\n☆')
   
   if text.startswith('اضف فلوس ') and len(text.split()) == 3 and re.findall('[0-9]+', text):
     if await dev2_pls(m.from_user.id,m.chat.id):
       if m.reply_to_message and m.reply_to_message.from_user:
          floos_to_add = int(re.findall('[0-9]+', text)[0])
          if not await r.get(f'{m.reply_to_message.from_user.id}:Floos'):
             await r.set(f'{m.reply_to_message.from_user.id}:Floos',floos_to_add)
          else:
             floos = int(await r.get(f'{m.reply_to_message.from_user.id}:Floos'))
             await r.set(f'{m.reply_to_message.from_user.id}:Floos',floos_to_add+floos)
          await m.reply(f'「 {m.reply_to_message.from_user.mention} 」\n{k} ضفت له ( {floos_to_add} ) ريال 💸')
   
   
   if text == 'استخراج الاكواد':
      if await devp_pls(m.from_user.id,m.chat.id):
         if await r.get(f'{Dev_Zaid}:codeWait'):
           t = await r.ttl(f'{Dev_Zaid}:codeWait')
           wait = time.strftime('%H:%M:%S', time.gmtime(t))
           return await m.reply(f'{k} استخرجت اكواد الكشط من شوي تعال بعد {wait}')
         else:
           txt = 'اكواد الكشط:\n'
           ccc = 1
           for none in range(10):
             code = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
             await r.set(f'{code}:CodeBank:{Dev_Zaid}',1,ex=7200)
             txt += f'{ccc} ) `{code}`\n'
             ccc += 1
           await r.set(f'{Dev_Zaid}:codeWait',1,ex=7200)
           txt += '\n~ الأكواد صالحة لساعتين فقط .'
           txt += '\n༄'
           return await m.reply(txt)
   
   if text.startswith('كشط ') and len(text.split()) == 2:
     code = text.split()[1]
     if not await r.get(f'{code}:CodeBank:{Dev_Zaid}'):
       return await m.reply(f'{k} الكود منتهي الصلاحيه او تابع لبوت ثاني')
     if await r.get(f'{m.from_user.id}:BankWaitKSHT:{Dev_Zaid}'):
       t = await r.ttl(f'{m.from_user.id}:BankWaitKSHT:{Dev_Zaid}')
       wait = time.strftime('%H:%M:%S', time.gmtime(t))
       return await m.reply(f'{k} كشطت كود من شوي تعال بعد {wait}')
     else:
       await r.delete(f'{code}:CodeBank:{Dev_Zaid}')
     if not await r.get(f'{m.from_user.id}:Floos'):
       floos_from_user = 0
     else:
       floos_from_user = int(await r.get(f'{m.from_user.id}:Floos'))
     chance = random.choice([1000000000, 2000000000, 3000000000])
     await r.set(f'{m.from_user.id}:Floos',floos_from_user+chance)
     await m.reply(f'{k} مبرووووك 🏆\n{k} كشطت الكود واخذت ( {chance} ريال 💸 )\n{k} فلوسك قبل ( `{floos_from_user}` ريال 💸 )\n{k} فلوسك الحين ( `{floos_from_user+chance}` ريال 💸 )')
     await r.set(f'{m.from_user.id}:BankWaitKSHT:{Dev_Zaid}',1,ex=7200)
     if await r.get(f'DevGroup:{Dev_Zaid}'):
       alert = f'𖡋 𝐍𝐀𝐌𝐄 ⌯ {m.from_user.mention}\n𖡋 𝐈𝐃 ⌯ `{m.from_user.id}`\n\nكشط الكود `{code}` وأخذ {chance} ريال 💸'
       await c.send_message(int(await r.get(f'DevGroup:{Dev_Zaid}')),alert)
   
   if text.startswith('زواج ') and re.findall('[0-9]+', text) and m.reply_to_message and m.reply_to_message.from_user and len(text.split()) == 2:
     if m.reply_to_message.from_user.id == c.me.id or m.reply_to_message.from_user.id == m.from_user.id:
       return await m.reply('?')
     if m.reply_to_message.from_user.is_bot:
       return False
     if await r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}'):
       getUser = await c.get_users(int(await r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}')))
       mention = getUser.mention
       return await m.reply(f'「 {mention} 」 \n{k} تعاليييي زوجك بيخونك')
     if await r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}'):
       getUser = await c.get_users(int(await r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}')))
       mention = getUser.mention
       return await m.reply(f'「 {mention} 」 \n{k} تعال زوجتك بتخونك')
     if not await r.get(f'{m.from_user.id}:Floos'):
       floos_from_user = 0
     else:
       floos_from_user = int(await r.get(f'{m.from_user.id}:Floos'))
     floos = int(re.findall('[0-9]+', text)[0])
     if floos > floos_from_user:
       return await m.reply('مطفر فلوسك ماتكفي')
     else:
       if await r.get(f'{m.reply_to_message.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}'):
         return await m.reply('「 {} 」 \n{} مو سنقل دورلك غيرها\n༄'.format(m.reply_to_message.from_user.mention,k))
       if await r.get(f'{m.reply_to_message.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}'):
         return await m.reply('「 {} 」 \n{} مو سنقل دورلك غيره\n༄'.format(m.reply_to_message.from_user.mention,k))
       else:
         if floos < 50000:
           return await m.reply('لازم المهر اقل شي 50 ألف ريال')
         else:
           if floos == floos_from_user:
             await r.delete(f'{m.from_user.id}:Floos')
           else:
             await r.set(f'{m.from_user.id}:Floos',floos_from_user-floos)
           await r.set(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}',m.reply_to_message.from_user.id)
           await r.set(f'{m.reply_to_message.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}',m.from_user.id)
           to_marry = '''
💒 وثيقة زواج

{k} 👰 العروس ↢ ( {one} )
{k} 🤵 العريس ↢ ( {two} )
'''
           to_marry += f'\n{k} 💸 المهر ↢ ( `{floos}` ريال )\n༄'
           await r.set(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}',to_marry)
           await r.set(f'{m.reply_to_message.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}',to_marry)
           await r.set(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}',floos)
           await r.set(f'{m.reply_to_message.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}',floos)
           await r.sadd(f'{m.chat.id}:zwag:{Dev_Zaid}', f'{m.reply_to_message.from_user.id}--{m.from_user.id}&&floos={floos}')
           return await m.reply(f'''
{k} باركووو للعرسان 

{k} 👰 العروس ↢ ( {m.reply_to_message.from_user.mention} )
{k} 🤵 العريس ↢ ( {m.from_user.mention} )

{k} 💸 المهر ↢ ( `{floos}` ريال )
☆
''')
           
           
   if text == 'زواجي':
     if not await r.get(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}'):
       return await m.reply(f'{k} انت سنقل')
     else:
       if await r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}'):
         getUser = await c.get_users(int(await r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}')))
         txt = await r.get(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}').format(k=k,two=m.from_user.mention(m.from_user.first_name[:10]),one=getUser.mention(getUser.first_name[:10]))
         return await m.reply(txt)
       if await r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}'):
         getUser = await c.get_users(int(await r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}')))
         txt = await r.get(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}').format(k=k,two=getUser.mention(getUser.first_name[:10]),one=m.from_user.mention(m.from_user.first_name[:10]))
         return await m.reply(txt)         
   
   if text == "سورس" or text == "السورس":
    return await m.reply_photo(
        "https://gcdnb.pbrd.co/images/bOMz1R4wG9xF.jpg",
        caption="سورس فلير حماية الكروبات، ارفعه مشرف بكروبك واحميها:",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("الدخول البوت 💥", url="https://t.me/w7G_BoT")]]
        )
    )
   
   if text== 'طلاق' and await r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}'):
     getUser = await c.get_users(int(await r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}')))
     floos = int(await r.get(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}'))
     await r.srem(f'{m.chat.id}:zwag:{Dev_Zaid}', f'{getUser.id}--{m.from_user.id}&&floos={floos}')
     if not await r.get(f'{getUser.id}:Floos'):
       floos_from_whife = 0
     else:
       floos_from_whife = int(await r.get(f'{getUser.id}:Floos'))
     await r.set(f'{getUser.id}:Floos', floos_from_whife+floos)
     await r.delete(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}')
     await r.delete(f'{getUser.id}:marriedWomen:{m.chat.id}{Dev_Zaid}')
     await r.delete(f'{getUser.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}')
     await r.delete(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}')
     await r.delete(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}')
     await r.delete(f'{getUser.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}')
     return await m.reply(f'{k} طلقتك من 「 {getUser.mention} 」\n{k} ضفت ( {floos} ريال 💸 ) لفلوسها')
     
   
   if text== 'خلع' and await r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}'):
     getUser = await c.get_users(int(await r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}')))
     floos = int(await r.get(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}'))
     await r.srem(f'{m.chat.id}:zwag:{Dev_Zaid}', f'{m.from_user.id}--{getUser.id}&&floos={floos}')
     if not await r.get(f'{getUser.id}:Floos'):
       floos_from_has = 0
     else:
       floos_from_has = int(await r.get(f'{getUser.id}:Floos'))
     await r.set(f'{getUser.id}:Floos', floos_from_has+floos)
     await r.delete(f'{getUser.id}:marriedMan:{m.chat.id}{Dev_Zaid}')
     await r.delete(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}')
     await r.delete(f'{getUser.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}')
     await r.delete(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}')
     await r.delete(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}')
     await r.delete(f'{getUser.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}')
     return await m.reply(f'{k} خلعتك من 「 {getUser.mention} 」\n{k} ورجعت له المهر ( {floos} ريال 💸 )')

   if text == 'كت' or text == 'تويت' or text == 'كت تويت':
      return await m.reply(random.choice(cut))
   
   if text == 'جمل':
     gmla = random.choice(gomal)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', gmla.replace(" '",""), ex=600)
     await m.reply(f'الجملة ↢ ( {gmla} )\n{k} اكتبها بدون فواصل')
   
   if await r.get(f'{m.chat.id}:gameEmoji:{Dev_Zaid}'):
     if text == await r.get(f'{m.chat.id}:gameEmoji:{Dev_Zaid}'):
        ra = random.randint(1,5)
        t = await r.ttl(f'{m.chat.id}:gameEmoji:{Dev_Zaid}')
        timeo = f"{20 - int(t)}.{random.randint(1,9)}"
        await r.delete(f'{m.chat.id}:gameEmoji:{Dev_Zaid}')
        if await r.get(f'{m.from_user.id}:Floos'):
           get = int(await r.get(f'{m.from_user.id}:Floos'))
           await r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(await r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           await r.set(f'{m.from_user.id}:Floos',ra)
        return await m.reply(f'''
صح عليك ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
⏰الوقت: {timeo} ثانية
💸فلوسك: {floos} ريال
☆
''')
   
   if await r.get(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}'):
    try:
     if int(text) == await r.get(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}'):
        ra = random.randint(1,5)
        t = await r.ttl(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}')
        timeo = f"{600 - int(t)}.{random.randint(1,9)}"
        await r.delete(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}')
        if await r.get(f'{m.from_user.id}:Floos'):
           get = int(await r.get(f'{m.from_user.id}:Floos'))
           await r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(await r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           await r.set(f'{m.from_user.id}:Floos',ra)
        return await m.reply(f'''
صح عليك ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
⏰الوقت: {timeo} ثانية
💸فلوسك: {floos} ريال
☆
''')
     else:
        await r.delete(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}')
        return await m.reply(f'{k} اجابتك خطأ')
    except Exception:
     pass

   if await r.get(f'{m.chat.id}:game:{Dev_Zaid}'):
     if text == await r.get(f'{m.chat.id}:game:{Dev_Zaid}'):
        ra = random.randint(1,5)
        t = await r.ttl(f'{m.chat.id}:game:{Dev_Zaid}')
        timeo = f"{600 - int(t)}.{random.randint(1,9)}"
        await r.delete(f'{m.chat.id}:game:{Dev_Zaid}')
        if await r.get(f'{m.from_user.id}:Floos'):
           get = int(await r.get(f'{m.from_user.id}:Floos'))
           await r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(await r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           await r.set(f'{m.from_user.id}:Floos',ra)
        await m.reply(f'''
صح عليك ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
⏰الوقت: {timeo} ثانية
💸فلوسك: {floos} ريال
☆
''')
        return True
     
   
   if text == 'ترتيب':
     name = random.choice(trteep)
     name1 = name
     name = re.sub('سحور', 'س ر و ح', name)
     name = re.sub('سياره', 'ه ر س ي ا', name)
     name = re.sub('استقبال', 'ل ب ا ت ق س ا', name)
     name = re.sub('قنافه', 'ه ق ا ن ف', name)
     name = re.sub('ايفون', 'و ن ف ا', name)
     name = re.sub('بطاطس', 'ب ط ا ط س', name)
     name = re.sub('مطبخ', 'خ ب ط م', name)
     name = re.sub('كرستيانو', 'س ت ا ن و ك ر ي', name)
     name = re.sub('دجاجه', 'ج ج ا د ه', name)
     name = re.sub('مدرسه', 'ه م د ر س', name)
     name = re.sub('الوان', 'ن ا و ا ل', name)
     name = re.sub('غرفه', 'غ ه ر ف', name)
     name = re.sub('ثلاجه', 'ج ه ت ل ا', name)
     name = re.sub('قهوه', 'ه ق ه و', name)
     name = re.sub('سفينه', 'ه ن ف ي س', name)
     name = re.sub('مصر', 'ر م ص', name)
     name = re.sub('محطه', 'ه ط م ح', name)
     name = re.sub('طياره', 'ر ا ط ي ه', name)
     name = re.sub('رادار', 'ر ا ر ا د', name)
     name = re.sub('منزل', 'ن ز م ل', name)
     name = re.sub('مستشفى', 'ى ش س ف ت م', name)
     name = re.sub('كهرباء', 'ر ب ك ه ا ء', name)
     name = re.sub('تفاحه', 'ح ه ا ت ف', name)
     name = re.sub('اخطبوط', 'ط ب و ا خ ط', name)
     name = re.sub('سنترال', 'ن ر ت ل ا س', name)
     name = re.sub('فرنسا', 'ن ف ر س ا', name)
     name = re.sub('برتقاله', 'ر ت ق ب ا ه ل', name)
     name = re.sub('تفاح', 'ح ف ا ت', name)
     name = re.sub('مطرقه', 'ه ط م ر ق', name)
     name = re.sub('هريسه', 'س ه ر ي ه', name)
     name = re.sub('لبانه', 'ب ن ل ه ا', name)
     name = re.sub('شباك', 'ب ش ا ك', name)
     name = re.sub('باص', 'ص ا ب', name)
     name = re.sub('سمكه', 'ك س م ه', name)
     name = re.sub('ذباب', 'ب ا ب ذ', name)
     name = re.sub('تلفاز', 'ت ف ل ز ا', name)
     name = re.sub('حاسوب', 'س ا ح و ب', name)
     name = re.sub('انترنت', 'ا ت ن ر ن ت', name)
     name = re.sub('ساحه', 'ح ا ه س', name)
     name = re.sub('جسر', 'ر ج س', name)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     await m.reply(f'رتب ↢ {name}')
     return True
   
   if text == 'ايموجي':
      if await r.get(f'{m.chat.id}:gameEmoji:{Dev_Zaid}'):
        return await m.reply(f'{k} معليش في لعبة ايموجي شغالة الحين حاول بعد 20 ثانية\n\n{k} في حال ماتبي تكملها ارسل سكب')
      ran = random.choice(emojis_pics)
      emoji = ran['emoji']
      photo = ran['photo']
      a = await m.reply_photo(photo,caption='اسرع واحد يرسل الايموجي')
      await r.delete(f'{m.chat.id}:game:{Dev_Zaid}')
      await asyncio.sleep(3)
      await r.set(f'{m.chat.id}:gameEmoji:{Dev_Zaid}', emoji,ex=20)
      await a.edit_media(media=InputMediaPhoto (media='https://telegra.ph/file/b53b14951a50d7f75c39e.jpg', caption='ارسل الايموجي الحين'))
      return True
   
   if text == 'سكب':
      if await r.get(f'{m.chat.id}:gameEmoji:{Dev_Zaid}'):
         await r.delete(f'{m.chat.id}:gameEmoji:{Dev_Zaid}')
         await m.reply(f'{k} سكبت لعبه الايموجي')
         return True
   
   if text == 'انقليزي':
     name = random.choice(english)
     name1 = name
     name = re.sub("ذئب", "wolf", name)
     name = re.sub("معلومات", "information", name)
     name = re.sub("قنوات", "channels", name)
     name = re.sub("مجموعات", "groups", name)
     name = re.sub("كتاب", "book", name)
     name = re.sub("تفاحه", "apple", name)
     name = re.sub("مصر", "egypt", name)
     name = re.sub("فلوس", "money", name)
     name = re.sub("اعلم", "i know", name)
     name = re.sub("تمساح", "crocodile", name)
     name = re.sub("مختلف", "different", name)
     name = re.sub("ذكي", "intelligent", name)
     name = re.sub("كلب", "dog", name)
     name = re.sub("صقر", "falcon", name)
     name = re.sub("مشكله", "error", name)
     name = re.sub("كمبيوتر", "computer", name)
     name = re.sub("اصدقاء", "friends", name)
     name = re.sub("منضده", "table", name)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     await m.reply(f'اكتب معنى ↢ ( {name} )')
     return True
   
   if text == 'معاني':
     name = random.choice(m3any)
     name1 = name
     name = re.sub("قرد", "🐒", name)
     name = re.sub("دجاجه", "🐔", name)
     name = re.sub("بطريق", "🐧", name)
     name = re.sub("ضفدع", "🐸", name)
     name = re.sub("بومه", "🦉", name)
     name = re.sub("نحله", "🐝", name)
     name = re.sub("ديك", "🐓", name)
     name = re.sub("جمل", "🐫", name)
     name = re.sub("بقره", "🐄", name)
     name = re.sub("دولفين", "🐳", name)
     name = re.sub("تمساح", "🐊", name)
     name = re.sub("قرش", "🦈", name)
     name = re.sub("نمر", "🐅", name)
     name = re.sub("اخطبوط", "🐙", name)
     name = re.sub("سمكه", "🐟", name)
     name = re.sub("خفاش", "🦇", name)
     name = re.sub("اسد", "🦁", name)
     name = re.sub("فأر", "🐭", name)
     name = re.sub("ذئب", "🐺", name)
     name = re.sub("فراشه", "🦋", name)
     name = re.sub("عقرب", "🦂", name)
     name = re.sub("زرافه", "🦒", name)
     name = re.sub("قنفذ", "🦔", name)
     name = re.sub("تفاحه", "🍎", name)
     name = re.sub("باذنجان", "🍆", name)
     name = re.sub("قوس قزح", "🌈", name)
     name = re.sub("بزازه", "🍼", name)
     name = re.sub("بطيخ", "🍉", name)
     name = re.sub("وزه", "🦆", name)
     name = re.sub("كتكوت", "🐣", name)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     await m.reply(f'ايش معنى الايموجي ↢ ( {name} )')
     return True
   
   if text == 'احسب':
     name = random.choice(Maths)
     name1 = name
     name = re.sub("200", "250 - 50 = ?", name)
     name = re.sub("605", "655 - 50 = ?", name)
     name = re.sub("210", "247 - 37 = ?", name)
     name = re.sub("128", "168 - 40 = ?", name)
     name = re.sub("126", "202 - 76 = ?", name)
     name = re.sub("263", "31297 ÷ 119 = ?", name)
     name = re.sub("150", "246 - 96 = ?", name)
     name = re.sub("2000", "200 × 10 = ?", name)
     name = re.sub("40", "95 - 55 = ?", name)
     name = re.sub("242", "276 - 34 = ?", name)
     name = re.sub("14", "29 - 15 = ?", name)
     name = re.sub("13", "16 - 3 = ?", name)
     name = re.sub("1000", "956 + 44 = ?", name)
     name = re.sub("810", "767 + 43 = ?", name)
     name = re.sub("110", "77 + 33 = ?", name)
     name = re.sub("830", "745 + 85 = ?", name)
     name = re.sub("111", "66 + 45 = ?", name)
     name = re.sub("92", "61 + 31 = ?", name)
     name = re.sub("1110", "988 + 122 = ?", name)
     name = re.sub("6800", "85 × 80 = ?", name)
     name = re.sub("1554", "777 × 2 = ?", name)
     name = re.sub("920", "92 × 10 = ?", name)
     name = re.sub("1740", "87 × 20 = ?", name)
     name = re.sub("1140", "76 × 15 = ?", name)
     name = re.sub("1056", "88 × 12 = ?", name)
     name = re.sub("331", "243 + 88 = ?", name)
     name = re.sub("162", "250 - 88 = ?", name)
     name = re.sub("245", "290 - 45 = ?", name)
     name = re.sub("900", "975 - 75 = ?", name)
     name = re.sub("791", "878 - 87= ?", name)
     name = re.sub("0", "99 - 99 = ?", name)
     name = re.sub("57", "77 - 20 = ?", name)
     name = re.sub("220", "250 - 30 = ?", name)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     await m.reply(f'{name}')
     return True
   
   if text == 'عربي':
     name = random.choice(Arab)
     name1 = name
     name = re.sub("اناث", "انثى", name)
     name = re.sub("ثيران", "ثور", name)
     name = re.sub("دروس", "درس", name)
     name = re.sub("فحص", "فحوص", name)
     name = re.sub("رجال", "رجل", name)
     name = re.sub("كتب", "كتاب", name)
     name = re.sub("ضغوط", "ضغط", name)
     name = re.sub("صف", "صفوف", name)
     name = re.sub("عصفور", "عصافير", name)
     name = re.sub("لصوص", "لص", name)
     name = re.sub("تماسيح", "تمساح", name)
     name = re.sub("ملك", "ملوك", name)
     name = re.sub("فصل", "فصول", name)
     name = re.sub("كلاب", "كلب", name)
     name = re.sub("صقور", "صقر", name)
     name = re.sub("عقد", "عقود", name)
     name = re.sub("بحور", "بحر", name)
     name = re.sub("هاتف", "هواتف", name)
     name = re.sub("حدائق", "حديقه", name)
     name = re.sub("مسرح", "مسارح", name)
     name = re.sub("جرائم", "جريمة", name)
     name = re.sub("مدارس", "مدرسة", name)
     name = re.sub("منزل", "منازل", name)
     name = re.sub("كرسي", "كراسي", name)
     name = re.sub("مناطق", "منطقة", name)
     name = re.sub("بيوت", "بيت", name)
     name = re.sub("بنك", "بنوك", name)
     name = re.sub("علم", "علوم", name)
     name = re.sub("وظائف", "وظيفة", name)
     name = re.sub("طلاب", "طالب", name)
     name = re.sub("مراحل", "مرحلة", name)
     name = re.sub("فنانين", "فنان", name)
     name = re.sub("صواريخ", "صاروخ", name)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     await m.reply(f'اكتب جمع او مفرد ↢ ( {name} )')
     return True
   
   if text == 'كلمات':
     name = random.choice(words)
     '''
     name1 = name
     name = re.sub("ذئب", "ذئب", name)
     name = re.sub("معلومات", "معلومات", name)
     name = re.sub("قنوات", "قنوات", name)
     name = re.sub("مجموعات", "مجموعات", name)
     name = re.sub("كتاب", "كتاب", name)
     name = re.sub("تفاحه", "تفاحه", name)
     name = re.sub("مصر", "مصر", name)
     name = re.sub("فلوس", "فلوس", name)
     name = re.sub("اعلم", "اعلم", name)
     name = re.sub("تمساح", "تمساح", name)
     name = re.sub("مختلف", "مختلف", name)
     name = re.sub("ذكي", "ذكي", name)
     name = re.sub("كلب", "كلب", name)
     name = re.sub("صقر", "صقر", name)
     name = re.sub("مشكله", "مشكله", name)
     name = re.sub("كمبيوتر", "كمبيوتر", name)
     name = re.sub("اصدقاء", "اصدقاء", name)
     name = re.sub("منضده", "منضده", name)
     name = re.sub("سائق", "سائق", name)
     name = re.sub("جبل", "جبل", name)
     name = re.sub("مفتاح", "مفتاح", name)
     name = re.sub("يساوي", "يساوي", name)
     name = re.sub("انتبه", "انتبه", name)
     name = re.sub("موقد", "موقد", name)
     name = re.sub("مكتئب", "مكتئب", name)
     name = re.sub("انسان", "انسان", name)
     name = re.sub("ضفدع", "ضفدع", name)
     name = re.sub("عشق", "عشق", name)
     name = re.sub("منزل", "منزل", name)
     name = re.sub("طلاب", "طلاب", name)
     name = re.sub("فنان", "فنان", name)
     name = re.sub("صاروخ", "صاروخ", name)
     '''
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', name,ex=600)
     await m.reply(f'الكلمة ↢ ( {name} )')
     return True

   if text == 'تفكيك':
     tfkeek = random.choice(trteep)
     name = ' '.join(a for a in tfkeek)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', name,ex=600)
     await m.reply(f'فكك ↢ ( {tfkeek} )')
     return True
   
   
   if text == 'عواصم':
     country=random.choice(countries)
     name = country['name']
     capital=country['capital']
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', capital,ex=600)
     await m.reply(f'{k} ايش عاصمة {name} ؟')
     return True
   
   if text == 'اكمل':
     name = random.choice(mthal)
     name1 = name
     name = re.sub("اخوات", "لو قلبك مات متجيش على اتنين ... ", name)
     name = re.sub("زيهم", "اى ياعمهم اشتكيلك منهم تعمل ... ", name)
     name = re.sub("شمعتك", "دارى على ... تقيد", name)
     name = re.sub("داره", "من خرج من ... قل مقداره", name)
     name = re.sub("الوالدين", "رضا ... احسن من ابوك وامك", name)
     name = re.sub("الرءوس", "اذا تطاول الايدي تساوت ... ", name)
     name = re.sub("مرايه", "فى الوش ... وفى القفه سلايه", name)
     name = re.sub("حدو", "الشئ اللى يزيد عن ...  ينقلب لضدو", name)
     name = re.sub("رجالها", "مايجبها الا  ... ", name)
     name = re.sub("عدوك", "امشى عدل يحتار ... فيك", name)
     name = re.sub("الزبيب", "ضرب الحبيب زى اكل  ... ", name)
     name = re.sub("الغراب", "ياما جاب ...  لامه", name)
     name = re.sub("ماتو", "اللى اغتشو ... ", name)
     name = re.sub("اتمكن", "اتمسكن لحد ما ... ", name)
     name = re.sub("زجاج", "اللى بيتو من ... مايحدفش الناس بالطوب", name)
     name = re.sub("فار", "لو غاب القط العب يا ... ", name)
     name = re.sub("شهر", "امشي ... ولا تعدى نهر", name)
     name = re.sub("القتيل", "يقتل ... ويمشى فى جنازته", name)
     name = re.sub("الغطاس", "المايه تكدب ... ", name)
     name = re.sub("يكحلها", "جه ... عماها", name)
     name = re.sub("امه", "القرد فى عين ... غزال", name)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1 ,ex=600)
     await m.reply(f'اكمل ↢ ( {name} ؟ )')
     return True
   
   if text == 'احكام':
     if await r.get(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}'):
       return await m.reply(f"{k} معليش في لعبة احكام شغالة الحين حاول بعد دقيقة")
     await m.reply(f'''
{k} بدينا لعبة احكام واضفت اسمك 
{k} اللي يبي يلعب يرسل كلمة ( انا ) 

{k} اللي عليك انت صاحب اللعبة ترسل ( تم ) اذا اكتمل العدد
☆
''')
     await r.delete(f'{m.chat.id}:ListAhkam:{Dev_Zaid}')
     await r.set(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}',m.from_user.id,ex=120)
     await r.sadd(f'{m.chat.id}:ListAhkam:{Dev_Zaid}',m.from_user.id)
     return True
     
   if text == 'انا' and await r.get(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}'):
     if await r.sismember(f'{m.chat.id}:ListAhkam:{Dev_Zaid}',m.from_user.id):
       return await m.reply(f"{k} اسمك موجود بالقائمة")
     else:
       await m.reply(f"{k} ضفت اسمك للقائمة")
       await r.sadd(f'{m.chat.id}:ListAhkam:{Dev_Zaid}',m.from_user.id)
       return True
  
   if text == 'تم' and await r.get(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}') and m.from_user.id == int(await r.get(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}')):
     if len(await r.smembers(f'{m.chat.id}:ListAhkam:{Dev_Zaid}')) == 1:
       return await m.reply(f"{k} مافيه لاعبين")
     else:
       ids = [elem for elem in await r.smembers(f'{m.chat.id}:ListAhkam:{Dev_Zaid}')]
       id = random.choice(ids)
       getUser = await c.get_users(int(id))
       await m.reply(f"{k} تم اختيار ( ⁪⁬⁪⁬{getUser.mention} ) للحكم عليه")
       await r.delete(f'{m.chat.id}:ListAhkam:{Dev_Zaid}')
       await r.delete(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}')
       return True
   
   
   if text == 'روليت':
     if await r.get(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}'):
       return await m.reply(f"{k} معليش في لعبة روليت شغالة الحين حاول بعد دقيقة")
     await m.reply(f'''
{k} بدينا لعبة الروليت واضفت اسمك 
{k} اللي يبي يلعب يرسل كلمة ( انا ) 

{k} اللي عليك انت صاحب اللعبة ترسل ( تم ) اذا اكتمل العدد
☆
''')
     await r.delete(f'{m.chat.id}:ListRolet:{Dev_Zaid}')
     await r.set(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}',m.from_user.id,ex=120)
     await r.sadd(f'{m.chat.id}:ListRolet:{Dev_Zaid}',m.from_user.id)
     return True
     
   if text == 'انا' and await r.get(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}'):
     if await r.sismember(f'{m.chat.id}:ListRolet:{Dev_Zaid}',m.from_user.id):
       return await m.reply(f"{k} اسمك موجود بالقائمة")
     else:
       await m.reply(f"{k} ضفت اسمك للقائمة")
       await r.sadd(f'{m.chat.id}:ListRolet:{Dev_Zaid}',m.from_user.id)
       return True
  
   if text == 'تم' and await r.get(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}') and m.from_user.id == int(await r.get(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}')):
     if len(await r.smembers(f'{m.chat.id}:ListRolet:{Dev_Zaid}')) == 1:
       return await m.reply(f"{k} مافيه لاعبين")
     else:
       ids = [elem for elem in await r.smembers(f'{m.chat.id}:ListRolet:{Dev_Zaid}')]
       id = random.choice(ids)
       getUser = await c.get_users(int(id))
       await m.reply(f"{k} مبروك اخترت اللاعب ( {getUser.mention} ) واخذ 3 مجوهرات")
       if not await r.get(f'{getUser.id}:Floos'):
         floos = 0
       else:
         floos = int(await r.get(f'{getUser.id}:Floos'))
       await r.set(f"{getUser.id}:Floos",floos+10)
       await r.delete(f'{m.chat.id}:ListRolet:{Dev_Zaid}')
       await r.delete(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}')
       return True
       
  
   if text == 'خواتم':
     name = random.randint(1,6)
     await r.set(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}', name ,ex=600)
     await r.delete(f'{m.chat.id}:game:{Dev_Zaid}')
     return await m.reply('''
１    ２      ３     ４    ５     ６
  ↓     ↓      ↓     ↓     ↓     ↓
  ✋🏼 ‹› ✋🏼 ‹› ✋🏼 ‹› ✋🏼 ‹› ✋🏼 ‹› ✋🏼
  
  
⚘ اختار اليد اللي تتوقع فيها الخاتم
     ''')
   
   if text == 'اعلام':
     country=random.choice(countries_)
     name = country['name']
     flag=country['flag']
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', name,ex=600)
     await m.reply_photo(flag, caption='ايش اسم الدولة ؟')
     return True
   
   if text == 'دين':
     dee = random.choice(deen)
     question = dee['question']
     answer = dee['answer']
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', answer ,ex=600)
     await m.reply(question)
     return True
   
   if text == 'سيارات':
     car = random.choice(cars)
     brand = car["brand"]
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', brand ,ex=600)
     await m.reply_photo(car['photo'], caption='وش اسم السيارة ؟')
     return True
   
   if text == 'ارقام':
     num = ''
     for a in range(random.randint(5,15)):
       num += str(random.randint(1,9))
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', num ,ex=600)
     await m.reply(f'الرقم ↢ ( {num} )', protect_content=True)
     return True
     
   if text == 'انمي':
     anim = random.choice(anime)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', anim['anime'] ,ex=600)
     await m.reply_photo(anim['photo'], caption='ايش اسم شخصية الانمي ؟')
     return True
   
   if text == 'صور':
     ph = random.choice(pics)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', ph['answer'] ,ex=600)
     if not ph['caption']:
       caption = 'وش الي فالصورة؟'
     else:
       caption = ph['caption']
     await m.reply_photo(ph['photo'], caption=caption)
     return True
   
   if text == 'كرة قدم' or text == 'كره قدم':
     ph = random.choice(football)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', ph['answer'] ,ex=600)
     if not ph['caption']:
       caption = 'وش اسم الاعب ؟'
     else:
       caption = ph['caption']
     await m.reply_photo(ph['photo'], caption=caption)
     return True
   
   if text == 'تشفير':
     ph = random.choice(tashfeer)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', ph['answer'] ,ex=600)
     if not ph['caption']:
       caption = 'فك التشفير ؟'
     else:
       caption = ph['caption']
     await m.reply_photo(ph['photo'], caption=caption)
     return True
   
   if text == 'تركيب':
     name = random.choice(tarkeeb)
     name1 = name
     name = re.sub("اناث", "ا ن ا ث", name)
     name = re.sub("ثيران", "ث ي ر ا ن", name)
     name = re.sub("دروس", "د ر و س", name)
     name = re.sub("فحص", "ف ح ص", name)
     name = re.sub("رجال", "ر ج ا ل", name)
     name = re.sub("انستا", "ا ن س ت ا", name)
     name = re.sub("ضغوط", "ض غ و ط", name)
     name = re.sub("صف", "ص ف", name)
     name = re.sub("رجب", "ر ج ب", name)
     name = re.sub("اسد", "ا س د", name)
     name = re.sub("وقع", "و ق ع", name)
     name = re.sub("ملك", "م ل ك", name)
     name = re.sub("فصل", "ف ص ل", name)
     name = re.sub("كلاب", "ك ل ا ب", name)
     name = re.sub("صقور", "ص ق و ر", name)
     name = re.sub("عقد", "ع ق د", name)
     name = re.sub("بحور", "ب ح و ر", name)
     name = re.sub("هاتف", "ه ا ت ف", name)
     name = re.sub("حدائق", "ح د ا ئ ق", name)
     name = re.sub("مسرح", "م س ر ح", name)
     name = re.sub("جرائم", "ج ر ا ئ م", name)
     name = re.sub("مدارس", "م د ا ر س", name)
     name = re.sub("منزل", "م ن ز ل", name)
     name = re.sub("كرسي", "ك ر س ي", name)
     name = re.sub("مناطق", "م ن ا ط ق", name)
     name = re.sub("بيوت", "ب ي و ت", name)
     name = re.sub("بنك", "ب ن ك", name)
     name = re.sub("علم", "ع ل م", name)
     name = re.sub("وظائف", "و ظ ا ئ ف", name)
     name = re.sub("طلاب", "ط ل ا ب", name)
     name = re.sub("مراحل", "م ر ا ح ل", name)
     name = re.sub("فنانين", "ف ن ا ن ي ن", name)
     name = re.sub("صواريخ", "ص و ا ر ي خ", name)
     await r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     await m.reply(f'ركب ↢ ( {name} )')
   
   if text == "سكب ديمون":
    if m.from_user.id in users_demon:
        del users_demon[m.from_user.id]
        return await m.reply("⇜ ابشر الغيت اللعبة")
    else:
        return await m.reply("⇜ مافيه لعبة ديمون شغالة")
        
   if text == 'حجره' or text == 'حجرة':
     return await m.reply('- اختار حجره / ورقة / مقص',reply_markup=InlineKeyboardMarkup (
     [
     [
       InlineKeyboardButton ('🪨', callback_data=f'RPS:rock++{m.from_user.id}'),
       InlineKeyboardButton ('📃', callback_data=f'RPS:paper++{m.from_user.id}'),
       InlineKeyboardButton ('✂️', callback_data=f'RPS:scissors++{m.from_user.id}'),
     ]
     ]
     ))
   
   if text == 'نرد':
     dice = await c.send_dice(m.chat.id,"🎲",reply_to_message_id=m.id,
     reply_markup=InlineKeyboardMarkup (
       [[
         InlineKeyboardButton ("🧚‍♀️",url=f"t.me/{channel}")
       ]]
     ))
     if dice.dice.value == 6:
        ra = 10
        if await r.get(f'{m.from_user.id}:Floos'):
           get = int(await r.get(f'{m.from_user.id}:Floos'))
           await r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(await r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           await r.set(f'{m.from_user.id}:Floos',ra)
        return await m.reply(f'''
صح عليك فزت **[بالنرد]({dice.link})** ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
💸فلوسك: `{floos}` ريال
☆
''', disable_web_page_preview=True)
     else:
        return await m.reply(f"{k} للأسف خسرت بالنرد")
       
   
   if text == 'ديمون':
     if m.from_user.id in users_demon:
        return await m.reply("⇜ في لعبة ديمون شغالة استخدم امر <code>سكب ديمون</code>")
     else:
        return await m.reply(f'''بوو 👻
انا ديمون 🧛🏻‍♀️ اقدر اعرف مين الشخصية الي فبالك !

- فكر بشخص واضغط بدء وجاوب على اسئلتي''',
     reply_markup=InlineKeyboardMarkup (
       [
       [
        InlineKeyboardButton ('بدء 🧛🏻‍♀️',callback_data=f'start_aki:{m.from_user.id}')
       ]
       ]
     ))

@Client.on_callback_query(filters.regex('aki'))
async def akinatorHandler(c,m):
   channel = await r.get(f'{Dev_Zaid}:BotChannel') or 'yqyqy66'
   if m.data == f'start_aki:{m.from_user.id}':
    rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
       )
    await m.edit_message_text("⇜ جاري بدء اللعبة...",reply_markup=rep)
    aki= akinator.Akinator()
    q = aki.start_game(language="ar")
    users_demon.update({m.from_user.id:[aki,q]})
    return await m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))
   if m.data == f'aki_c:n++{m.from_user.id}':
    users_demon[m.from_user.id][1] = users_demon[m.from_user.id][0].answer("n")
    if users_demon[m.from_user.id][0].progression >= 65:
        users_demon[m.from_user.id][0].win()
        str_to_send = users_demon[m.from_user.id][0].first_guess
        logging.debug(str_to_send)
        await m.message.delete()
        rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
         )
        try: await c.send_photo(m.message.chat.id,str_to_send['absolute_picture_path'],caption=f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        except Exception: await c.send_message(m.message.chat.id,f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        del users_demon[m.from_user.id]
    else:
        return await m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))
   if m.data == f'aki_c:y++{m.from_user.id}':
    users_demon[m.from_user.id][1] = users_demon[m.from_user.id][0].answer("y")
    if users_demon[m.from_user.id][0].progression >= 65:
        users_demon[m.from_user.id][0].win()
        str_to_send = users_demon[m.from_user.id][0].first_guess
        logging.debug(str_to_send)
        await m.message.delete()
        rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
         )
        try: await c.send_photo(m.message.chat.id,str_to_send['absolute_picture_path'],caption=f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        except Exception: await c.send_message(m.message.chat.id,f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        del users_demon[m.from_user.id]
    else:
        return await m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))
   if m.data == f'aki_c:p++{m.from_user.id}':
    users_demon[m.from_user.id][1] = users_demon[m.from_user.id][0].answer("p")
    if users_demon[m.from_user.id][0].progression >= 65:
        users_demon[m.from_user.id][0].win()
        str_to_send = users_demon[m.from_user.id][0].first_guess
        logging.debug(str_to_send)
        await m.message.delete()
        rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
         )
        try: await c.send_photo(m.message.chat.id,str_to_send['absolute_picture_path'],caption=f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        except Exception: await c.send_message(m.message.chat.id,f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        del users_demon[m.from_user.id]
    else:
        return await m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))


def get_emoji_bank(count):
  if count == 1:
     return '🥇 ) '
  if count == 2:
     return '🥈 ) '
  if count == 3:
     return '🥉 ) '
  else:
     return f' {count}  ) '
     
     