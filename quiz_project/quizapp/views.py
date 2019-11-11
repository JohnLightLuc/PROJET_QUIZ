from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .models import *


# Create your views here.

def connect(request):
    if request.method == "POST":
        message = ""
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
                return redirect('quizapp:courses')
        else:
            message = "Le username ou mot de passe incorrect"
            return render(request, 'pages/quiz/connexion.html', {'message': message})
    return render(request, 'pages/quiz/connexion.html')

@login_required(login_url='connect/')
def courses(request):
    levels = Level.objects.filter(statut= True)
    
    data={
        'levels':levels
    }
    return render(request, 'pages/quiz/courses.html',data)

@login_required(login_url='connect/')
def resultat(request):
    
    data={}
    return render(request, 'pages/quiz/resultat.html',data)

@login_required(login_url='connect/')
def quiz(request, id):

    questions = Question.objects.filter(statut=True)
    print(questions)
    paginator = Paginator(questions, 1)
    page = request.GET.get('page')
    try:
        question = paginator.get_page(page)
    except EmptyPage:
        question = paginator(1)
    except PageNotAnInteger:
        question = paginator(paginator.num_pages)
    data={
        'question': question,
        'questions': questions
    }
    print(question)
    return render(request, 'pages/quiz/quiz.html', data )


def inscription(request):
    
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2 =request.POST.get('repass')
        if password == password2:
            try:
                user = User(username = username, email= email, password= password)
                user.save()
                message = "Vous avez été enregistré avec succes! "
            except:
                message = "Erreur d'enregistrement ! "
    else:
        message = "Bienvenue"
    return render(request, 'pages/quiz/inscription.html', {'message': message})


def deconnexion(request):
    logout(request)
    return redirect('siteapp:index') 
