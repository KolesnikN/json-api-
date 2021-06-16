from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from rest_framework.reverse import reverse

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Author(models.Model):
    """Автор"""
    name = models.CharField("Имя автора", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Book(models.Model):
    title = models.CharField("Название книги", max_length=100)
    published_year = models.PositiveSmallIntegerField("Дата издания", default=2019)
    author = models.ManyToManyField(Author, related_name="book_director")
    genre = models.CharField("Жанр", max_length=100)
    rating = models.PositiveSmallIntegerField("Рейтинг", default=1)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


