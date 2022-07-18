from django.db import models


def user_directory_path(instance, filename) -> str:
    # file will be uploaded to MEDIA_ROOT/user_<login>/<filename>
    return 'user_{0}/{1}'.format(instance.login, filename)


class User(models.Model):
    """Пользователь сайта"""
    login = models.CharField("логин пользователя", max_length=15, unique=True)
    password = models.CharField("пароль пользователя", max_length=20)
    photo = models.ImageField("аватарка пользователя",
                              upload_to=user_directory_path)
    creation_date = models.DateTimeField(
        "дата создания пользователя", auto_now_add=True)
    friends = models.ManyToManyField("self")

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return self.login
