from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from books.models import Book, Author, Genre
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .service import YearFilter, NameFilter
from books.serializers import (
    BookDetailSerializer,
    TopBookDetailSerializer,
    TopAuthorDetailSerializer,
    AuthorListSerializer,
    GenreListSerializer,
)

class BookList(generics.ListAPIView):
    """Вывод книг"""
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = YearFilter

    def delete(self, request, pk):
        # Удаление книги по её ID
        book = get_object_or_404(Book.objects.all(), pk=id)
        book.delete()
        return Response({
            "message": "Book with id `{}` has been deleted.".format(pk)
        }, status=204)

class AuthorList(generics.ListAPIView):
    """Вывод авторов"""
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    filter_backends = (DjangoFilterBackend,)

    def delete(self, request, pk):
        # Удаление автора по его ID
        author = get_object_or_404(Author.objects.all(), pk=id)
        author.delete()
        return Response({
            "message": "Author with id `{}` has been deleted.".format(pk)
        }, status=204)

class AuthorSearch(generics.ListAPIView):
    """Вывод авторов"""
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = NameFilter

class GenresList(generics.ListAPIView):
    """Вывод жанров"""
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    filter_backends = (DjangoFilterBackend,)

class TopBooks(generics.ListAPIView):
    """Топ 10 книг с лучшим рейтингом по убыванию"""
    queryset = Book.objects.order_by('-rating')
    serializer_class = TopBookDetailSerializer
    filter_backends = (DjangoFilterBackend,)

class TopAuthors(generics.ListAPIView):
    """Топ 10 авторов с набиольшим кол-вом книг"""
    queryset = Author.objects.order_by('-number_of_book')
    serializer_class = TopAuthorDetailSerializer
    filter_backends = (DjangoFilterBackend,)



