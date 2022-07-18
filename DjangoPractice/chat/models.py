from django.db import models


class Message(models.Model):
    """Сообщение, отправляемое от одного пользователя к другому"""
    text = models.TextField("текст сообщения", blank=False, max_length=1024)
    sent_at = models.DateTimeField("дата отсылки сообщения", auto_now_add=True)

    class Meta:
        db_table = "message"
