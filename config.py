# (c) ՏIᒪᗴᑎT ᘜᕼOՏT ⚡️ # Dont Remove Credit

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

DS_API_ID = int(environ.get("DS_API_ID", "36330180"))
DS_API_HASH = environ.get("DS_API_HASH", "afb7a21b5d2805604c2f514f172bcdb8")
DS_BOT_TOKEN = environ.get("DS_BOT_TOKEN", "8770518531:AAGuqpVU89THZ27z6_JQpkIsJ35FO3r0haA")
DS_BOT_USERNAME = environ.get("DS_BOT_USERNAME", "PornXwaliBot") # bot username without @
DS_LOG_CHANNEL = int(environ.get("DS_LOG_CHANNEL", "-1004365695836"))
DS_STICKER = environ.get("DS_STICKER", "")
DS_PIC = environ.get('DS_PIC', 'https://i.ibb.co/MDrBMh7b/tmpr4ymok7g.jpg')

# Database Channel For Text Or Caption Store 
DS_DESI_FILE_CHANNEL = int(environ.get("DS_DESI_FILE_CHANNEL", "-1004380244889"))
DS_VIDESI_FILE_CHANNEL = int(environ.get("DS_VIDESI_FILE_CHANNEL", "-1004334954233"))
FREE_LIMIT_DESI = 5
FREE_LIMIT_VIDESI = 3
PREMIUM_LIMIT_DESI = 40
PREMIUM_LIMIT_VIDESI = 15

# Bot Admins
try:
    DS_ADMINS=[]
    for x in (environ.get("DS_ADMINS", "8743131347").split()):
        DS_ADMINS.append(int(x))
except ValueError:
      raise Exception("Your Admins list does not contain valid integers.")
    
# Mongodb Database 
DS_DB_URI = environ.get("DS_DB_URI", "mongodb+srv://euthledemo:euthle.pass@cluster0.k5jdjvi.mongodb.net/?appName=Cluster0")
DS_DB_NAME = environ.get("DS_DB_NAME", "susant-botz")

# Force subscribe channel 
DS_AUTH_CHANNEL = int(environ.get('DS_AUTH_CHANNEL', '-1003897378101')) # give your force subscribe channel id here else leave it blank

# Verification Variables
DS_API = environ.get("DS_API", "f454aa0a0473907a126cdc6763f5dc53361c1c7a") # shortlink api
DS_URL = environ.get("DS_URL", "shortxlinks.com") # shortlink domain without https://
DS_VERIFY_TUTORIAL = environ.get("DS_VERIFY_TUTORIAL", "https://t.me/howtoopenCineZonelinks/5") # how to open link 
DS_VERIFICATION = bool(environ.get("DS_VERIFICATION", False)) # set True Or False and make sure spelling is correct and first letter capital.

# (c) ՏIᒪᗴᑎT ᘜᕼOՏT ⚡️ # Dont Remove Credit
