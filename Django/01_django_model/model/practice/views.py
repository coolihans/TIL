from multiprocessing import context
from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    context={
        'articles': articles,
    }
    return render(request, 'practice/article_list.html', context)

    
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context={
        'article': article,
    }
    return render(request, 'practice/article_detail.html', context)