import os
import sys

# Place this project on the system path
path = '/opt/django-mpd-client/mpd'
if path not in sys.path:
    sys.path.append(path)

# Specify the settings file.
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

os.chdir(path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

