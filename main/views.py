from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from . models import *
import pickle

def home(request):
    #sold = Image.objects.filter(~Q(ownerWallet='Locked'))
    #sold = round(sold.count() / 100, 2)

    local_avail_buffs_path = "/Users/RyanRobertson21/PycharmProjects/xrd/12-automated_token_sale/availableBuffs.pickle"
    production_avail_buffs_path = "/home/RyanRobertson21/xrdPayment/12-automated_token_sale/availableBuffs.pickle"

    context = {}

    left = len(read_pickle_file(production_avail_buffs_path))
    context['left'] = left
    print(left)
    sold = 10000 - left
    sold = round(sold / 100, 2)
    print('here avail buffs')
    print(sold)
    context['sold'] = sold
    #context['sold'] = sold
    return render(request, 'main/home.html', context)

def chest(request):
    images = ImageTwo.objects.all()
    images= sorted(images, key= lambda image:int(image.uniqueId))

    context = {}

    context['images'] = images
    return render(request, 'main/chest.html', context)

def trading(request):
    images = Image.objects.filter(~Q(forSale='No'))
    images= sorted(images, key= lambda image:int(image.uniqueId))
    images2 = ImageTwo.objects.filter(~Q(forSale='No'))
    images2= sorted(images2, key= lambda image:int(image.uniqueId))
    images = images + images2
    images= sorted(images, key= lambda image:int(image.uniqueId))

    context = {}

    context['images'] = images
    return render(request, 'main/trading.html', context)

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

def read_pickle_file(path):
    try:
        with open(path, 'rb') as f:
            file = pickle.load(f)
            return file
    except EOFError:
        return 10000

def instructions(request):
    local_wild_path = "/Users/RyanRobertson21/PycharmProjects/xrd/12-automated_token_sale/wildTickets.pickle"
    production_wild_path = "/home/RyanRobertson21/xrdPayment/12-automated_token_sale/wildTickets.pickle"
    context = {}
    left = len(read_pickle_file(production_wild_path))
    context['left'] = left
    redeemed = 10000 - left
    redeemed = round(redeemed / 100, 2)
    print('here wild redeemed')
    print(redeemed)
    context['redeemed'] = redeemed
    return render(request, 'main/instructions.html', context)

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
