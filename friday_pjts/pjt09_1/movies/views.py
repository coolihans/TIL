import random

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_safe
from django.contrib.auth.decorators import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Movie
from django.core.paginator import Paginator
from movies.serializers import MovieSerializer


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('-popularity')
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movies': page_obj
    }
    return render(request, 'movies/index.html', context)


@api_view(['GET'])
def ajax(request):
    movies = Movie.objects.order_by('-popularity')
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    serializer = MovieSerializer(page_obj, many=True)

    return Response(serializer.data)  


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genre_queryset = movie.genres.filter(movie=movie.pk).values('name')

    context = {
        'movie': movie,
        'genres': genre_queryset,
    }

    return render(request, 'movies/detail.html', context)


@require_safe
@login_required
def recommended(request):
    movies = list(Movie.objects.filter(vote_count__gte=3000, popularity__gte=30))
    recommend = random.sample(movies, 10)

    context = {
        'movies': recommend,
    }

    return render(request, 'movies/recommended.html', context)
