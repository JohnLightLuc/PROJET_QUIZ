


from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'quizapp'

3
3
urlpatterns = [
    path('', views.level, name='courses'),
    path('quiz/<int:id>/', views.quiz, name='quiz'),
    path('quest/<int:id>/', views.quest, name='quest'),
    path('connect/', views.connect, name='connect'),
    path('suscribe/', views.inscription, name='suscribe'),
    path('logout/', views.deconnexion, name='logout'),
    path('sender/', views.senddata),
    path('resultat/', views.resultat, name='resultat'),
    path('resultats/', views.resultats, name='resultats'),
]