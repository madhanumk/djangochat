from django.urls import re_path
from .consumer import ChatConsumer

# the empty string routes to ChatConsumer, which manages the chat functionality.
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<pk>\d+)/$', ChatConsumer.as_asgi()),
]