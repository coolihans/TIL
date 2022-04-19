from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Article, Comment
from .forms import ArticleForm, CommentForm

'''commit 여부에 따른 코드 차이
article = form.save()
article = Article(title=request.POST.get('title'), content=request.POST.get('content')).save()

article = form.save(commit=False)
article.user = user
article.save()

article = Article(title=request.POST.get('title'), content=request.POST.get('content'))
article.user = user
article.save()
'''


@login_required
@require_http_methods(['GET', 'POST'])
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():  # article.user 는 validation check하지 않음!
            article = form.save(commit=False)  # 저장 직전에 멈추고, article 객체만 리턴해라
            article.user = request.user
            article.save()
            return redirect('articles:article_detail', article.pk)
    else:
        form = ArticleForm()
    context = { 'form': form, }
    return render(request, 'articles/article_form.html', context)


@require_safe
def article_index(request):
    articles = Article.objects.order_by('-pk')
    context = { 'articles': articles, }
    return render(request, 'articles/article_index.html', context)


@login_required
@require_safe
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    is_like = request.user.like_articles.filter(pk=article.pk).exists()
    form = CommentForm()
    context = { 
        'article': article,
        'form': form,
        'is_like': is_like,
    }
    return render(request, 'articles/article_detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 요청보낸 사용자 == 글 작성자 일 경우에만
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():  # article.user 는 validation check하지 않음!
                article = form.save(commit=False)  # 저장 직전에 멈추고, article 객체만 리턴해라
                article.save()
                return redirect('articles:article_detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = { 'form': form, }
        return render(request, 'articles/article_form.html', context)
    else:
        return redirect('articles:article_detail', article.pk)


@login_required
@require_POST
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:article_index')


@login_required 
@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()
    return redirect('articles:article_detail', article.pk)


@login_required
@require_POST
def comment_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)  # pk=article_pk
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:article_detail', article.pk)


@login_required
@require_POST
def article_like(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    user = request.user
    # 현재 사용자가 article에 좋아요를 기존에 했는지에 따라 다름.
    if user.like_articles.filter(pk=article.pk).exists():
        # 좋아요 취소 user.like_articles.filter(pk=article_pk)
        article.like_users.remove(user)
    else:
        # 좋아요 추가
        article.like_users.add(user)
    return redirect('articles:article_detail', article_pk)