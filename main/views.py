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
    print('a')
    images = Image.objects.filter(~Q(forSale='No'))
    print(type(images))
    for i in images:
        print(i)
        print(type(i))
        break
    print('b')
    images = sorted(images, key= lambda image:int(image.uniqueId))
    print(type(images))
    for i in images:
        print(i)
        print(type(i))
        break
    images2 = ImageTwo.objects.filter(~Q(forSale='No'))
    images2 = sorted(images2, key= lambda image:int(image.uniqueId))
    images = images + images2
    images = sorted(images, key= lambda image:int(image.uniqueId))
    traits = Trait.objects.all()
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
    old_local_wild_path = "/Users/RyanRobertson21/PycharmProjects/xrd/12-automated_token_sale/wildTickets.pickle"
    local_wild_path = "C:\\Users\\rtrob\\my_projects\\xrdPayment\\12-automated_token_sale\\wildTickets.pickle"
    production_wild_path = "/home/RyanRobertson21/xrdPayment/12-automated_token_sale/wildTickets.pickle"
    context = {}
    left = len(read_pickle_file(production_wild_path))
    context['left'] = left
    redeemed = 40000 - left
    print('l')
    print(left)
    print(redeemed)
    redeemed = round(redeemed / 400, 2)
    print('here wild redeemed')
    print(redeemed)
    context['redeemed'] = redeemed

    buff = 0
    labagbuff = 0
    scorp = 0
    dinos = 0
    roid_boiz = 0
    robos = 0
    rippies = 0
    gnomes = 0
    radish = 0
    penguins = 0
    pandas = 0
    radoodle = 0
    cats = 0
    natty_radish = 0
    apes = 0
    hell = 0
    hoard = 0
    t_shirt = 0
    cc_hundred_thousand = 0
    cc_fifty_thousand = 0
    cc_twenty_five_thousand = 0
    cc_ten_thousand = 0
    cc_five_thousand = 0
    cc_two_thousand_five_hundred = 0
    cc_one_thousand = 0
    cc_five_hundred = 0
    cc_one_hundred = 0
    print('hi')
    available_wild = read_pickle_file(production_wild_path)
    print(available_wild)

    for wild in available_wild:
        if wild <= 25:  # 25 regular buffs from collection
            buff += 1
        elif wild <= 26:  # 1 Labagarre buff, send buff1
            labagbuff += 1
        elif wild <= 29:  # 3 Scorps
            scorp += 1
        elif wild <= 69:  # 40 Dinos
            dinos += 1
        elif wild <= 79:  # 10 roid boiz
            roid_boiz += 1
        elif wild <= 89:  # 10 robos
            robos += 1
        elif wild <= 99:  # 10 rippies
            rippies += 1
        elif wild <= 104:  # 5 gnomes
            gnomes += 1
        elif wild <= 109:  # 5 radishes
            radish += 1
        elif wild <= 114:  # 5 penguins
            penguins += 1
        elif wild <= 129:  # 15 pandas
            pandas += 1
        elif wild <= 139:  # 10 radoodles
            radoodle += 1
        elif wild <= 149:  # 10 mutant cats
            cats += 1
        elif wild <= 169:  # 20 natty radishes
            natty_radish += 1
        elif wild <= 199:  # 30 rad apes
            apes += 1
        elif wild <= 209:  # 10 hell hound cerbers
            hell += 1
        elif wild <= 229:  # 20 hoard
            hoard += 1
        elif wild <= 234:  # 5 t shirts
            t_shirt += 1
        elif wild <= 434:  # 1,000 crew
            cc_hundred_thousand += 1
        elif wild <= 834:  # 500 crew coin
            cc_fifty_thousand += 1
        elif wild <= 1234:  # 250 crew coin
            cc_twenty_five_thousand += 1
        elif wild <= 2234:  # 100 crew coin
            cc_ten_thousand += 1
        elif wild <= 4234:  # 50 crew coin
            cc_five_thousand += 1
        elif wild <= 12234:  # 25 crew coin
            cc_two_thousand_five_hundred += 1
        elif wild <= 22234:  # 10 crew coin
            cc_one_thousand += 1
        elif wild <= 39234:  # 5 crew coin
            cc_five_hundred += 1
        elif wild <= 40000:  # 1 crew coin
            cc_one_hundred += 1

    context['buff'] = buff
    context['labagbuff'] = labagbuff
    context['scorp'] = scorp
    context['dinos'] = dinos
    context['roid_boiz']= roid_boiz
    context['robos']= robos
    context['rippies']= rippies
    context['gnomes']= gnomes

    context['radish']= radish
    context['penguins']= penguins
    context['pandas']= pandas
    context['radoodle']= radoodle
    context['cats']= cats
    context['natty_radish']= natty_radish
    context['apes']= apes
    context['hell']= hell
    context['hoard']= hoard
    context['t_shirt']= t_shirt
    context['cc_hundred_thousand']= cc_hundred_thousand
    context['cc_fifty_thousand']= cc_fifty_thousand
    context['cc_twenty_five_thousand']= cc_twenty_five_thousand
    context['cc_ten_thousand']= cc_ten_thousand
    context['cc_five_thousand']= cc_five_thousand
    context['cc_two_thousand_five_hundred']= cc_two_thousand_five_hundred
    context['cc_one_thousand']= cc_one_thousand
    context['cc_five_hundred']= cc_five_hundred
    context['cc_one_hundred']= cc_one_hundred

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
