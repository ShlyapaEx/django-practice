# Generated by Django 4.0.6 on 2022-07-19 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='login',
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата рождения пользователя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]