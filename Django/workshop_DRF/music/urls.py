from django.urls import path
from . import views

urlpatterns = [
    # GET & POST api/v1/artists/ # 모든 가수
    path('artists/', views.artist_list),
    # GET api/v1/artists/<artist_pk>/
    path('artists/<int:artist_pk>/', views.artist_detail),
    # POST api/v1/artists/<artist_pk>/music/   
    path('artists/<int:artist_pk>/music/', views.music_create),
    # GET api/v1/music/ # 모든 음악?
    path('music/', views.music_all_list),
    # GET & PUT & DELETE api/v1/music/<music_pk>/ # 특정음악의 응답 수정 삭제
    path('music/<int:music_pk>/', views.music_detail_update_delete),
]
