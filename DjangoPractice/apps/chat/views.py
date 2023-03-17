from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import IsChatOwnerOrReadOnly, IsInChat, IsMessageSenderOrInChat
from .serializers import (ChatSerializer, DetailChatSerializer,
                          MessageSerializer)
from .queries import (get_chats_for_user, read_chat_list,
                      read_messages_list)


class ChatAPIViewSet(viewsets.ModelViewSet):
    queryset = read_chat_list()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated, IsChatOwnerOrReadOnly)

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
    permission_classes = (IsAuthenticated, IsMessageSenderOrInChat | IsInChat)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
