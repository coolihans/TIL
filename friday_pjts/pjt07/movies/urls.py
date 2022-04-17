from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_index, name='movie_index'),
    path('create/', views.movie_create, name='movie_create'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/delete/', views.movie_delete, name='movie_delete'),
    path('<int:movie_pk>/update/', views.movie_update, name='movie_update'),
    path('<int:movie_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
