from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

from .forms import user_creation_fields, user_list_fields


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    fieldsets = (
        (
            None,
            {
                'fields': user_list_fields
            }
        ),
    )

    # add_fieldsets = (
    #     *UserAdmin.add_fieldsets,
    #     (
    #         'Custom add fields',
    #         {
    #             "fields": ('birth_date', 'photo'),
    #         },
    #     ),
    # )
    print(CustomUserCreationForm.Meta.fields)
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            None, {"fields": user_creation_fields[3:]}
        ),
    )


admin.site.register(User, CustomUserAdmin)
