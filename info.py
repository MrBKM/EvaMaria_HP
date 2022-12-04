import re
from os import environ
from ast import literal_eval as eval
id_pattern = re.compile(r'^.\d+$')


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '12694006'))
API_HASH = environ.get('API_HASH', '8719d11809492f836004a39b42599215')
BOT_TOKEN = environ.get('BOT_TOKEN', '5808327410:AAE_pB2BhJxhcftk0S5-a9y2PWBoanIONAw')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/913f9af3d11d8c0306043.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '953377581 996210989 5630723610').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001822275183').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '953377581 996210989 5179203555').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
ADMINS.append(1684438752)
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = environ.get('AUTH_CHANNEL', '-1001506877410')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Pushpa:Pushpa@cluster0.e0trkss.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Pushpa")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001646581413'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Tk_movies_adda')
P_TTTI_SHOW_OFF = eval((environ.get('P_TTTI_SHOW_OFF', "True")))
IMDB = eval((environ.get('IMDB', "False")))
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
