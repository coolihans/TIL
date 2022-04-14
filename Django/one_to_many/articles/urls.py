from django.urls import path
from . import views

app_name = 'articles'


urlpatterns = [
    # /articles/create/
    path('create/', views.article_create, name='article_create'),
    # /articles/
    path('', views.article_index, name='article_index'),
    # /articles/1/
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    # /articles/1/update/
    path('<int:article_pk>/update/', views.article_update, name='article_update'),
    # /articles/1/delete/
    path('<int:article_pk>/delete/', views.article_delete, name='article_delete'),
    path('<int:article_pk>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),

]



# 댓글 생성
"""
1. detail 페이지를 요청함.
2. detail > form 태그에 내용입력 + submit
3. form.action 해당하는 URL로 요청 발생 
4. view 함수 실행
5. view 함수 내부에서 validation check & save / error
6. response
"""