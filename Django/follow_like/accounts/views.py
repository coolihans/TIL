from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_safe, require_POST
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


@require_safe
def profile(request, username):
    me = request.user
    User = get_user_model()
    profile_user = get_object_or_404(User, username=username)
    is_fan = me.stars.filter(pk=profile_user.pk).exists()
    context = {
        'profile_user': profile_user,
        'is_fan': is_fan,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
@require_POST
def follow(request, user_pk):
    you = get_object_or_404(get_user_model(),pk=user_pk)
    me = request.user
    if me != you:
        if you.fans.filter(pk=me.pk).exists():
            you.fans.remove(me)
        else:
            you.fans.add(me)
    return redirect('accounts:profile', you.username)