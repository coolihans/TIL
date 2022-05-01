from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Artist, Music
from .serializers import ArtistListSerializer, ArtistSerializer, MusicListSerializer, MusicSerializer
from music import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def artist_list(request):
    # 전체 가수 리스트 조회
    if request.method == 'GET':
        artists = Artist.objects.all()  
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    # 가수의 정보 생성
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)

@api_view(['POST'])
def music_create(request, artist_pk):
    # 특정 가수의 음악 정보 생성 => artist_pk 필요
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET'])
def music_all_list(request):
    music_all = Music.objects.all()
    serializer = MusicListSerializer(music_all, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def music_detail_update_delete(request, music_pk):

    music = get_object_or_404(Music, music_pk)
    
    def music_detail():
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    def music_update():
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):   # 400 출력
            serializer.save()
            return Response(serializer.data)

    def music_delete():         # 삭제 후 삭제한 음악의 id 출력???
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return music_detail()
    elif request.method == 'PUT':
        return music_update()
    elif request.method == 'DELETE':
        return music_delete()