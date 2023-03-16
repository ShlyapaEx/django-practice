from .models import Chat, Message
from django.db.models.query import QuerySet


def read_chat_list() -> QuerySet:
    """Возвращает список всех чатов из базы данных в формате QuerySet"""
    queryset = Chat.objects.all()
    return queryset


# def read_messages_from_chat_list(chat_id: int | str) -> QuerySet:
#     queryset = Message.objects.filter(chat=chat_id).all()
#     return queryset

def read_messages_from_chat_list() -> QuerySet:
    queryset = Message.objects.all()
    return queryset


def get_chats_for_user(user) -> QuerySet:
    """
    Функция get_chats_for_user возвращает QuerySet всех чатов,
    в которых находится пользователь.
    """
    queryset = Chat.objects.prefetch_related('users').filter(users=user).all()
    return queryset
