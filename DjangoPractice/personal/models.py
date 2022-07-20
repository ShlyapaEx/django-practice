from django.db import models
from django.contrib.auth.models import AbstractUser
# TODO: Переместить get_user_directory_path в другой файл


class User(AbstractUser):
    """Пользователь сайта"""

    def get_user_directory_path(instance, filename) -> str:
        """Возвращает путь загрузки файлов в формате MEDIA_ROOT/<user_username>/<filename>"""
        return 'user_{0}/{1}'.format(instance.username, filename)

    # login = models.CharField("логин пользователя", max_length=15, unique=True)
    # password = models.CharField("пароль пользователя", max_length=20)
    photo = models.ImageField("аватарка пользователя",
                              upload_to=get_user_directory_path)
    birth_date = models.DateTimeField(
        "дата рождения пользователя", null=True, blank=True)
    friends = models.ManyToManyField("self")

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return self.username
