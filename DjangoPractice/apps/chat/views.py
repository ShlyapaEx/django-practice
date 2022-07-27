from django.shortcuts import render
from rest_framework import generics

from .services import read_chat_list
from .serializers import ChatSerializer


class ChatAPIView(generics.ListAPIView):
    queryset = read_chat_list()
    serializer_class = ChatSerializer
