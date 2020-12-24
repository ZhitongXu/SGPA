from django.urls import path
from . import views

urlpatterns = [
    path('', views.openintro, name='open-intro'),
    path('openintro/', views.openintro, name='open-intro')
]
