from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^books/$', views.BookList.as_view()),
    url(r'^authors/$', views.AuthorList.as_view()),
    url(r'^genres/$', views.GenresList.as_view()),
    # url(r'^books/top/$', views.Top.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

