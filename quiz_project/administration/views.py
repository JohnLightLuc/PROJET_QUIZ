from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='siteapp:home')
def login(request):
    return render(request, 'pages/admin/login.html')

@login_required(login_url='siteapp:home')
def home(request):
    return render(request, 'pages/admin/index.html')

@login_required(login_url='siteapp:home')
def best(request):
    return render(request, 'pages/admin/best.html')



def connexion(request):
    postdata = json.loads(request.body.decode('utf-8'))
    username=postdata['username']
    password=postdata['password']
    print("###################user", username) 
    print("###################user", password) 
    user = authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        print("###################user is login")   
        login(request, user)

        data={
            'success':True,
            'message':'connecte'
        }

    else:

        data={
            'success':False,
            'message':'Erro Login...'
        }
    return JsonResponse(data, safe=False)

def logout_view(request):
    logout(request)
    return redirect('blog:home')