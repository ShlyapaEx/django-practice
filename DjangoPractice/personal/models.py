from django.db import models


class User(models.Model):
    """Пользователь сайта"""
    login = models.CharField("логин пользователя", max_length=15)
    password = models.CharField("пароль пользователя", max_length=20)
    photo = models.ImageField("аватарка пользователя",
                              upload_to="user_images/%Y/%m/%d/")
    creation_date = models.DateTimeField("дата создания пользователя", )

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return self.login
