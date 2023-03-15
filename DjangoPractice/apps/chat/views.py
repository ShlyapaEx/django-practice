from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .services import read_chat_list, read_messages_from_chat_list
from .serializers import ChatSerializer, MessageSerializer


class ChatAPIViewSet(viewsets.ModelViewSet):
    queryset = read_chat_list()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)


class MessageAPIViewSet(viewsets.ModelViewSet):
    queryset = read_messages_from_chat_list()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
