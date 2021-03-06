from http.client import BAD_REQUEST
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Article, Comment
from .forms import ArticleForm, CommentForm

@login_required
@require_http_methods(['GET','POST'])
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:article_detail', article.pk)
    else:
        form = ArticleForm()
    context = { 'form': form ,}
    return render(request, 'articles/article_form.html', context)


@require_safe
def article_index(request):
    articles = Article.objects.order_by('-pk')
    context = { 'articles' : articles, }

    return render(request, 'articles/article_index.html', context)


@login_required
@require_safe
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    context = { 
        'article': article,
        'form': form    
     }

    return render(request, 'articles/article_detail.html', context)


@login_required
@require_http_methods(['GET','POST'])
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect('articles:article_detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = { 'form': form ,}
        return render(request, 'articles/article_form.html', context)
    else:
        return redirect('articles:article_detail', article.pk)


@login_required
@require_POST
def article_delete(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:article_index')


@login_required
@require_POST
def comment_create(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:article_detail', article.pk)
    return redirect('accounts:login', article.pk)


@require_POST
def comment_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()

        return redirect('articles:article_detail', article.pk)