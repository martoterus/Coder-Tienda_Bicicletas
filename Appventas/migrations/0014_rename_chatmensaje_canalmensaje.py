# Generated by Django 4.1 on 2022-08-29 20:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Appventas', '0013_canal_chatmensaje_canalusuario_canal_usuarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatMensaje',
            new_name='CanalMensaje',
        ),
    ]
