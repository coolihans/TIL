from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dinner/', views.dinner),
    path('lotto/', views.lotto),
    path('greeting/<str:name>/', views.greeting),
]
