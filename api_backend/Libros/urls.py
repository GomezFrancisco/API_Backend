from django.urls import path
from Libros import views

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('libros/', views.libros_rest, name='libros-rest'),
    path('nuevo_libro/', views.NuevoLibro.as_view(), name='nuevo_libro'),
    path('autores/', views.autores_rest, name='autores-rest'),
    path('nuevo_autor/', views.NuevoAutor.as_view(), name='nuevo_autor'),
    path('editoriales/', views.editoriales_rest, name='editoriales-rest'),
    path('nueva_editorial/', views.NuevaEditorial.as_view(), name='nueva_editorial'),
]