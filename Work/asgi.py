import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import wsPattern  # Assuming your WebSocket routes are defined here

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Work.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(wsPattern),  # Route WebSocket requests to the correct handler
})

# The port setting is managed by Render and should not be manually set in the ASGI file
