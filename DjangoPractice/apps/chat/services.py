from .models import Chat, Message, Attachment
from django.db.models.query import QuerySet


def read_chat_list() -> QuerySet:
    """Возвращает список всех чатов из базы данных"""
    queryset = Chat.objects.all()
    return queryset
