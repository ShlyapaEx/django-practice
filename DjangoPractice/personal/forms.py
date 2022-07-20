from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

user_fields = ('username', 'password', 'birth_date', 'photo', 'friends')


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = user_fields


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = user_fields
