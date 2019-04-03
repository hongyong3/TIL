from django.shortcuts import render
from .models import Movie

# 여기에 코드를 작성하시오.

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/index.html', {'movies':movies})