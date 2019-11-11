from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    home = FirstSectionIndex.objects.filter(statut=True)
    data={
        'home': home,
    }
    return render(request, 'pages/home/home.html',data)