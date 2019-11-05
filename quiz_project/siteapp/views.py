from django.shortcuts import render

# Create your views here.


def index(request):
    
    data={}
    return render(request, 'pages/siteapp/home.html',data)

def contact(request):
    
    data={}
    return render(request, 'pages/siteapp/contact.html',data)