from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # /accounts/signup/
    path('signup/', views.signup, name='signup'),
    # /accounts/login/
    path('login/', views.login, name='login'),
    # /accounts/logout/
    path('logout/', views.logout, name='logout'),
    # /accounts/neo/
    path('<str:username>/', views.profile, name='profile'),
    # /accounts/hans/follow/
    path('<int:user_pk>/follow/', views.follow, name='follow'),

]
