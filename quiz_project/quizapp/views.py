from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from .models import *
from django.db.models import Avg, Count, Sum


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
    quiz = Quiz.objects.filter(statut=True)
    
    data={
        'levels':levels,
        'quiz':quiz,
    }
    return render(request, 'pages/quiz/courses.html',data)

@login_required(login_url='connect/')
def resultat(request):
    resut = Resultat.objects.all().order_by('-id')[:1]
    data={
        'resut': resut
    }
    return render(request, 'pages/quiz/resultat.html',data)

@login_required(login_url='connect/')
def quiz(request,id):

    quiz = Quiz.objects.filter(level__id= id)
    data={
        'quiz': quiz,
    }
    return render(request, 'pages/quiz/quizs.html', data )
    

def quest(request,id):
    
    quiz = Quiz.objects.filter(statut=True)
    totalquest = Quiz.objects.filter(statut=True).count()
    somme = Question.objects.filter(statut=True).aggregate(point = Sum('point'))

    print("totalquest = ", totalquest)
    point_total = somme['point']
    data={
        'quiz': quiz,
        'totalquest':totalquest,
        'point_total': point_total,
    }
    return render(request, 'pages/quiz/quiz.html', data )

def senddata(request):
    send= False
    postdata = json.loads(request.body.decode('utf-8'))
    # if user.is_authenticated:
    points = postdata['point']
    taux = postdata['taux']
    util = User.objects.get(username='john')
    quiz = Quiz.objects.get(id=1)
    try:
        result = Resultat()
        result.quiz_id = quiz
        result.user_id = util
        result.note = points
        result.taux = taux
        result.save()
        send= True
    except:
        print("erreur deregidstre")
        send= False
    datas = {
    'send': send,
    }
    return JsonResponse(datas, safe=False)



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
    
