from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.

def connect(request):
    if request.method == "POST":
        message = ''
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        _next = request.GET.get('next', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:

            print("user is login")
            
            login(request, user)
            if _next: 
                return redirect(_next)
            else:
                return redirect('index')
        else:
            return render(request, 'pages/quiz/inscription.html')
    return render(request, 'pages/quiz/connexion.html')

# @login_required(login_url='quizapp:connect')
def courses(request):
    levels = Level.objects.filter(statut= True)
    
    data={
        'levels':levels
    }
    return render(request, 'pages/quiz/courses.html',data)

# @login_required(login_url='quizapp:connect')
def resultat(request):
    
    data={}
    return render(request, 'pages/quiz/resultat.html',data)

# @login_required(login_url='quizapp:connect')
def quiz(request, id):

    questions = quiz.objects.filter(level__id= id)
    
    data={
        'questions': questions
    }
    return render(request, 'pages/quiz/quiz.html',data)


def inscription(request):
    return render(request, 'pages/quiz/inscription.html')

