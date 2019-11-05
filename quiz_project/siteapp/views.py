from django.shortcuts import render

# Create your views here.


def home(request):
    
    data={}
    return render(request, 'pages/sites/home.html',data)

def contact(request):
    
    data={}
    return render(request, 'pages/sites/contact.html',data)