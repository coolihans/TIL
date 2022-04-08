from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from .models import Article
from .forms import ArticleForm


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():  # <= 실패시 form에 에러메시지가 담김
            article = form.save()
            return redirect('articles:detail', article.pk)
    elif request.method == 'GET':
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/form.html', context)


@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():  # <= 실패시 form에 에러메시지가 담김
            article = form.save()
            return redirect('articles:detail', article.pk)
    elif request.method == 'GET':
        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }

    return render(request, 'articles/form.html', context)


# 아래 함수는 POST 요청만 받음
# @require_http_methods(['POST'])
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')
