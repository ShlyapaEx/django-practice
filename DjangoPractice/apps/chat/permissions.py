from rest_framework import permissions

from .models import Chat


class IsChatOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта Chat,
    позволяющее редактировать его только владельцам объекта.
    """

    def has_object_permission(self, request, view, chat: Chat) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return chat.owner == request.user
