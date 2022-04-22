from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie, Actor, Review
from . import serializers
from .serializers import (ActorlistSerializer, ActorSerializer,
                          MovielistSerializer, MovieSerializer,
                          ReviewlistSerializer, ReviewSerializer)


# Create your views here.
@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorlistSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovielistSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    review = get_list_or_404(Review)
    serializer = ReviewlistSerializer(review, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_update_delete(request, review_pk):
    
    review = get_object_or_404(Review, pk=review_pk)    
    
    def review_detail():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def review_update():
        serializer = ReviewSerializer(review, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def review_delete():
        review.delete()
        data = {
            'delete': f'데이터 {review_pk}번이 삭제되었습니다.',
        }
        return Response(data, status.HTTP_204_NO_CONTENT)       

    if request.method == 'GET':
        return review_detail()
    elif request.method == 'PUT':
        return review_update()
    elif request.method == 'DELETE':
        return review_delete()


@api_view(['POST'])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
