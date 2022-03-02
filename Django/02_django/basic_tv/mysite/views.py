from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
import random

# Create your views here.
def home(request):
  return render(request, 'home.html')

def dinner(request):
  menus = ['떡볶이', '햄버거', '초밥', '피자']
  pick = random.choice(menus)
  context = {
    'pick' : pick,
    'menus' : menus,
  }
  return render(request, 'dinner.html', context)

def lotto(request):
  lucky_numbers = random.sample(range(1,46), 6)
  context = {
    'lucky_numbers': lucky_numbers,
  }
  return render(request, 'lotto.html', context)


def greeting(request, name):
  context = {
    'name' : name,
  }
  return render(request, 'greeting.html', context)