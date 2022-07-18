from django.db import models


class Chat(models.Model):
    """Чат, в котором общаются пользователи"""
    first_user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    second_user = models.ForeignKey('User', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "chat"


def chat_directory_path(instance: Chat, filename) -> str:
    # file will be uploaded to MEDIA_ROOT/chat_<first_user>_<second_user>/<filename>
    return 'chat_{0}_{1}/{2}'.format(
        instance.first_user,
        instance.second_user,
        filename
    )


class Message(models.Model):
    """Сообщение, отправляемое от одного пользователя к другому"""
    chat = models.ForeignKey('Chat',
                             on_delete=models.CASCADE,
                             verbose_name="Чат, в котором будем осуществляться переписка"
                             )
    text = models.TextField("текст сообщения", blank=False, max_length=1024)
    sent_at = models.DateTimeField("дата отсылки сообщения", auto_now_add=True)
    last_updated_at = models.DateTimeField(
        "дата изменения сообщения", auto_now=True)

    from_user = models.ForeignKey('User', on_delete=models.SET_NULL)
    to_user = models.ForeignKey('User', on_delete=models.SET_NULL)

    class Meta:
        db_table = "message"


class Attachment(models.Model):
    """Вложенные файлы к сообщению"""
    file_owner = models.ForeignKey('User', on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)

    file = models.FileField(
        "Файл, прикреплённый к сообщению", upload_to=chat_directory_path)
    upload_date = models.DateTimeField(
        "Дата загрузки файла", auto_now_add=True)

    class Meta:
        db_table = "attachment"
