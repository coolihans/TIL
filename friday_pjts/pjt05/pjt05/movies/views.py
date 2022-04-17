from django.shortcuts import redirect, render
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)

def new(request):
    return render(request, 'movies/new.html')

# edit -> update
def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/edit.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.title = request.GET['title']
    movie.audience = request.GET['audience']
    movie.release_date = request.GET['release_date']
    movie.genre = request.GET['genre']
    movie.score = request.GET['score']
    movie.poster_url = request.GET['poster_url']
    movie.description = request.GET['description']
    movie.save()
    return redirect('movies:detail', movie.pk)

def create(request):
    movie = Movie()
    movie.title = request.GET['title']
    movie.audience = request.GET['audience']
    movie.release_date = request.GET['release_date']
    movie.genre = request.GET['genre']
    movie.score = request.GET['score']
    movie.poster_url = request.GET['poster_url']
    movie.description = request.GET['description']
    movie.save()
    return redirect('movies:detail', movie.pk)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')