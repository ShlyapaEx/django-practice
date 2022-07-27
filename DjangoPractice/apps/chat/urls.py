from django.urls import path

from .views import ChatAPIView

urlpatterns = [
    path('get_chat_list', ChatAPIView.as_view()),
    # path('test/', test)
]
