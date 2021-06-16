from django.db import models
from django.urls import reverse



class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Название жанра", max_length=100)
    number_of_genres = models.PositiveSmallIntegerField("Количество книг в жанре", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Author(models.Model):
    """Авторы"""
    name = models.CharField("Имя", max_length=100)
    number_of_book = models.PositiveSmallIntegerField("Количество книг автора", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Book(models.Model):
    title = models.CharField("Название книги", max_length=100)
    published_year = models.PositiveSmallIntegerField("Дата издания", default=2019)
    rating = models.PositiveSmallIntegerField("Рейтинг", default=1)
    genre = models.ManyToManyField(Genre, verbose_name="жанры", related_name="genre_book")
    author_name = models.ManyToManyField(Author, verbose_name="Автор", related_name="book_author")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


