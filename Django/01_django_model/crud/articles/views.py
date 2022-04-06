from django.shortcuts import redirect, render
from .models import Article

# Create your views here.
"""
1. 글 작성 버튼을 누르면(/aritcles/new)
2. form 제공
3. form 제출시 (/articles/create)
4. 글 작성(db save)
5. detail 페이지로 이동 / list 이동
"""
# create 은 2개..
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return redirect('articles:detail', article.pk)

def list(request):
    articles = Article.objects.order_by('-updated_at')
    context = {'articles': articles,}
    return render(request, 'articles/list.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)

# update = 2개 필요
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return redirect('articles:detail', article.pk)

# delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:list')
    elif request.method == 'GET':
        return redirect('articles:detail', article.pk)