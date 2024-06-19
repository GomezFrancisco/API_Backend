from rest_framework import serializers

from Libros.models import Libro, Autor, Editorial


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    autores = AutorSerializer(many=True, read_only=True)
    editoriales = EditorialSerializer(many=True, read_only=True)

    class Meta:
        model = Libro
        fields = '__all__'