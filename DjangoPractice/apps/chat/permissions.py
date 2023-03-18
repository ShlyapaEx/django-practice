from rest_framework import permissions

from .queries import user_is_in_chat_by_chat_id

from .models import Chat, Message


class IsChatOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта Chat,
    позволяющее редактировать его только владельцам объекта.
    """

    def has_object_permission(self, request, view, chat: Chat) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return chat.owner == request.user


class IsInChat(permissions.BasePermission):
    """
    Разрешение позволяющее читать сообщения только пользователям,
    находящимся в чате
    """

    def has_permission(self, request, view):
        return user_is_in_chat_by_chat_id(user=request.user,
                                          chat_id=request.data.get('chat'))


class IsMessageSender(permissions.BasePermission):
    """
    Разрешение на уровне объекта Message,
    позволяющее редактировать сообщение только его отправителю.
    """

    def has_object_permission(self, request, view, message: Message):
        if request.method in permissions.SAFE_METHODS:
            return True
        return message.sender == request.user
