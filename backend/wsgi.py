"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

path = "/home/katherineLiberona/backendecommerce/backend"
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
if path not in sys.path:
    sys.path.append(path)
application = StaticFilesHandler(get_wsgi_application())
