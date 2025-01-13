import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import wsPattern

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Work.settings')

application = get_wsgi_application()

port = os.environ.get('PORT', 8000)  # Ensure your app uses the correct port
  
