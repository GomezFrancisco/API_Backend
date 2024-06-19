from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=128)
    nacionalidad = models.CharField(max_length=128)
    anio_nacimiento = models.IntegerField()

    def _str_(self):
        return f'{self.nombre}-{self.nacionalidad}-{self.anio_nacimiento}'

class Editorial(models.Model):
    nombre = models.CharField(max_length=128)
    direccion = models.CharField(max_length=256)

    def _str_(self):
        return f'{self.nombre}-{self.direccion}'

class Libro(models.Model):
    titulo = models.CharField(max_length=128)
    genero = models.CharField(max_length=128)
    anio_publicacion = models.IntegerField()
    autores = models.ManyToManyField(Autor, related_name="libros")
    editoriales = models.ManyToManyField(Editorial, related_name="libros")

    def _str_(self):
        return self.titulo