# Author:ZJF
from .base import *
import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER': 'root',
        'PASSWORD': '123123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}



DEBUG = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


XADMIN_TITLE = 'Typeidea管理后台'
XADMIN_FOOTER_TITLE = 'power by zjf'