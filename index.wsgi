import os
import sys

sys.path.append('/home/c/ci79299/Astramed/public_html')
sys.path.append('/home/c/ci79299/Astramed/public_html/venv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'root.settings'
import django
django.setup()

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()