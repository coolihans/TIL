from django.shortcuts import get_object_or_404, render, redirect
from .forms import MovieForm
from .models import Movie
from django.views.decorators.http import require_http_methods, require_POST, require_safe


@require_safe
def index(request):
    movies = Movie.objects.all().order_by('-pk')
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)


@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        #유효성 검사
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)


@require_http_methods(["GET", "POST"])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        #유효성 검사
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    
    context = {
        'form': form,
        'movie' : movie,
    }
    return render(request, 'movies/update.html', context)


@require_POST
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movies:index')