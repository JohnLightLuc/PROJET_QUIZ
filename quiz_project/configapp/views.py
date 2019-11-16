from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    nan = Nan.objects.filter(statut=True)
    data={
        'nan': nan,
    }
    return render(request, 'pages/home/home.html', data)