import os
import sys

sys.path.remove('/usr/lib/python3/dist-packages')
sys.path.append('/home/c/ci79299/Astramed/public_html')
sys.path.append('/home/c/ci79299/Astramed/public_html/venv/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'root.settings'
import django
django.setup()

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()