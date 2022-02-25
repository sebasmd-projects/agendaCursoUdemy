"""
WSGI config for agendaCursoUdemyDJRF project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import json

from django.core.wsgi import get_wsgi_application
from django.core.exceptions import ImproperlyConfigured

with open("sensitive_data.json") as f: 
    value = json.loads(f.read())
     
def get_value(value_title, values=value): 
    try: 
        return values[value_title] 
    except: 
        msg = "El nombre o variable %s no existe" % value_title 
        raise ImproperlyConfigured(msg)

if get_value("ENVIRONMENT") == "local":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agendaCursoUdemyDJRF.settings.local')
    print("WSGI Environment: local")
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agendaCursoUdemyDJRF.settings.prod')
    print("WSGI Environment: prod")

application = get_wsgi_application()
