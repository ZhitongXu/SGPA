from django.http import JsonResponse
import json
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'network/home.html')


def intro(request):
    return render(request, 'network/intro.html')


def growth(request):
    return render(request, 'network/growth.html')


def abroad(request):
    return render(request, 'network/abroad.html')


def china(request):
    return render(request, 'network/china.html')


def univ(request, univname):
    context = {}
    context['univ'] = univname
    mydic = {
        'fudan' : '复旦大学',
        'peking' : '北京大学',
        'nankai' : '南开大学',
        'ruc' : '中国人民大学',
        'tsinghua' : '清华大学',
        'xiamen' : '厦门大学',
    }
    context['dic'] = mydic
    return render(request, 'network/univ.html', context)


def univ_abroad(request, univname):
    context = {}
    context['univ'] = univname
    context['address'] = 'network/media/' + univname + '.png'
    mydic = {
        'yale' : '耶鲁大学',
        'stanford' : '斯坦福大学',
        'oxford' : '牛津大学',
        'princeton' : '普林斯顿大学',
        'mit' : '麻省理工学院',
        'harvard' : '哈佛大学',
        'columbia': '哥伦比亚大学',
        'harvard': '哈佛大学',
        'cmu': '卡耐基梅隆大学',
        'michigan': '密歇根大学',
        'australian': '澳洲国立大学',
        'penn': '宾夕法尼亚大学',
        'toronto': '多伦多大学',
        'berkeley': '加州大学伯克利分校',
        'cambridge': '剑桥大学',
        'chicago': '芝加哥大学',
    }
    context['dic'] = mydic
    return render(request, 'network/univ_abroad.html', context)


def graph(request, univname):
    with open("static/network/media/data/" + univname + ".json", 'r', encoding='utf-8')as f:
        return JsonResponse(json.load(f))


def recommend(request):
    return render(request, 'network/recommend.html')


def match(request):
    return render(request, 'network/match.html')


