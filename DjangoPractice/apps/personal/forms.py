from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from apps.personal.models import User


"""
Список полей в форме регистрации.
ВАЖНО!!!: не переставлять местами и не удалять поля username, password1, password2, password
Они используются в .admin.py в классе CustomUserAdmin
Добавлять дополнительные поля можно, но только в конец
Это сделано для того, чтобы список полей держался в одном месте
"""
user_creation_fields = ('username', 'password1',
                        'password2', 'birth_date', 'photo')

user_list_fields = ('username', 'password', 'birth_date', 'photo')


class CustomUserCreationForm(UserCreationForm):
    photo = forms.ImageField(required=False,
                             widget=forms.FileInput(attrs={"id": "image_field",  # you can access your image field with this id for css styling .
                                                    'style': "height: 100px ; width : 100px ; "}))

    class Meta:
        model = User
        fields = user_creation_fields


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = user_list_fields
