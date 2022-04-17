from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # accounts/signup/
    path('signup/', views.signup, name='signup'),
    # accounts/login/
    path('login/', views.login, name='login'),
    # accounts/logout/
    path('logout/', views.logout, name='logout'),
    # accounts/update/
    path('update/', views.update, name='update'),
    # accounts/delete/ -> 회원 정보 삭제 
    path('delete/', views.delete, name='delete'),
    # accounts/password/ -> 비밀번호 변경
    path('password/', views.change_password, name='change_password'),

]
