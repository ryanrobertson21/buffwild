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

def instructions(request):
    return render(request, 'main/instructions.html')

def terms(request):
    return render(request, 'main/terms.html')

def test(request):
    return render(request, 'main/test.html')

def walletLookup(request):
    images=None
    if request.GET.get('searchWal'):
        search = request.GET.get('searchWal')
        images = Image.objects.filter(ownerWallet=search)
    try:
        if request.GET.get('searchNum'):
            search = request.GET.get('searchNum')
            images = Image.objects.filter(uniqueId=search)
    except ValueError: ## This prevents someone who searches for anything but a number from breaking the page
            print("Invalid Search. Numbers only")


    return render(request, 'main/walletLookup.html',{
        'images': images,
    })


def error_404_view(request, exception):
    return render(request, 'main/404.html')

def error_500_view(request):
    return render(request, 'main/500.html')
