from django.shortcuts import render
from .models import Keyword


# Create your views here.
def ball(request):
    keywords = Keyword.objects.filter(type="level1")
    context = {
        'keywords': keywords,
    }
    return render(request, 'ball/choosekeywords.html', context)


def ballone(request):
    keywords = Keyword.objects.filter(type="level21")
    context = {
        'keywords': keywords,
    }
    return render(request, 'ball/choosekeywords.html', context)


def balltwo(request):
    keywords = Keyword.objects.filter(type__in=['mm', 'model selection', 'machine learning', 'theoretic statistics', 'bayesian inference', 'bio statistics'])
    context = {
        'keywords': keywords,
    }
    return render(request, 'ball/choosekeywords.html', context)


def ballthree(request):
    keywords = Keyword.objects.filter(type="level23")
    context = {
        'keywords': keywords,
    }
    return render(request, 'ball/choosekeywords.html', context)


def nextball(request):
    keywords = Keyword.objects.filter(type="level3")
    context = {
        'keywords': keywords,
    }
    return render(request, 'ball/choosekeywords.html', context)
