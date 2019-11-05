


from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'quizapp'
urlpatterns = [
    path('', views.courses, name='courses'),
    path('', views.resultat, name='resultat'),
    path('', views.quiz, name='quiz'),


]