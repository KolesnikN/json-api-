from django_filters import rest_framework as filters
from .models import Book

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class YearFilter(filters.FilterSet):
    """Филтьтр по годам издания"""
    published_year = filters.RangeFilter()

    class Meta:
        model = Book
        fields = ['published_year']

class NameFilter(filters.FilterSet):
    """Фильтр по id автора"""
    author_name = filters.CharFilter()

    class Meta:
        model = Book
        fields = ['author_name', 'title']
