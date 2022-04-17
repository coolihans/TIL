from django.shortcuts import render
import requests
import random

# Create your views here.
BASE_URL = 'https://api.themoviedb.org/3/'

def index(request):
    return render(request, 'index.html')

def recommendations(request, movie_id):
    url = f'{BASE_URL}movie/{movie_id}/similar?api_key=04c08caa3c3ade3d88e6c71bcfb450cb&language=en-US&page=1'
    response = requests.get(url)
    context = {
        'recommendations':response.json(),
        }
    return render(request, 'recommendations.html', context)



# https://api.themoviedb.org/3/movie/{movie_id}/similar?api_key=04c08caa3c3ade3d88e6c71bcfb450cb&language=en-US&page=1