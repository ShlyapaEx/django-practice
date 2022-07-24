from django.contrib import admin
from .models import Chat, Attachment, Message


class MessageInline(admin.TabularInline):
    """ Inline сообщений(Message) в Chat """
    model = Message
    extra = 0
    ordering = ('sent_at',)


class ChatAdmin(admin.ModelAdmin):
    """ Админка для Chat с Inline """
    inlines = (MessageInline, )


class AttachmentInline(admin.TabularInline):
    """ Inline прикреплённых файлов(Attachment) в Message """
    model = Attachment
    fk_name = 'message'
    extra = 0


class MessageAdmin(admin.ModelAdmin):
    """ Админка для Message c Inline """
    model = Message
    readonly_fields = ('sent_at',)
    inlines = (AttachmentInline, )


admin.site.register(Attachment)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
