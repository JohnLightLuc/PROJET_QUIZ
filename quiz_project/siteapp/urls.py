


from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'siteapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),


]