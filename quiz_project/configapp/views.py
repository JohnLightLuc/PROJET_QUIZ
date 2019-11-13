from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    home = SecondSectionIndex.objects.filter(statut=True)
    print(home)
    data={
        'home': home,
    }
    return render(request, 'pages/home/home.html')