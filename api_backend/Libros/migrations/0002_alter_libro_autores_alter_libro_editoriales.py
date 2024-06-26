# Generated by Django 4.1 on 2024-06-19 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(related_name='libros', to='Libros.autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='editoriales',
            field=models.ManyToManyField(related_name='libros', to='Libros.editorial'),
        ),
    ]
