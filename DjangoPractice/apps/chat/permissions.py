from rest_framework import permissions

from .queries import user_is_in_chat_with_message, user_is_in_chat_by_chat_id

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
    The has_permission function checks if the user is in the chat.
    If so, it returns True and allows them to send a message.
    Otherwise, it returns False and does not allow them to send a message.
    """

    def has_permission(self, request, view):
        return user_is_in_chat_by_chat_id(user=request.user,
                                          chat_id=request.data.get('chat'))


class IsMessageSenderOrInChat(permissions.BasePermission):
    """
    Разрешение на уровне объекта Message, позволяющее читать его 
    только пользователям, находящимся в одном чате с отправителем
    и позволяющее редактировать сообщение только его отправителю.
    """

    def has_object_permission(self, request, view, message: Message):
        current_user = request.user
        if (request.method in permissions.SAFE_METHODS
                and user_is_in_chat_with_message(user=current_user, message=message)):
            return True
        return message.sender == current_user
