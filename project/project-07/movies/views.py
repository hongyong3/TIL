from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Genre, Movie, Score 
# Create your views here.

def index(request):
    # movies = Movie.objects.order_by('pk')
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)
    
def detail(request, movie_pk):
    movie = Movie.objects.annotate(score_avg=Avg('score__score')).get(pk=movie_pk)
    # movie = Movie.objects.get(pk=movie_pk)
    genre = Genre.objects.get(pk=movie.genre_id)
    scores = movie.score_set.all()
    context = {
        'movie' : movie,
        'genre' : genre,
        'scores' : scores,
    }
    return render(request, 'movies/detail.html', context)
    
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')
    
def new(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    score = request.POST.get('score')
    content = request.POST.get('content')
    scores = Score(movie=movie, content=content, score=score)
    scores.save()
    return redirect('movies:detail', movie.pk)
    
def scores_delete(request, movie_pk, score_pk):
    movie = Movie.objects.get(pk=movie_pk)
    score = Score.objects.get(pk=score_pk)
    score.delete()
    return redirect('movies:detail', movie.pk)