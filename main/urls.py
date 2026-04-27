from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Проверь вот эту строку: name должно быть 'movie_detail'
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]