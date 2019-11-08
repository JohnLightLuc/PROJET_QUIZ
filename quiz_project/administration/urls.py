from django.contrib import admin
from django.urls import path,include
from administration import views

app_name = 'administrationapp'
urlpatterns = [
    path('', views.logIn, name='login'),
    path('home/', views.home, name='home'),
    path('best/', views.best, name='best'),
    path("logout/", views.logout_view, name="logout"),

]