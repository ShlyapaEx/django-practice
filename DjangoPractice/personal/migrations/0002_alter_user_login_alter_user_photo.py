# Generated by Django 4.0.6 on 2022-07-18 18:14

from django.db import migrations, models
import personal.models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=15, unique=True, verbose_name='логин пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to=personal.models.user_directory_path, verbose_name='аватарка пользователя'),
        ),
    ]