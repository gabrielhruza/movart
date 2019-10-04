# settings.py
from .base import *

# Database

import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
   )
}

# Instagram

SOCIAL_AUTH_INSTAGRAM_KEY = 'bafa9911f3794994a6d8c1cc8bdbdd5b'      #Client ID
SOCIAL_AUTH_INSTAGRAM_SECRET = '2d4fcfe6b3f8468eabdba97a6eeceacb'   #Client SECRET
SOCIAL_AUTH_INSTAGRAM_EXTRA_DATA = [('user', 'user'),]
