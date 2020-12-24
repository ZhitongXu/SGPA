from django.urls import path
from . import views

urlpatterns = [
    path('ques/', views.ques, name='ques'),
]

