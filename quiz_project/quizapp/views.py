from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='siteapp:home')
def courses(request):
    
    data={}
    return render(request, 'pages/quiz/courses.html',data)

@login_required(login_url='siteapp:home')
def resultat(request):
    
    data={}
    return render(request, 'pages/quiz/resultat.html',data)

@login_required(login_url='siteapp:home')
def quiz(request):
    
    data={}
    return render(request, 'pages/quiz/quiz.html',data)
