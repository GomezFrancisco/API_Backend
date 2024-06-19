from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Libro, Autor, Editorial
from .forms import LibroForm, AutorForm, EditorialForm
from .serializers import LibroSerializer, AutorSerializer, EditorialSerializer


def get_all_libros():
    libros = Libro.objects.all().order_by('titulo')
    serializer = LibroSerializer(libros, many=True)
    return serializer.data

def get_all_autores():
    autores = Autor.objects.all().order_by('nombre')
    serializer = AutorSerializer(autores, many=True)
    return serializer.data

def get_all_editoriales():
    editoriales = Editorial.objects.all().order_by('nombre')
    serializer = EditorialSerializer(editoriales, many=True)
    return serializer.data


def libros_rest(request):
    libros = get_all_libros()
    return JsonResponse(libros, safe=False)

def autores_rest(request):
    autores = get_all_autores()
    return JsonResponse(autores, safe=False)

def editoriales_rest(request):
    editoriales = get_all_editoriales()
    return JsonResponse(editoriales, safe=False)

def Home(request):
    libros = Libro.objects.all()
    autores = get_all_autores()
    editoriales = get_all_editoriales()
    return render(request, 'home.html', {
        'Libros': libros,
        'Autores': autores,
        'Editoriales': editoriales,
    })

class NuevoLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'form_libro.html'
    success_url = reverse_lazy('home')

class NuevoAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'form_autor.html'
    success_url = reverse_lazy('home')

class NuevaEditorial(CreateView):
    model = Editorial
    form_class = EditorialForm
    template_name = 'form_editorial.html'
    success_url = reverse_lazy('home')