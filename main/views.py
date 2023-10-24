from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    lastMatch = Match.objects.get(title="المباراة الماضية")
    nextMatch = Match.objects.get(title="المباراة القادمة")

    context = {'lastMatch': lastMatch, 'nextMatch': nextMatch}
    return render(request, 'home.html', context)


def news(request):

    context = {}
    return render(request, 'news.html', context)

def newsDetail(request):

    context = {}
    return render(request, 'newsDetail.html', context)


def media(request):
    
    context = {}
    return render(request, 'media.html', context)


def players(request):
    

    context = {}
    return render(request, 'players.html', context)


def matchDetail(request, pk):
    match = Match.objects.get(id=pk)

    context = {'match': match}
    return render(request, 'matchDetail.html', context)
