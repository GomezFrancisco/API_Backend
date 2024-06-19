from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=128)
    nacionalidad = models.CharField(max_length=128)
    anio_nacimiento = models.IntegerField()

    def _str_(self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=128)
    direccion = models.CharField(max_length=256)

    def _str_(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=128)
    genero = models.CharField(max_length=128)
    anio_publicacion = models.IntegerField()
    autores = models.ManyToManyField(Autor)
    editoriales = models.ManyToManyField(Editorial)

    def _str_(self):
        return self.titulo