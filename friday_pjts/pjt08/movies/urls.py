from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # GET /articles/ => index
    # POST /articles/ => create
    # path('', views.article_index_create),
    
    # GET /articles/1/ => detail
    # PUT /articles/1/ => update
    # DELETE /articles/1/ => delete
    # path('<int:article_pk>/', views.article_detail_update_delete),

    # POST /articles/1/comments/ => 1번 글에 댓글 달기
    # path('<int:article_pk>/comments/', views.comment_create),
    # PUT /articles/1/comments/1/ => 1번 글에 달린 1번 댓글 수정
    # DELETE /articles/1/comments/1/ => 1번 글에 달린 1번 댓글 삭제
    # path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_delete)


    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail_update_delete),
    path('movies/<int:movie_pk>/reviews', views.create_review),

]
