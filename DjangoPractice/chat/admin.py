from django.contrib import admin
from .models import Chat, Attachment, Message

models_list = (Chat, Attachment, Message)
admin.site.register(models_list)
