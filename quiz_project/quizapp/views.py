from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def connect(request):
    if request.method == "POST":
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
                return redirect('home')
        else:
            return render(request, 'pages/quiz/connexion.html')
    return render(request, 'pages/quiz/connexion.html')

@login_required(login_url='quizapp:connect')
def courses(request):
    
    data={}
    return render(request, 'pages/quiz/courses.html',data)

@login_required(login_url='quizapp:connect')
def resultat(request):
    
    data={}
    return render(request, 'pages/quiz/resultat.html',data)

@login_required(login_url='quizapp:connect')
def quiz(request):
    
    data={}
    return render(request, 'pages/quiz/quiz.html',data)

