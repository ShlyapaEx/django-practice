from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import IsChatOwnerOrReadOnly, IsInChat, IsMessageSender
from .serializers import (ChatSerializer, DetailChatSerializer,
                          MessageSerializer, MessageUpdateSerializer)
from .queries import (get_chats_for_user, read_chat_list,
                      read_messages_list)


class ChatAPIViewSet(viewsets.ModelViewSet):
    queryset = read_chat_list()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated, IsInChat, IsChatOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request) -> Response:
        current_user_chats = get_chats_for_user(request.user)
        serializer = self.get_serializer(current_user_chats, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, pk=None) -> Response:
        queryset = get_chats_for_user(request.user)
        chat_object = get_object_or_404(queryset, pk=pk)
        serializer = DetailChatSerializer(chat_object)
        return Response(data=serializer.data)


class MessageAPIViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = read_messages_list()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, IsMessageSender, IsInChat)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'update' or self.action == 'partial_update':
            serializer_class = MessageUpdateSerializer
        return serializer_class
