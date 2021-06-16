from books.models import Book, Author, Genre
from rest_framework import permissions, viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsOwnerOrReadOnly
from .service import get_client_ip, YearFilter, PaginationBooks
from books.serializers import (
    BookDetailSerializer,
    CreateBookSerializer,
    AuthorListSerializer,
    GenreListSerializer,

)
class BookList(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AuthorList(generics.CreateAPIView):
    """Вывод авторов"""
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer

class GenresList(generics.CreateAPIView):
    """Вывод жанров"""
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer


# class BookList_top(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookDetailSerializer
#     filter_backends = (DjangoFilterBackend)
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)





# class BookViewSet(viewsets.ReadOnlyModelViewSet):
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = BookFilter
#     pagination_class = PaginationBooks
#
#     def get_queryset(self):
#         book = Book.objects.all()
#         return book
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return BookDetailSerializer
#
#
# class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вывод актеров или режиссеров"""
#     queryset = Author.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return AuthorListSerializer
#
# class GenreViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вывод количества книг жанров"""
#     queryset = Genre.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return GenreListSerializer
#
# class CreateBook(viewsets.ModelViewSet):
#     """Добавление книги"""
#     serializer_class = CreateBookSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(ip=get_client_ip(self.request))
