from django.urls import path
from main.views import index, about, contact, author

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('authors/', author, name='author'),
]
