import os

from django.core.wsgi import get_wsgi_application
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('books.urls')),
]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

application = get_wsgi_application()
