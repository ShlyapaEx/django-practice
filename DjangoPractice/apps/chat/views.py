from rest_framework import viewsets

from .services import read_chat_list
from .serializers import ChatSerializer


class ChatAPIViewSet(viewsets.ModelViewSet):
    queryset = read_chat_list()
    serializer_class = ChatSerializer
