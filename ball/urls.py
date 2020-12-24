from django.urls import path
from . import views

urlpatterns = [
    path('choosekeywords/', views.ball, name='ball'),
    path('choosekeywords/ballone', views.ballone, name='ballone'),
    path('choosekeywords/balltwo', views.balltwo, name='balltwo'),
    path('choosekeywords/ballthree', views.ballthree, name='ballthree'),
    path('choosekeywords/nextball', views.nextball, name='nextball'),
]

