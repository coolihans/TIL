from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        # print(form.errors)
    else:
        # new
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def index(request):
    pass

def detail(request, pk):
    pass

def edit(request, pk):
    pass

def update(request, pk):
    pass

def delete(request, pk):
    pass