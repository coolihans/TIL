from django.shortcuts import render


def ping(request):
    return render(request, 'galaxy/ping.html')


def pong(request):

    return render(request, 'galaxy/pong.html')


def pingpong(request):

    return render(request, 'galaxy/pingpong.html')