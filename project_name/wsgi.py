"""
WSGI config for where_ng project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from utility.utils import ENV_MODE




"""
    Since we can do more logic in our python file 
    
""""
if ENV_MODE == 'dev' or ENV_MODE == 'development':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings.production")

application = get_wsgi_application()
