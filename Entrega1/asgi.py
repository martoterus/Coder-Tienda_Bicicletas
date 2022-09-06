import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing


                                                    #nombre proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Entrega1.settings')

#application = get_asgi_application()
application = ProtocolTypeRouter({"http": get_asgi_application(),"websocket": AuthMiddlewareStack(URLRouter(room.routing.websocket_urlpatterns) 
    )
})

