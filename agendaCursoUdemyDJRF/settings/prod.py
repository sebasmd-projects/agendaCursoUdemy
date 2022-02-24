from .base import * 

DEBUG = True 

ALLOWED_HOSTS = ['',''] 

DATABASES = { 
   'default': { 
       'ENGINE': get_value('DB_ENGINE'), 
       'NAME': get_value('DB_NAME'), 
       'USER': get_value('DB_USER'), 
       'PASSWORD': get_value('DB_PASSWORD'), 
       'HOST': get_value('DB_HOST'), 
       'PORT': get_value('DB_PORT'), 
   } 
} 

STATIC_URL = '/static/' 

STATICFILES_DIRS = [BASE_DIR.child('static')] 

MEDIA_URL = '/media/' 

MEDIA_ROOT = BASE_DIR.child('media') 

EMAIL_HOST = get_value('EMAIL_HOST') 

EMAIL_HOST_USER = get_value('EMAIL_HOST_USER') 

EMAIL_HOST_PASSWORD = get_value('EMAIL_HOST_PASSWORD') 

EMAIL_PORT = get_value('EMAIL_PORT')

EMAIL_USE_TLS = True 