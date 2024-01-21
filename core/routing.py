from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter, ProtocolTypeRouter

from chatbox import routing

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
})
