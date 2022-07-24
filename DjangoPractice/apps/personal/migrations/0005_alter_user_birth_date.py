# Generated by Django 4.0.6 on 2022-07-20 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='дата рождения пользователя'),
        ),
    ]