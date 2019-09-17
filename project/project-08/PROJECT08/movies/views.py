from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from .models import Genre, Movie, Score
from .forms import MovieForm, ScoreForm

# Create your views here.
def index(request):
    # movies = Movie.objects.order_by('pk')
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()
    context = {
        'movies': movies,
        }
    return render(request, 'movies/index.html', context)
    
def detail(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    movie = Movie.objects.annotate(score_avg=Avg('score__score')).get(pk=movie_pk)
    genre = Genre.objects.get(pk=movie.genre_id)
    scores = movie.score_set.all()
    form = ScoreForm()
    context = {
        'form' : form,
        'movie' : movie,
        'genre' : genre,
        'scores' : scores,
    }
    return render(request, 'movies/detail.html', context)
    
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # if request.method == 'POST':
    movie.delete()
    return redirect('movies:index')
    # else:
    #     return redirect('movies:detail', movie.pk)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
            
    else:
        form = MovieForm()
    context = {
        'form':form, 
    }
    return render(request, 'movies/form.html', context)
    
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/form.html', context)
    
def scores_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        score = Score(movie=movie)
        form = ScoreForm(request.POST, instance=score)
        if form.is_valid():
            score = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        return redirect('movies:detail', movie.pk)
    
def scores_delete(request, movie_pk, score_pk):
    movie = Movie.objects.get(pk=movie_pk)
    score = Score.objects.get(pk=score_pk)
    score.delete()
    return redirect('movies:detail', movie.pk)