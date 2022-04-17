from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import (require_http_methods, require_POST,
                                          require_safe)
from .forms import MovieForm, CommentForm
from .models import Comment, Movie

# Create your views here.

@require_safe
def movie_index(request):
    movies = Movie.objects.all()
    context ={
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:movie_detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)


@require_safe
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = CommentForm()

    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/detail.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def movie_update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                movie = form.save()
                return redirect('movies:movie_detail', movie.pk)
        else:
            form = MovieForm(instance=movie)     
    else:
        return redirect('movies:movie_detail', movie.pk)
    context={
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)

@require_POST
def movie_delete(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if request.user == movie.user:
            movie.delete()
        return redirect('movies:movie_index')
    return redirect('accounts:login')


@require_POST
def comment_create(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.movie = movie
            comment.save()
        return redirect('movies:movie_detail', movie.pk)
    return redirect('accounts:login')



@require_POST
def comment_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        return redirect('movies:movie_detail', movie.pk)
    return redirect('accounts:login')    