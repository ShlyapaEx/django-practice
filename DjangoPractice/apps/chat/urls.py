from django.urls import include, path
from .routers import chats_router, messages_router


urlpatterns = [
    path('', include(chats_router.urls)),
    path('', include(messages_router.urls))
]
