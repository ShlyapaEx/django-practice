from django.db import models
from django.conf import settings


class Chat(models.Model):
    """Чат, в котором общаются пользователи"""
    first_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="first_user")
    second_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="second_user")

    class Meta:
        db_table = "chat"


class Message(models.Model):
    """Сообщение, отправляемое от одного пользователя к другому"""

    chat = models.ForeignKey('Chat',
                             on_delete=models.CASCADE,
                             verbose_name="чат, в котором будет осуществляться переписка"
                             )
    text = models.TextField("текст сообщения", blank=False, max_length=1024)
    sent_at = models.DateTimeField("дата отсылки сообщения", auto_now_add=True)
    last_updated_at = models.DateTimeField(
        "дата изменения сообщения", auto_now=True)

    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="from_user", verbose_name="отправитель", null=True)
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="to_user", verbose_name="получатель", null=True)

    class Meta:
        db_table = "message"


class Attachment(models.Model):
    """Вложенные файлы к сообщению"""

    def get_chat_directory_path(instance: Chat, filename) -> str:
        """Возвращает путь загрузки файлов в формате TODO"""
        return 'chat_{0}/message_{1}/{2}'.format(
            instance.message.chat.id,
            instance.message.id,
            filename
        )

    file_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)

    # TODO: Ограничение не количество файлов в сообщении
    file = models.FileField(
        "файл, прикреплённый к сообщению", upload_to=get_chat_directory_path)
    upload_date = models.DateTimeField(
        "дата загрузки файла", auto_now_add=True, )

    class Meta:
        db_table = "attachment"
