from rest_framework import routers
from .views import ChatAPIViewSet, MessageAPIViewSet

chats_router = routers.SimpleRouter()
messages_router = routers.SimpleRouter()

chats_router.register(r'chats', ChatAPIViewSet)
messages_router.register(r'messages', MessageAPIViewSet)
