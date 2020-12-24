from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='network-home'),
    path('intro/', views.intro, name='intro'),
    path('growth/', views.growth, name='growth'),
    path('abroad/', views.abroad, name='abroad'),
    path('abroad/univ/<str:univname>', views.univ_abroad, name='univ_abroad'),
    path('china/', views.china, name='china'),
    path('china/univ/<str:univname>', views.univ, name='univ_chs'),
    path('graph/<str:univname>', views.graph, name='graph'),
    path('recommend/', views.recommend, name='recommend'),
    path('match/', views.match, name='match'),
]
