from django.db import models
from django.conf import settings


class Chat(models.Model):
    """Чат, в котором общаются пользователи"""
    name = models.CharField("Название чата", max_length=30)

    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              verbose_name="Создатель чата",
                              related_name="owned_chats",
                              on_delete=models.DO_NOTHING)

    users = models.ManyToManyField(to=settings.AUTH_USER_MODEL,
                                   verbose_name="Пользователи в чате",
                                   related_name="chats")

    class Meta:
        db_table = "chat"

    def __str__(self) -> str:
        return f"Chat_{self.id}, Owner: {self.owner}"


class Message(models.Model):
    """Сообщение, отправляемое пользователем"""

    chat = models.ForeignKey('Chat', on_delete=models.CASCADE,
                             verbose_name="чат с сообщением",
                             related_name="messages")

    text = models.TextField("текст сообщения", blank=False, max_length=1024)
    sent_at = models.DateTimeField("дата отсылки сообщения", auto_now_add=True)
    last_updated_at = models.DateTimeField("дата изменения сообщения",
                                           auto_now=True)
    sender = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name="отправитель")

    class Meta:
        db_table = "message"
        ordering = ('sent_at',)


class Attachment(models.Model):
    """Вложенный файл к сообщению"""

    def get_chat_directory_path(instance: Chat, filename) -> str:
        """Возвращает путь загрузки файлов в формате chats/chat_id/message_id/filename"""
        return 'chats/chat_{0}/message_{1}/{2}'.format(instance.message.chat.id,
                                                       instance.message.id,
                                                       filename)

    file_owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   verbose_name='владелец файла')

    message = models.ForeignKey(to='Message', on_delete=models.CASCADE,
                                related_name="attachments")

    # TODO: Ограничение нa количество файлов в сообщении
    file = models.FileField(verbose_name="файл, прикреплённый к сообщению",
                            upload_to=get_chat_directory_path)
    upload_date = models.DateTimeField(verbose_name="дата загрузки файла",
                                       auto_now_add=True)

    class Meta:
        db_table = "attachment"
