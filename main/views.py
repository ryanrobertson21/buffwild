from django.shortcuts import render
from django.http import HttpResponse
from . models import *


def home(request):
    images = Images.objects.all()
    context = {}
    context['images'] = images
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')

def instructions(request):
    return render(request, 'main/instructions.html')
