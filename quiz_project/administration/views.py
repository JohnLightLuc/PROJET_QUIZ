from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'pages/admin/login.html')

def home(request):
    return render(request, 'pages/admin/index.html')

def best(request):
    return render(request, 'pages/admin/best.html')