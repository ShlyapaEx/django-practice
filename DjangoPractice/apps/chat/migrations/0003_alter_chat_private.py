# Generated by Django 4.0.6 on 2022-07-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat_private_alter_attachment_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='private',
            field=models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], editable=False, verbose_name='Является ли чат приватным?'),
        ),
    ]
