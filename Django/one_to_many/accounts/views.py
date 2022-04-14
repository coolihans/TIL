from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('articles:article_index')
        else:
            form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('articles:article_index')


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                return redirect(request.GET.get('next') or 'articles:article_index')
        else:
            form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('articles:article_index')
        

def logout(request):
    auth_logout(request)
    return redirect('articles:article_index')    


def profile(request, username):
    pass
