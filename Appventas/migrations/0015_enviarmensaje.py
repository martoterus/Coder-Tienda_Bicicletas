# Generated by Django 4.0.6 on 2022-09-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appventas', '0014_alter_bicicletas_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnviarMensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
    ]
