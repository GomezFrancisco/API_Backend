from django.contrib import admin
from Libros.models import Libro, Autor, Editorial
# Register your models here.

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Editorial)