


from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'quizapp'
urlpatterns = [
    path('', views.courses, name='courses'),
    path('resultat', views.resultat, name='resultat'),
    path('quiz/<int:id>/', views.quiz, name='quiz'),
    path('quest/<int:id>/', views.quest, name='quest'),
    path('connect/', views.connect, name='connect'),
    path('suscribe/', views.inscription, name='suscribe'),
    path('logout/', views.deconnexion, name='logout'),
    path('sender/', views.senddata),
]