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
        fields = ("author_name", "title")

class TopBookDetailSerializer(serializers.ModelSerializer):
    """Вывод топ 10 книг по рейтингу"""
    class Meta:
        model = Book
        fields = ('title', 'rating',)

class TopAuthorDetailSerializer(serializers.ModelSerializer):
    """Вывод топ 10 книг по рейтингу"""
    class Meta:
        model = Author
        fields = ('name', 'number_of_book',)







class CreateBookSerializer(serializers.ModelSerializer):
    """Добавление книги"""

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    class Meta:
        model = Book
        fields = "__all__"
