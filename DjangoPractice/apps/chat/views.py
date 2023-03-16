from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly
from .serializers import (ChatSerializer, DetailChatSerializer,
                          MessageSerializer)
from .queries import (get_chats_for_user, read_chat_list,
                      read_messages_from_chat_list)


class ChatAPIViewSet(viewsets.ModelViewSet):
    queryset = read_chat_list()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request):
        current_user_chats = get_chats_for_user(request.user)
        serializer = self.get_serializer(current_user_chats, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, pk=None):
        queryset = get_chats_for_user(request.user)
        chat_object = get_object_or_404(queryset, pk=pk)
        serializer = DetailChatSerializer(chat_object)
        return Response(data=serializer.data)


class MessageAPIViewSet(viewsets.ModelViewSet):
    queryset = read_messages_from_chat_list()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(sender=current_user)
