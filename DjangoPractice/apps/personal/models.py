from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
# TODO: Переместить get_user_directory_path в другой файл??


class User(AbstractUser):
    """Пользователь сайта"""

    def get_user_directory_path(instance, filename) -> str:
        """Возвращает путь загрузки файлов в формате MEDIA_ROOT/<user_username>/<filename>"""
        return 'users/user_{0}/{1}'.format(instance.username, filename)

    photo = models.ImageField("аватарка пользователя",
                              upload_to=get_user_directory_path,
                              null=True)
    birth_date = models.DateField("дата рождения пользователя", default=now,
                                  null=False, blank=False)
    friends = models.ManyToManyField("self")

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return self.username
