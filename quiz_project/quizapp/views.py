from django.shortcuts import render

# Create your views here.

def courses(request):
    
    data={}
    return render(request, 'pages/quiz/courses.html',data)

def resultat(request):
    
    data={}
    return render(request, 'pages/quiz/resultat.html',data)

def quiz(request):
    
    data={}
    return render(request, 'pages/quiz/quiz.html',data)
