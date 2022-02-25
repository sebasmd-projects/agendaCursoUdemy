import json

from django.conf import global_settings
from django.core.exceptions import ImproperlyConfigured
from unipath import Path

BASE_DIR = Path(__file__).ancestor(3) 

with open("sensitive_data.json") as f: 
    value = json.loads(f.read())
     
def get_value(value_title, values=value): 
    try: 
        return values[value_title] 
    except: 
        msg = "El nombre o variable %s no existe" % value_title 
        raise ImproperlyConfigured(msg)
    
_ = lambda s: s

SECRET_KEY = get_value('SECRET_KEY') 

ROOT_URLCONF = get_value('ROOT_URLCONF')

WSGI_APPLICATION = get_value('WSGI_APPLICATION') 

LANGUAGE_CODE = get_value('LANGUAGE_CODE') 

TIME_ZONE = get_value('TIME_ZONE') 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DJANGO_APPS = ( 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
) 

LOCAL_APPS = (
    'applications.persona',
    'applications.home',
) 

THIRD_PARTY_APPS = (
    'rest_framework',
    'ckeditor',
) 

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS 

MIDDLEWARE = [ 
    'django.middleware.security.SecurityMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',    
    'django.middleware.common.CommonMiddleware', 
    'django.middleware.csrf.CsrfViewMiddleware', 
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', 
    'django.contrib.messages.middleware.MessageMiddleware', 
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  
] 

TEMPLATES = [ 
    { 
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        'DIRS': [BASE_DIR.child('templates')], 
        'APP_DIRS': True, 
        'OPTIONS': { 
            'context_processors': [ 
                'django.template.context_processors.debug', 
                'django.template.context_processors.request', 
                'django.contrib.auth.context_processors.auth', 
                'django.contrib.messages.context_processors.messages', 
            ], 
        }, 
    }, 
] 

AUTH_PASSWORD_VALIDATORS = [ 
    { 
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', 
    }, 
    { 
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 
    }, 
    { 
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', 
    }, 
    { 
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', 
    }, 
]

LANGUAGES = (
 ('es', _('Espanish')),
 ('en', _('English')),
)

USE_I18N = True 

USE_L10N = True

USE_TZ = True
