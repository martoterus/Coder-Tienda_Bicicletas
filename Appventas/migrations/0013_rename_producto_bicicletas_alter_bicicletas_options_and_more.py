# Generated by Django 4.0.6 on 2022-08-29 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appventas', '0012_alter_producto_imagen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='producto',
            new_name='bicicletas',
        ),
        migrations.AlterModelOptions(
            name='bicicletas',
            options={'verbose_name': 'bicicleta', 'verbose_name_plural': 'bicicletas'},
        ),
        migrations.CreateModel(
            name='repuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(null=True, upload_to='img')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appventas.categorias')),
            ],
            options={
                'verbose_name': 'repuesto',
                'verbose_name_plural': 'repuestos',
            },
        ),
        migrations.CreateModel(
            name='indumentarias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('color', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=30)),
                ('talle', models.CharField(max_length=30)),
                ('imagen', models.ImageField(null=True, upload_to='img')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appventas.categorias')),
            ],
            options={
                'verbose_name': 'indumentaria',
                'verbose_name_plural': 'indumentarias',
            },
        ),
        migrations.CreateModel(
            name='accesorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('tipo', models.CharField(max_length=30)),
                ('imagen', models.ImageField(null=True, upload_to='img')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appventas.categorias')),
            ],
            options={
                'verbose_name': 'accesorio',
                'verbose_name_plural': 'accesorios',
            },
        ),
    ]
