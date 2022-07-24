# Generated by Django 4.0.6 on 2022-07-22 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_remove_chat_first_user_remove_chat_private_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='is_private',
        ),
        migrations.RemoveField(
            model_name='message',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='to_user',
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='отправитель'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='users',
            field=models.ManyToManyField(related_name='chats', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи в чате'),
        ),
    ]
