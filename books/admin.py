from django.contrib import admin
from .models import Book, Author, Genre

# Для добавления данных в БД использую админку
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
