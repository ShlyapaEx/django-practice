from django.urls import include, path
from .routers import chats_router


urlpatterns = [
    path('', include(chats_router.urls))

]
