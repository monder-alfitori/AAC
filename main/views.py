from django.shortcuts import render
from .models import *



def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)



def home(request):
    lastMatch = Match.objects.get(title="المباراة الماضية")
    nextMatch = Match.objects.get(title="المباراة القادمة")
    news = News.objects.all().order_by('-created_at')
    players = Player.objects.all().order_by("?")
    media = Media.objects.all().order_by('-created_at')
    hero = News.objects.filter(is_hero=True).order_by('-created_at')

    context = {'lastMatch': lastMatch, 'nextMatch': nextMatch, 'news': news, 'players': players, 'media': media, 'hero': hero}
    return render(request, 'home.html', context)


def news(request):
    news = News.objects.all().order_by('-created_at')
    sort_by =  request.GET.get('sort')

    if sort_by == 'firstTeam':
        news = news.filter(category="الفريق الأول")
    elif sort_by == 'volleyball':
        news = news.filter(category="الطائرة")
    elif sort_by == 'academy':
        news = news.filter(category="الأكاديمية")
    elif sort_by == 'club':
        news = news.filter(category="النادي")


    context = {'news': news}
    return render(request, 'news.html', context)

def newsDetail(request, pk):
    news = News.objects.get(id=pk)

    context = {'news': news}
    return render(request, 'newsDetail.html', context)


def media(request):
    media = Media.objects.all().order_by('-created_at')
    sort_by =  request.GET.get('sort')

    if sort_by == 'highligts':
        media = media.filter(category="الملخصات")
    elif sort_by == 'archieve':
        media = media.filter(category="الأرشيف")
    elif sort_by == 'meetings':
        media = media.filter(category="لقاءات إعلامية")
    elif sort_by == 'volleyball':
        media = media.filter(category="الطائرة")

    context = {'media': media}
    return render(request, 'media.html', context)


def players(request):
    players = Player.objects.all().order_by('number')
    sort_by =  request.GET.get('sort')

    if sort_by == 'firstTeam':
        players = players.filter(category="الفريق الأول")
    elif sort_by == 'volleyball':
        players = players.filter(category="الطائرة")


    context = {'players': players}
    return render(request, 'players.html', context)


def matchDetail(request, pk):
    match = Match.objects.get(id=pk)

    context = {'match': match}
    return render(request, 'matchDetail.html', context)
