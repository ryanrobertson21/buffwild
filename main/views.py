from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def home(request):
    context_dict = {}
    files = os.listdir(os.path.join(settings.STATICFILES_DIRS, "unlocked/"))
    context_dict['files'] = files
    return render(request, 'main/home.html', context=context_dict)

def about(request):
    return render(request, 'main/about.html')

def instructions(request):
    return render(request, 'main/instructions.html')
