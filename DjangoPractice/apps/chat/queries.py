from .models import Chat, Message
from django.db.models.query import QuerySet


def read_chat_list() -> QuerySet:
    """Возвращает список всех чатов из базы данных в формате QuerySet"""
    queryset = Chat.objects.all()
    return queryset


def read_messages_list() -> QuerySet:
    """
    Функция read_messages_list возвращает QuerySet всех сообщений из базы данных.
    """
    queryset = Message.objects.all()
    return queryset


def get_chats_for_user(user) -> QuerySet:
    """
    Функция get_chats_for_user возвращает QuerySet всех чатов,
    в которых находится пользователь.
    """
    queryset = Chat.objects.prefetch_related('users').filter(users=user).all()
    return queryset


def get_messages_for_chat(chat) -> QuerySet:
    queryset = Message.objects.select_related('chat').filter(chat=chat).all()
    return queryset


def user_is_in_chat_by_chat_id(user, chat_id) -> bool:
    chat_found = Chat.objects.prefetch_related('users') \
                             .filter(pk=chat_id, users=user).exists()
    return chat_found


def user_is_in_chat_with_message(user, message) -> bool:
    chat_found = Chat.objects.prefetch_related('users') \
                             .filter(messages=message, users=user).exists()
    return chat_found
