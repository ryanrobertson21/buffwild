from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from . models import *

def home(request):
    sold = Image.objects.filter(~Q(ownerWallet='Locked'))
    sold = round(sold.count() / 100, 2)
    context = {}
    context['sold'] = sold
    return render(request, 'main/home.html', context)

def chest(request):
    images = ImageTwo.objects.all()
    images= sorted(images, key= lambda image:int(image.uniqueId))

    context = {}

    context['images'] = images
    return render(request, 'main/chest.html', context)

def collection(request):
    images = Image.objects.all()
    images= sorted(images, key= lambda image:int(image.uniqueId))

    if request.GET.get('unlocked'):
        print('here 1')
        images = Image.objects.filter(~Q(ownerWallet='Locked'))
        images= sorted(images, key=lambda image:int(image.uniqueId))

    if request.GET.get('1of1'):
        print('here 2')
        images = Image.objects.filter(uniqueId__gte=9910)
        images= sorted(images, key=lambda image:int(image.uniqueId))

    if request.GET.get('1of1') and request.GET.get('unlocked'):
        print('here 3')
        images = Image.objects.filter(~Q(ownerWallet='Locked'), uniqueId__gte=9910)
        images= sorted(images, key=lambda image:int(image.uniqueId))

    page = request.GET.get('page', 1)
    paginator = Paginator(images, 200)

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)


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

def test4(request):
    return render(request, 'main/test4.html')

def walletLookup(request):
    images=None
    if request.GET.get('searchWal'):
        search = request.GET.get('searchWal')
        images = Image.objects.filter(ownerWallet=search)
        images= sorted(images, key=lambda image:int(image.uniqueId))
        images2 = ImageTwo.objects.filter(ownerWallet=search)
        images2= sorted(images2, key=lambda image:int(image.uniqueId))
        images = images + images2
    try:
        if request.GET.get('searchNum'):
            search = request.GET.get('searchNum')
            if int(search) > 10000:
                images = ImageTwo.objects.filter(uniqueId=search.lstrip('0'))
                images= sorted(images, key= lambda image:int(image.uniqueId))
            else:
                images = Image.objects.filter(uniqueId=search.lstrip('0'))
                images= sorted(images, key= lambda image:int(image.uniqueId))

    except ValueError: ## This prevents someone who searches for anything but a number from breaking the page
            print("Invalid Search. Numbers only")


    return render(request, 'main/walletLookup.html',{
        'images': images,
    })


def error_404_view(request, exception):
    return render(request, 'main/404.html')

def error_500_view(request):
    return render(request, 'main/500.html')
