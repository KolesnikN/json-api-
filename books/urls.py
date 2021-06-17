from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/top/', views.TopBooks.as_view()),
    path('authors/', views.AuthorSearch.as_view()),
    path('authors/top', views.TopAuthors.as_view()),
    path('genres/', views.GenresList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

