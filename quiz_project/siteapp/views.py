from django.shortcuts import render
import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.http import JsonResponse

from django.contrib.auth.models import User
from .models import *
# Create your views here.


def index(request):
    
    data={}
    return render(request, 'pages/home/home.html',data)

def contact(request):
    
    data={}
    return render(request, 'pages/home/contact.html',data)


def connexion(request):
    postdata = json.loads(request.body.decode('utf-8'))
    email=postdata['email']
    password=postdata['password']
    print("###################user", email) 
    print("###################user", password) 
    user = authenticate(email=email, password=password)
    
    if user is not None and user.is_active:
        print("###################user is login")   
        login(request, user)

        data={
            'success':True,
            'message':'connecte'
        }
        return redirect('quizapp:courses')

    else:

        data={
            'success':False,
            'message':'Erro Login...'
        }
    return JsonResponse(data, safe=False)

def logout_view(request):
    logout(request)
    return redirect('blog:home')