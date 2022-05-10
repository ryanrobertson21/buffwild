from django.shortcuts import render
from django.http import HttpResponse
from . models import *

def home(request):
    return render(request, 'main/home.html')

def collection(request):
    images = Image.objects.all()
    context = {}
    context['images'] = images
    return render(request, 'main/collection.html', context)

def cover(request):
    return render(request, 'main/cover.html')

def about(request):
    return render(request, 'main/about.html')

def instructions(request):
    return render(request, 'main/instructions.html')

def test(request):
    return render(request, 'main/test.html')

def walletLookup(request):
    images=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        images = Image.objects.filter(ownerWallet=search)

    return render(request, 'main/walletLookup.html',{
        'images': images,
    })

def error_404_view(request, exception):
    return render(request, 'main/404.html')

def error_500_view(request):
    return render(request, 'main/500.html')
