# portofolio/api/index.py

from vercel_wsgi import handle
from portofolio.wsgi import application  # ⬅️ pastikan ini sesuai nama project kamu

def handler(request, context):
    return handle(request, application)
