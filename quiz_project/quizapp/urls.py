


from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'quizapp'
urlpatterns = [
    path('', views.courses, name='courses'),
    path('resultat', views.resultat, name='resultat'),
    path('<int:id>/quiz', views.quiz, name='quiz'),
    path('connect/', views.connect, name='connect'),
    path('suscribe/', views.inscription, name='suscribe'),


]