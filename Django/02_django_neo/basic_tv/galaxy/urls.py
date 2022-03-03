from django.urls import path
from . import views

app_name = 'galaxy'

urlpatterns = [
    # '/ping/'
    path('ping/', views.ping, name='ping'),
    path('pong/', views.pong, name='pong'),
    path('pingpong/', views.pingpong, name='pingpong'),
]
