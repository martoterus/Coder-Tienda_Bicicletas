# Generated by Django 4.0.6 on 2022-08-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appventas', '0011_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
