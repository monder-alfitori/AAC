from django.shortcuts import render

# Create your views here.
def home(request):

    context = {}
    return render(request, 'home.html', context)


def news(request):

    context = {}
    return render(request, 'news.html', context)

def media(request):
    
    context = {}
    return render(request, 'media.html', context)


def players(request):
    
    context = {}
    return render(request, 'players.html', context)
