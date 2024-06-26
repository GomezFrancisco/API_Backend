# Generated by Django 4.1 on 2024-06-18 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('nacionalidad', models.CharField(max_length=128)),
                ('anio_nacimiento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('direccion', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128)),
                ('genero', models.CharField(max_length=128)),
                ('anio_publicacion', models.IntegerField()),
                ('autores', models.ManyToManyField(to='Libros.autor')),
                ('editoriales', models.ManyToManyField(to='Libros.editorial')),
            ],
        ),
    ]
