from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.chat.models import Chat
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

from .forms import user_creation_fields, user_list_fields


class ChatInline(admin.TabularInline):
    model = User.chats.through
    extra = 0


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    inlines = [ChatInline]
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Дополнительная информация", {'fields': user_list_fields[2:]}
        ),
    )

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            "Дополнительная информация", {"fields": user_creation_fields[3:]}
        ),
    )


admin.site.register(User, CustomUserAdmin)
