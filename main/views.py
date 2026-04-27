from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import Q # Импортируем Q для сложного поиска

def index(request):
    # Получаем запрос из строки поиска (input name="q")
    query = request.GET.get('q')
    # Получаем категорию из фильтра (cat)
    category_filter = request.GET.get('cat')

    movies = Movie.objects.all().order_by('-created_at')

    # Если есть поисковый запрос
    if query:
        movies = movies.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    # Если выбран фильтр по категории
    if category_filter:
        movies = movies.filter(category=category_filter)

    return render(request, 'main/index.html', {'movies': movies, 'query': query})
def movie_detail(request, movie_id): # Аргумент должен совпадать с тем, что в urls.py
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'main/detail.html', {'movie': movie})