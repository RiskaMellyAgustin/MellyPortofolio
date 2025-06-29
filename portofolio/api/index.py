# api/index.py

from django.core.wsgi import get_wsgi_application
from asgiref.wsgi import WsgiToAsgi

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portofolio.settings")  # ganti kalau nama project bukan 'portofolio'

application = get_wsgi_application()
asgi_app = WsgiToAsgi(application)
