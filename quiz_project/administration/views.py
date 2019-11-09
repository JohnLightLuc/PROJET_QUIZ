from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def logIn(request):
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
            return render(request, 'login')
    return render(request, 'login')
    return render(request, 'pages/admin/login.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'pages/admin/index.html')


def best(request):
    return render(request, 'pages/admin/best.html')

    

def logout_view(request):
    logout(request)
    return redirect('blog:home')