# Generated by Django 4.0.6 on 2022-07-30 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0010_alter_message_options_alter_attachment_file_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.CharField(default='default', max_length=30, verbose_name='Название чата'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='owner',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owned_chats', to=settings.AUTH_USER_MODEL, verbose_name='Создатель чата'),
            preserve_default=False,
        ),
    ]
