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
