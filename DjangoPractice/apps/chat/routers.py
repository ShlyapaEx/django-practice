from rest_framework import routers
from .views import ChatAPIViewSet

chats_router = routers.SimpleRouter()
chats_router.register(r'chats', ChatAPIViewSet)
