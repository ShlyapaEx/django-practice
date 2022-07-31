from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from .services import read_chat_list, read_messages_from_chat_list
from .serializers import ChatSerializer, MessageSerializer


class ChatAPIViewSet(viewsets.ModelViewSet):
    queryset = read_chat_list()
    serializer_class = ChatSerializer


class MessageAPIViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = read_messages_from_chat_list()
    serializer_class = MessageSerializer
    # TODO: perm classes
    # permission_classes = ()

    # TODO: Сделать тоньше
    def create(self, request, *args, **kwargs):
        # main thing starts
        # list to be passed to the serializer
        attachments = list(request.FILES.keys())
        print(attachments, "****")
        serializer = self.get_serializer(
            data=request.data, attachments=attachments)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
