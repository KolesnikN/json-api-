from rest_framework import serializers, viewsets
from books.models import Book, Author, Genre


class AuthorListSerializer(serializers.ModelSerializer):
    """Вывод списка авторов"""
    class Meta:
        model = Author
        fields = ("name",)

class GenreListSerializer(serializers.ModelSerializer):
    """Вывод списка жанров"""
    class Meta:
        model = Genre
        fields = ("name", "number_of_genres",)

class BookDetailSerializer(serializers.ModelSerializer):
    """Список книг"""

    class Meta:
        model = Book
        fields = ("title",)

# class BookViewSet(viewsets.ReadOnlyModelViewSet):
#     """Список книг"""
#     author = AuthorListSerializer(read_only=True, many=True)
#     book = BookDetailSerializer(read_only=True, many=True)
#
#     genre = GenreListSerializer(read_only=True, many=True)







class CreateBookSerializer(serializers.ModelSerializer):
    """Добавление книги"""

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    class Meta:
        model = Book
        fields = "__all__"
