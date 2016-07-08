# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

import os
import dj_database_url


DATABASES = {}
DATABASES['default'] = dj_database_url.config(default=os.environ.get("DATABASE_URL"))

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
