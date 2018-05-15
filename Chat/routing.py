from django.conf.urls import url

from Chat.consumers import ChatConsumer

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer),
]
