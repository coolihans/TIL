from rest_framework import serializers
from .models import Movie, Actor, Review


class ActorlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name',)


class ActorSerializer(serializers.ModelSerializer):
    class MovielistSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Movie
            fields = ('title',)
    
    movies = MovielistSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'movies', 'name',)


class MovielistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class MovieSerializer(serializers.ModelSerializer):
    
    class ActorlistSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    class ReviewlistSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content',)

    actors = ActorlistSerializer(many=True, read_only=True)
    review_set = ReviewlistSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date' , 'poster_path',)


class ReviewlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)


class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content',)