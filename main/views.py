from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from . models import *
import pickle
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SummarySerializer, BuffPlainSerializer, BuffSerializer, BuffSerializerTwo
from .pagination import StandardResultsSetPagination
from itertools import chain

from django.views.generic import View, TemplateView

def home(request):
    #sold = Image.objects.filter(~Q(ownerWallet='Locked'))
    #sold = round(sold.count() / 100, 2)

    old_local_avail_buffs_path = "/Users/RyanRobertson21/PycharmProjects/xrd/12-automated_token_sale/availableBuffs.pickle"
    local_avail_buffs_path = "C:\\Users\\rtrob\\my_projects\\xrdPayment\\12-automated_token_sale\\availableBuffs.pickle"
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



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@api_view(['GET'])
def trade_stats(request):
    queryList1 = Image.objects.select_related('traits').filter(~Q(ownerWallet='Locked'))
    queryList2 = ImageTwo.objects.filter(~Q(ownerWallet='Locked'))
    queryList = list(chain(queryList1, queryList2))
    owners = []
    for buff in queryList:
        if buff.ownerWallet not in owners:
            owners.append(buff.ownerWallet)
    num_owners = len(owners)
    genesis_items = 10000
    genesis_reserved = len(queryList1)
    trade_stats = TradeStats.objects.all()
    print(trade_stats[0])
    volume = trade_stats[0].manual_volume + trade_stats[0].automated_volume
    num_trades = trade_stats[0].manual_number_trades + trade_stats[0].automated_number_trades
    highest_trade = trade_stats[0].highest_trade
    asking_prices = list(filter(lambda x: x.forSale != "No", queryList))
    print('asking prices here')
    print(asking_prices)
    print('is this the floor?')
    asking_prices.sort(key=lambda x: float(x.forSale))
    floor = float(asking_prices[0].forSale)

    return JsonResponse({'genesis_items': genesis_items, 'genesis_reserved': genesis_reserved, 'floor': floor, 'volume': volume, 'num_trades': num_trades, 'highest_trade': highest_trade, 'num_owners': num_owners})

@api_view(['GET'])
def buff_list(request):
    # queryList1 = Image.objects.all()
    # queryList2 = ImageTwo.objects.all()
    # serializer1 = BuffSerializer(queryList1, many=True)
    # serializer2 = BuffSerializerTwo(queryList2, many=True)
    # print('hi, in the views here')
    # print(type(serializer1))
    # print(serializer1)
    # return JsonResponse({'buff': serializer1.data, 'buff1': serializer2.data})

    #SEE IF MAKING WALLETS_SET A DICT INSTEAD OF LIST IMPROVES LOOKUP ON THE OTHER SIDE. KEYS=WALLETS, VALUES IRRELEVANT SO CAN MAKE W/E
    queryList1 = Image.objects.filter(~Q(ownerWallet='Locked'))
    queryList2 = ImageTwo.objects.filter(~Q(ownerWallet='Locked'))
    queryList = list(chain(queryList1, queryList2))
    wallets_set = set()
    for i in queryList:
        wallets_set.add(i.ownerWallet)
    print(len(wallets_set))
    return JsonResponse({'owners': list(wallets_set)})




class MainView(TemplateView):
    template_name = 'main/collection.html'

def format_floats(value):
    float_string = str(format (value, ',f'))
    new_string = float_string.rstrip('0').rstrip('.') if '.' in float_string else float_string
    return new_string

class PostJsonListView(View):
    serializer_class = SummarySerializer
    plain_serializer_class = BuffPlainSerializer

    def get(self, *args, **kwargs):
        print('kwargs here')
        print(kwargs)
        upper = kwargs.get('num_posts')
        lower = ""
        restart = self.request.GET.get('start', None)
        loaded = self.request.GET.get('loaded', None)
        if restart:
            print('yes')
            print(restart)
            lower = int(restart)
        else:
            lower = upper - 60
        #lower = 0;
        print('here is start followed by lower')
        print(restart)
        print(lower)

        # filter the queryset based on the filters applied
        queryList1 = Image.objects.select_related('traits').filter(~Q(ownerWallet='Locked'))
        queryList2 = ImageTwo.objects.filter(~Q(ownerWallet='Locked'))
        queryList = list(chain(queryList1, queryList2))

        owners = []
        for buff in queryList:
            if buff.ownerWallet not in owners:
                owners.append(buff.ownerWallet)
        num_owners = (format (len(owners), ',d'))

        asking_prices = list(filter(lambda x: x.forSale != "No", queryList))
        print('asking prices here')
        print(asking_prices)
        print('is this the floor?')
        asking_prices.sort(key=lambda x: float(x.forSale))
        floor = format_floats(float(asking_prices[0].forSale))

        print('HERE 1')

        if self.request.GET.get('search_bar', None):
            search = self.request.GET.get('search_bar').strip()
            try:
                if int(search) <= 10390:
                    queryList = filter(lambda x: x.uniqueId == int(search), queryList)
            except ValueError: ## This prevents someone who searches for anything but a number from breaking the page
                queryList = filter(lambda x: x.ownerWallet == search, queryList)
        print('HERE 2')
        status = self.request.GET.getlist('status', None)

        series = self.request.GET.getlist('series[]', None)
        series_specific_faction_buffs = self.request.GET.getlist('series_specific_faction_buffs[]', None)
        series_specific_one_of_ones = self.request.GET.getlist('series_specific_one_of_ones[]', None)
        print(series)
        print(series_specific_faction_buffs)
        price_min = self.request.GET.get('min_price', None)
        price_max = self.request.GET.get('max_price', None)

        score_min = self.request.GET.get('min_score', None)
        score_max = self.request.GET.get('max_score', None)

        background = self.request.GET.getlist('background[]', None)
        background_specific_atmospheric = self.request.GET.getlist('background_specific_atmospheric[]', None)
        background_specific_colors = self.request.GET.getlist('background_specific_colors[]', None)
        background_specific_dimensions = self.request.GET.getlist('background_specific_dimensions[]', None)

        fur = self.request.GET.getlist('fur[]', None)
        fur_specific_standard = self.request.GET.getlist('fur_specific_standard[]', None)
        fur_specific_animal = self.request.GET.getlist('fur_specific_animal[]', None)
        fur_specific_designer = self.request.GET.getlist('fur_specific_designer[]', None)
        fur_specific_the_risen = self.request.GET.getlist('fur_specific_the_risen[]', None)
        fur_specific_the_elders = self.request.GET.getlist('fur_specific_the_elders[]', None)
        fur_specific_the_demi_buff = self.request.GET.getlist('fur_specific_the_demi_buff[]', None)
        fur_specific_white_angel = self.request.GET.getlist('fur_specific_white_angel[]', None)
        fur_specific_devilish = self.request.GET.getlist('fur_specific_devilish[]', None)

        swag = self.request.GET.getlist('swag[]', None)
        swag_specific_standard = self.request.GET.getlist('swag_specific_standard[]', None)
        swag_specific_middle_class_fancy = self.request.GET.getlist('swag_specific_middle_class_fancy[]', None)
        swag_specific_premium_swag = self.request.GET.getlist('swag_specific_premium_swag[]', None)
        swag_specific_baby_buff = self.request.GET.getlist('swag_specific_baby_buff[]', None)
        swag_specific_premium_ink = self.request.GET.getlist('swag_specific_premium_ink[]', None)
        swag_specific_premium_weapons = self.request.GET.getlist('swag_specific_premium_weapons[]', None)
        swag_specific_bane_veins = self.request.GET.getlist('swag_specific_bane_veins[]', None)
        swag_specific_symbol = self.request.GET.getlist('swag_specific_symbol[]', None)

        horns = self.request.GET.getlist('horns[]', None)
        horns_specific_standard = self.request.GET.getlist('horns_specific_standard[]', None)
        horns_specific_standard_plus = self.request.GET.getlist('horns_specific_standard_plus[]', None)
        horns_specific_variant = self.request.GET.getlist('horns_specific_variant[]', None)
        horns_specific_baby_buff = self.request.GET.getlist('horns_specific_baby_buff[]', None)
        horns_specific_animal_horns = self.request.GET.getlist('horns_specific_animal_horns[]', None)
        horns_specific_halo = self.request.GET.getlist('horns_specific_halo[]', None)
        horns_specific_the_messiah = self.request.GET.getlist('horns_specific_the_messiah[]', None)

        eyes = self.request.GET.getlist('eyes[]', None)
        eyes_specific_standard = self.request.GET.getlist('eyes_specific_standard[]', None)
        eyes_specific_eyewear = self.request.GET.getlist('eyes_specific_eyewear[]', None)
        eyes_specific_impressionable = self.request.GET.getlist('eyes_specific_impressionable[]', None)
        eyes_specific_battle_ridden = self.request.GET.getlist('eyes_specific_battle_ridden[]', None)
        eyes_specific_beams = self.request.GET.getlist('eyes_specific_beams[]', None)
        eyes_specific_betrayer = self.request.GET.getlist('eyes_specific_betrayer[]', None)

        mouth = self.request.GET.getlist('mouth[]', None)
        mouth_specific_standard = self.request.GET.getlist('mouth_specific_standard[]', None)
        mouth_specific_kewl = self.request.GET.getlist('mouth_specific_kewl[]', None)
        mouth_specific_cool_guy = self.request.GET.getlist('mouth_specific_cool_guy[]', None)
        mouth_specific_bull_rings = self.request.GET.getlist('mouth_specific_bull_rings[]', None)
        mouth_specific_heated = self.request.GET.getlist('mouth_specific_heated[]', None)
        mouth_specific_prehistoric = self.request.GET.getlist('mouth_specific_prehistoric[]', None)

        smoking = self.request.GET.getlist('smoking[]', None)
        smoking_specific_yes = self.request.GET.getlist('smoking_specific_yes[]', None)
        smoking_specific_no = self.request.GET.getlist('smoking_specific_no[]', None)

        double_baby = self.request.GET.getlist('double_baby[]', None)
        double_baby_specific_no = self.request.GET.getlist('double_baby_specific_no[]', None)
        double_baby_specific_swag = self.request.GET.getlist('double_baby_specific_swag[]', None)
        double_baby_specific_horns = self.request.GET.getlist('double_baby_specific_horns[]', None)

        collections = self.request.GET.getlist('collections[]', None)
        collections_specific_yes = self.request.GET.getlist('collections_specific_yes[]', None)
        collections_specific_no = self.request.GET.getlist('collections_specific_no[]', None)

        matching = self.request.GET.getlist('matching[]', None)
        matching_specific_yes = self.request.GET.getlist('matching_specific_yes[]', None)
        matching_specific_no = self.request.GET.getlist('matching_specific_no[]', None)

        sort_by = self.request.GET.get('sort_by', None)

        buff_numbers = []

        if 'All' in status:
            queryList = queryList
        if 'For Sale' in status:
            queryList = queryList = filter(lambda x: x.forSale != "No", queryList)
        if 'Not For Sale' in status:
            queryList = queryList = filter(lambda x: x.forSale == "No", queryList)

        # faction buffs
        if 'Faction_Buffs' in series and series_specific_faction_buffs == []:
            series_specific_faction_buffs = ['Cyclops', 'Football', 'Ghost', 'Mummy', 'Pharaoh', 'Pirate', 'Buff Riders', 'La Bagarre Buff', 'Gnome Buff',
             'German Buff', 'Community Buffs', 'British Buff', 'Faction Buffs', 'Buffalo Soldier Lieutenants', 'Soldier Buffs', 'Into the Darkness Lieutenants',
             'Darkness Buffs', 'Unholy Buffalos Lieutenants', 'Unholy Buffs', 'Storm Born Lieutenants', 'Storm Born Buffs', 'Space Buff', 'Game Screenshots',
             'Radorable Buff', 'Santa Buff', 'World Cup Buff', 'Gamer Buffs', 'Workout Buffs']

        if 'Genesis_Collection_Buffs' in series:
            buff_numbers.extend(range(1,9911))
        if '1_of_1s' in series and series_specific_one_of_ones == []:
            buff_numbers.extend(range(9911, 10001))
        if 'Faction_Buffs' in series and series_specific_faction_buffs == []:
            buff_numbers.extend(range(10001, 10278))
        if 'Cyclops' in series_specific_faction_buffs:
            buff_numbers.extend(range(10001, 10007))
        if 'Football' in series_specific_faction_buffs:
            buff_numbers.extend(range(10007, 10016))
        if 'Ghost' in series_specific_faction_buffs:
            buff_numbers.append(10016)
        if 'Mummy' in series_specific_faction_buffs:
            buff_numbers.append(10017)
        if 'Pharaoh' in series_specific_faction_buffs:
            buff_numbers.append(10018)
        if 'Pirate' in series_specific_faction_buffs:
            buff_numbers.extend(range(10019, 10027))
        if 'Buff Riders' in series_specific_faction_buffs:
            buff_numbers.extend(range(10027, 10259))
        if 'La Bagarre Buff' in series_specific_faction_buffs:
            buff_numbers.append(10277)
        if 'Gnome Buff' in series_specific_faction_buffs:
            buff_numbers.append(10278)
        if 'German Buff' in series_specific_faction_buffs:
            buff_numbers.append(10279)
        if 'Community Buffs' in series_specific_faction_buffs:
            buff_numbers.extend(range(10280, 10282))
        if 'Faction Buffs' in series_specific_faction_buffs:
            buff_numbers.extend(range(10282, 10286))
        if 'British Buff' in series_specific_faction_buffs:
            buff_numbers.append(10286)
        if 'Buffalo Soldier Lieutenants' in series_specific_faction_buffs:
            buff_numbers.extend(range(10287, 10292))
        if 'Into the Darkness Lieutenants' in series_specific_faction_buffs:
            buff_numbers.extend(range(10292, 10297))
        if 'Unholy Buffalos Lieutenants' in series_specific_faction_buffs:
            buff_numbers.extend(range(10297, 10302))
        if 'Storm Born Lieutenants' in series_specific_faction_buffs:
            buff_numbers.extend(range(10302, 10307))
        if 'Space Buff' in series_specific_faction_buffs:
            buff_numbers.append(10307)
        if 'Game Screenshots' in series_specific_faction_buffs:
            buff_numbers.extend(range(10308, 10363))
        if 'Radorable Buff' in series_specific_faction_buffs:
            buff_numbers.append(10363)
        if 'Santa Buff' in series_specific_faction_buffs:
            buff_numbers.append(10364)
        if 'World Cup Buff' in series_specific_faction_buffs:
            buff_numbers.append(10365)
        if 'Gamer Buffs' in series_specific_faction_buffs:
            buff_numbers.extend(range(10366, 10370))
        if 'Darkness Buffs' in series_specific_faction_buffs:
            buff_numbers.extend(range(10370, 10374))
        if 'Soldier Buffs' in series_specific_faction_buffs:
            buff_numbers.extend(range(10374, 10378))
        if 'Storm Born Buffs' in series_specific_faction_buffs:
            buff_numbers.extend(range(10378, 10382))
        if 'Unholy Buffs' in series_specific_faction_buffs:
            buff_numbers.extend(range(10382, 10386))
        if 'Workout Buffs' in series_specific_faction_buffs:
            buff_numbers.extend(range(10386, 10391))

        # 1 of 1 buffs
        if '1_of_1s' in series and series_specific_one_of_ones == []:
            series_specific_one_of_ones = ['Angel Buff', 'Battle Buff', 'Buff God', 'Buff Ball Z', 'Bunny Buff', 'Cowboy', 'Demon Buff', 'Extinct Buff',
             'Coyote', 'Marley Buff', 'Mono Blue', 'Mono Cyan', 'Mono Green', 'Mono Orange', 'Mono Pink', 'Mono Red', 'Mono Yellow', 'Nacho Buff', 'Pixel Buff',
             'Safe Word Buff', 'Shadow Buff', 'Trippy', 'Wolf', 'Wooly', 'Zombie Buff']

        if 'Angel Buff' in series_specific_one_of_ones:
            buff_numbers.append(9911)
        if 'Battle Buff' in series_specific_one_of_ones:
            buff_numbers.extend(range(9912, 9920))
        if 'Buff God' in series_specific_one_of_ones:
            buff_numbers.extend(range(9920, 9930))
        if 'Buff Ball Z' in series_specific_one_of_ones:
            buff_numbers.append(9930)
        if 'Bunny Buff' in series_specific_one_of_ones:
            buff_numbers.extend(range(9931, 9934))
        if 'Cowboy' in series_specific_one_of_ones:
            buff_numbers.append(9934)
        if 'Demon Buff' in series_specific_one_of_ones:
            buff_numbers.append(9935)
        if 'Extinct Buff' in series_specific_one_of_ones:
            buff_numbers.append(9936)
        if 'Coyote' in series_specific_one_of_ones:
            buff_numbers.extend(range(9937, 9947))
        if 'Marley Buff' in series_specific_one_of_ones:
            buff_numbers.append(9947)
        if 'Mono Blue' in series_specific_one_of_ones:
            buff_numbers.extend(range(9948, 9950))
        if 'Mono Cyan' in series_specific_one_of_ones:
            buff_numbers.extend(range(9951, 9953))
        if 'Mono Green' in series_specific_one_of_ones:
            buff_numbers.extend(range(9954, 9957))
        if 'Mono Orange' in series_specific_one_of_ones:
            buff_numbers.extend(range(9957, 9960))
        if 'Mono Pink' in series_specific_one_of_ones:
            buff_numbers.extend(range(9960, 9963))
        if 'Mono Red' in series_specific_one_of_ones:
            buff_numbers.extend(range(9963, 9966))
        if 'Mono Yellow' in series_specific_one_of_ones:
            buff_numbers.extend(range(9966, 9969))
        if 'Nacho Buff' in series_specific_one_of_ones:
            buff_numbers.extend(range(9969, 9972))
        if 'Pixel Buff' in series_specific_one_of_ones:
            buff_numbers.append(9972)
        if 'Safe Word Buff' in series_specific_one_of_ones:
            buff_numbers.extend(range(9973, 9976))
        if 'Shadow Buff' in series_specific_one_of_ones:
            buff_numbers.extend(range(9976, 9984))
        if 'Trippy' in series_specific_one_of_ones:
            buff_numbers.append(9984)
        if 'Wolf' in series_specific_one_of_ones:
            buff_numbers.extend(range(9985, 9995))
        if 'Wooly' in series_specific_one_of_ones:
            buff_numbers.extend(range(9995, 10000))
        if 'Zombie Buff' in series_specific_one_of_ones:
            buff_numbers.append(10000)
        print('buff numbs')
        print(buff_numbers)
        if len(buff_numbers) > 0:
            print('we in buff numbers')

            queryList = filter(lambda x: x.uniqueId in buff_numbers, queryList)


        if price_min:
            queryList = filter(lambda x: x.forSale != "No", queryList)
            queryList = filter(lambda x: float(x.forSale) >= float(price_min), queryList)

        if price_max:
            queryList = filter(lambda x: x.forSale != "No", queryList)
            queryList = filter(lambda x: float(x.forSale) <= float(price_max), queryList)

        if score_min:
            queryList = filter(lambda x: x.uniqueId <= 9910 and float(x.traits.total_buff_score) >= float(score_min), queryList)

        if score_max:
            queryList = filter(lambda x: x.uniqueId <= 9910 and float(x.traits.total_buff_score) <= float(score_max), queryList)





        if 'Atmospheric' in background and background_specific_atmospheric == []:
            background_specific_atmospheric = ["Starry Night", "Towards the Storm", "Tornado", "Highlands", "Graveyard", "Alien World"]
        if 'Colors' in background and background_specific_colors == []:
            background_specific_colors = ['Desert Yellow', 'Green', 'Grey', 'Gue Pink', 'Ice Blue', 'Purple', 'Red']
        if 'Dimensions' in background and background_specific_dimensions == []:
            background_specific_dimensions = ['Heaven', 'Hellfire', 'Trippy', 'Matrix']

        if 'Standard' in fur and fur_specific_standard == []:
            fur_specific_standard = ["Purple", "Base Buff", "Browny", "Ginger Snap", "Green", "Gue Pink", "Ice Blue", "War Paint Pink", "War Paint", "Trippy", "Trippy Red"]
        if 'Animal' in fur and fur_specific_animal == []:
            fur_specific_animal = ["Black Leopard", "Cheetah", "Cheetah Blue", "Leopard Green", "Reverse Zebra Blue", "Reverse Zebra Red", "Reverse Zebra", "Zebra", "Zebra Yellow"]
        if 'Designer' in fur and fur_specific_designer == []:
            fur_specific_designer = ["Static Noise", "Static Noise Blue", "80's Wave Freaking Me Out", "Heat Wave Freaking Me Out", "The Bas", "The Bas Yellow"]
        if 'The_Risen' in fur and fur_specific_the_risen == []:
            fur_specific_the_risen = ["Zombie", "Zombie Red"]
        if 'The_Elders' in fur and fur_specific_the_elders == []:
            fur_specific_the_elders = ["Braided", "Black Leopard War Paint"]
        if 'The_Demi_Buff' in fur and fur_specific_the_demi_buff == []:
            fur_specific_the_demi_buff = ["Black Angel"]
        if 'White_Angel' in fur and fur_specific_white_angel == []:
            fur_specific_white_angel = ["Angel"]
        if 'Devilish' in fur and fur_specific_devilish == []:
            fur_specific_devilish = ["Devil"]

        if 'Standard' in swag and swag_specific_standard == []:
            swag_specific_standard = ["Chadagonia Blue", "Chadagonia Yellow", "Chadagonia Red", "Chadagonia Green", "Chadagonia Black", "Ryan", "Easter Morning", "Super Hero", "Hippie Vest", "No Swag", "Don't Drop The Soap", "Hoodie Green", "Can't Swim Mom", "Floaty Blue", "Top Chef", "Beater", "Trouble Maker", "XSEED Tribute", "Mom", "Reaper"]
        if 'Middle_Class_Fancy' in swag and swag_specific_middle_class_fancy == []:
            swag_specific_middle_class_fancy = ["BAMF", "Bullet Proof Vest", "Thug Life", "Buff Athletics Blue", "Buff Athletics Green", "Buff Athletics Pink", "The Executioner", "Rough Rider", "Chain Mail", "The Bludgeoner", "The Staff", "Excalibur", "Pilgrim", "Radix", "Area 51"]
        if 'Premium_Swag' in swag and swag_specific_premium_swag == []:
            swag_specific_premium_swag = ["The Name's Buff, James Buff", "Dr. Buff", "Desert Walker", "Over 9000", "Jet Pack", "No. 1", "Wild West", "Red Rider", "Impaled", "Champ Champ", "Alchemist"]
        if 'Baby_Buff' in swag and swag_specific_baby_buff == []:
            swag_specific_baby_buff = ["Baby Buff Bag Hiding Brown", "Baby Buff Bag Hiding Green", "Baby Buff Bag Hiding Pink", "Young Padabuff", "Baby Buff Bag Peaking Blue"]
        if 'Premium_Ink' in swag and swag_specific_premium_ink == []:
            swag_specific_premium_ink = ["Skull Wings", "FuccBoi Buff", "Dragon Tattoo", "Island Bruh"]
        if 'Premium_Weapons' in swag and swag_specific_premium_weapons == []:
            swag_specific_premium_weapons = ["Chainmail with The Staff", "Chainmail Excalibur", "Not Since Nam", "Space Warrior"]
        if 'Bane_Veins' in swag and swag_specific_bane_veins == []:
            swag_specific_bane_veins = ["Veins", "Bane"]
        if 'Symbol' in swag and swag_specific_symbol == []:
            swag_specific_symbol = ["野牛"]

        if 'Standard' in horns and horns_specific_standard == []:
            horns_specific_standard = ["The Marley", "Mohawk", "Braided Head", "Bra and Panties", "Mardi Gras Beads", "Conical Hat", "Horn Piercing", "Farmer Tags", "Buff Horns", "Ball And Chain", "Alien Protection Tin", "Broken Horns", "Feather Earrings"]
        if 'Standard_Plus' in horns and horns_specific_standard_plus == []:
            horns_specific_standard_plus = ["Cowboy Hat", "Chieftan", "Toboggan", "Potara Earings", "Coo Coo Cachoo", "Green Snap Back", "Pink Snap Back", "No Horns", "Guzzler Helmet", "Bloody"]
        if 'Variant' in horns and horns_specific_variant == []:
            horns_specific_variant = ["White Black Fade", "White Horns", "Metallic Horns", "Golden Tips", "Black to Red Fade", "Tie Dyed Horns", "Large Horns", "The Splinter"]
        if 'Baby_Buff' in horns and horns_specific_baby_buff == []:
            horns_specific_baby_buff = ["Baby Buff Blue", "Baby Buff Pink", "Baby Buff Green", "Baby Buff Brown", "Demon Baby Buff"]
        if 'Animal_Horns' in horns and horns_specific_animal_horns == []:
            horns_specific_animal_horns = ["Moose Antlers", "Moose Antlers Black", "Deer Antlers", "Deer Antlers Black"]
        if 'Halo' in horns and horns_specific_halo == []:
            horns_specific_halo = ["Demon Horns", "Halo"]
        if 'The_Messiah' in horns and horns_specific_the_messiah == []:
            horns_specific_the_messiah = ["Messiah's Crown"]

        if 'Standard' in eyes and eyes_specific_standard == []:
            eyes_specific_standard = ["Bored Eyes", "Confused", "Cry Baby", "Ragin' Bull", "Green Eyes", "Purple Eyes", "Red Eyes", "Bloodshot", "Wide Eyes", "Squinty"]
        if 'Eyewear' in eyes and eyes_specific_eyewear == []:
            eyes_specific_eyewear = ["Aviators", "Dude Shades", "Morpheus", "Spectacles", "Monocle", "Scouter", "Cyborg"]
        if 'Impressionable' in eyes and eyes_specific_impressionable == []:
            eyes_specific_impressionable = ["Starry Eyes", "Dizzy", "Baked", "Radix Eyes", "Sleeping"]
        if 'Battle_Ridden' in eyes and eyes_specific_battle_ridden == []:
            eyes_specific_battle_ridden = ["Open Scar", "Closed Scar", "Danglin' Eyes", "Demon Eyes"]
        if 'Beams' in eyes and eyes_specific_beams == []:
            eyes_specific_beams = ["Red Beam", "Purple Beam", "Blue Beam"]
        if 'Betrayer' in eyes and eyes_specific_betrayer == []:
            eyes_specific_betrayer = ["Betrayer"]

        if 'Standard' in mouth and mouth_specific_standard == []:
            mouth_specific_standard = ["Befuddled", "Bored", "Clean", "Come at me bro", "Grinnin'", "HA HA", "Jovial", "Phoneme Vuh", "Sad", "Shocked", "Smirkin'", "Surprised", "Tired", "Wahhhh", "Whistlin' Dixie", "WOW", "Yikes!"]
        if 'KEWL' in mouth and mouth_specific_kewl == []:
            mouth_specific_kewl = ["BAMF GRILLZ", "PLAT GRILLZ", "RAINBOW GRILLZ", "GOLD GRILLZ", "Kazoo", "Pacifier", "Bloody Nose", "Baby Rattler", "Tongue Out", "Awooga!"]
        if 'Cool_Guy' in mouth and mouth_specific_cool_guy == []:
            mouth_specific_cool_guy = ["Ciggy", "The Don", "Toothpick", "Buff Chaw", "Cheesin'"]
        if 'Bull_Rings' in mouth and mouth_specific_bull_rings == []:
            mouth_specific_bull_rings = ["Gold", "Goth", "Purple", "Red"]
        if 'Heated' in mouth and mouth_specific_heated == []:
            mouth_specific_heated = ["Hot Tamale", "Hot Tamale Green", "Cheefin'"]
        if 'Prehistoric' in mouth and mouth_specific_prehistoric == []:
            mouth_specific_prehistoric = ["Troll Tusks", "Sabertooth"]

        if 'Yes' in smoking and smoking_specific_yes == []:
            smoking_specific_yes = ["The Don", "Ciggy"]
        if 'No' in smoking and smoking_specific_no == []:
            smoking_specific_no = ["Troll Tusks", "Sabertooth", "Hot Tamale", "Hot Tamale Green", "Cheefin'", "Gold", "Goth", "Purple", "Red", "Toothpick", "Buff Chaw", "Cheesin'", "BAMF GRILLZ", "PLAT GRILLZ", "RAINBOW GRILLZ", "GOLD GRILLZ", "Kazoo", "Pacifier", "Bloody Nose", "Baby Rattler", "Tongue Out", "Awooga!", "Befuddled", "Bored", "Clean", "Come at me bro", "Grinnin'", "HA HA", "Jovial", "Phoneme Vuh", "Sad", "Shocked", "Smirkin'", "Surprised", "Tired", "Wahhhh", "Whistlin' Dixie", "WOW", "Yikes!"]

        if 'Yes' in double_baby and double_baby_specific_swag == []:
            double_baby_specific_swag = ["Baby Buff Bag Hiding Brown", "Baby Buff Bag Hiding Green", "Baby Buff Bag Hiding Pink", "Young Padabuff", "Baby Buff Bag Peaking Blue"]
        if 'Yes' in double_baby and double_baby_specific_horns == []:
            double_baby_specific_horns = ["Baby Buff Blue", "Baby Buff Pink", "Baby Buff Green", "Baby Buff Brown", "Demon Baby Buff"]
        if 'No' in double_baby and double_baby_specific_no == []:
            double_baby_specific_no = ["No"]


        if 'Yes' in collections and collections_specific_yes == []:
            collections_specific_yes = ["Cyborg Set", "Cowboy", "Dbz", "Matrix", "NoNo", "Undead", "Albino", "Rice Farmer", "Super Hero", "Trippy", "Gentleman", "Joseph Smith",
               "Day Walker", "Jordan", "Hells Kitchen", "Golded", "Girl", "Rasta", "Radix", "Bamf", "Frat Buff", "Demigod", "Regrets",
              "Raver", "Kiddie Pool", "Mutated", "Half Dead", "Oversized", "Easter Celebration", "Brads And Chads",
              "Chromed Out", "Natural Evolution", "Pride", "Buffs Mafia", "Family Guy", "Agent Zero", "Playboy", "Battle Hardened", "Fire"]
        if 'No' in collections and collections_specific_no == []:
            collections_specific_no = ["N/A"]
        if 'Yes' in matching and matching_specific_yes == []:
            matching_specific_yes = ["Black", "Blue", "Brown", "Green", "Orange", "Pink", "Purple", "Red", "Yellow"]
        if 'No' in matching and matching_specific_no == []:
            matching_specific_no = ["No"]

        print('HERE 4')

        background_specific = background_specific_atmospheric + background_specific_colors + background_specific_dimensions
        fur_specific = fur_specific_standard + fur_specific_animal + fur_specific_designer + fur_specific_the_risen + fur_specific_the_elders + fur_specific_the_demi_buff + fur_specific_white_angel + fur_specific_devilish
        swag_specific = swag_specific_standard + swag_specific_middle_class_fancy + swag_specific_premium_swag + swag_specific_baby_buff + swag_specific_premium_ink + swag_specific_premium_weapons + swag_specific_bane_veins + swag_specific_symbol
        horns_specific = horns_specific_standard + horns_specific_standard_plus + horns_specific_variant + horns_specific_baby_buff + horns_specific_animal_horns + horns_specific_halo + horns_specific_the_messiah
        eyes_specific = eyes_specific_standard + eyes_specific_eyewear + eyes_specific_impressionable + eyes_specific_battle_ridden + eyes_specific_beams + eyes_specific_betrayer
        mouth_specific = mouth_specific_standard + mouth_specific_kewl + mouth_specific_cool_guy + mouth_specific_bull_rings + mouth_specific_heated + mouth_specific_prehistoric
        smoking_specific = smoking_specific_yes + smoking_specific_no
        double_baby_specific = double_baby_specific_swag + double_baby_specific_horns + double_baby_specific_no
        collection_specific = collections_specific_yes + collections_specific_no
        matching_specific = matching_specific_yes + matching_specific_no

        print('HERE 5')

        if background_specific:
            queryList = filter(lambda x: x.uniqueId <= 9910 and x.traits.background_specific in background_specific, queryList)

        if fur_specific:
            queryList = filter(lambda x: x.uniqueId <= 9910 and x.traits.fur_specific in fur_specific, queryList)

        if swag_specific:
            queryList = filter(lambda x: x.uniqueId <= 9910 and x.traits.swag_specific in swag_specific, queryList)

        if horns_specific:
            queryList = filter(lambda x: x.uniqueId <= 9910 and x.traits.horns_specific in horns_specific, queryList)

        if eyes_specific:
            queryList = filter(lambda x: x.uniqueId <= 9910 and x.traits.eyes_specific in eyes_specific, queryList)

        if mouth_specific:
            queryList = filter(lambda x: x.uniqueId <= 9910 and x.traits.mouth_specific in mouth_specific, queryList)

        if smoking:
            queryList = filter(lambda x: x.uniqueId <= 9910 and x.traits.mouth_specific in smoking_specific, queryList)

        if double_baby_specific_swag:
            queryList = filter(lambda x: x.uniqueId <= 9910 and x.traits.swag_specific in double_baby_specific_swag and x.traits.double_baby_buff == "Yes", queryList)
        if double_baby_specific_horns:
            queryList = filter(lambda x: x.uniqueId <= 9910 and x.traits.horns_specific in double_baby_specific_horns and x.traits.double_baby_buff == "Yes", queryList)
        if double_baby_specific_no:
            queryList = filter(lambda x: x.uniqueId <= 9910 and x.traits.double_baby_buff == "No", queryList)

        if collection_specific:
            print('try here')
            print(collection_specific)
            queryList = filter(lambda x: x.uniqueId <= 9910 and any(item in x.traits.collections_name for item in collection_specific), queryList)

        if matching_specific:
            queryList = filter(lambda x: x.uniqueId <= 9910 and any(item in x.traits.matching_color for item in matching_specific), queryList)

        print('HERE 6')

        # sort it if applied on based on price/points
        queryList=list(queryList)
        from datetime import datetime

        if sort_by == "uniqueId_ascending":
            queryList.sort(key=lambda x: x.uniqueId)
        elif sort_by == "uniqueId_descending":
            queryList.sort(key=lambda x: x.uniqueId, reverse=True)
        elif sort_by == "forSale_ascending":
            queryList = list(filter(lambda x: x.forSale != "No", queryList))
            queryList.sort(key=lambda x: float(x.forSale))
        elif sort_by == "forSale_descending":
            queryList = list(filter(lambda x: x.forSale != "No", queryList))
            queryList.sort(key=lambda x: float(x.forSale), reverse=True)
        elif sort_by == "buffScore_ascending":
            queryList = list(filter(lambda x: x.uniqueId <= 9910, queryList))
            queryList.sort(key=lambda x: x.traits.total_buff_score)
        elif sort_by == "buffScore_descending":
            queryList = list(filter(lambda x: x.uniqueId <= 9910, queryList))
            queryList.sort(key=lambda x: x.traits.total_buff_score, reverse=True)
        elif sort_by == "date_listed_ascending":
            queryList = list(filter(lambda x: x.forSale != "No", queryList))
            queryList.sort(key=lambda x: x.date_listed, reverse=True)
            print('ascending list')
            print(queryList)
        elif sort_by == "date_listed_descending":
            queryList = list(filter(lambda x: x.forSale != "No", queryList))
            queryList.sort(key=lambda x: x.date_listed)


        print('HERE b')
        buffs_size = len(queryList)
        print(buffs_size)
        max_size = True if upper >= buffs_size else False
        if max_size:
            print('was max size')
            upper = buffs_size
        #print(queryList)
        print('wut')
        #print(queryList[0:5])
        print('lower')
        print(lower)
        print('upper')
        print(upper)
        queryList=list(queryList[lower:upper])
        data = self.plain_serializer_class.serialize_data(queryList)
        print('here is total genesis items')
        print(10000)
        genesis_items = (format (10000, ',d'))
        print('here is total genesis reserved')
        print(len(queryList1))
        genesis_reserved = (format (len(queryList1), ',d'))
        print('here is trade floor')


        print('here is items')

        trade_stats = TradeStats.objects.all()
        print(trade_stats[0])
        volume = format_floats(trade_stats[0].manual_volume + trade_stats[0].automated_volume)
        num_trades = (format (trade_stats[0].manual_number_trades + trade_stats[0].automated_number_trades, ',d'))
        highest_trade = format_floats(trade_stats[0].highest_trade)


        #print(type(data))
        #print('HERE 7')
        #print(data)
        #queryList = {'results': queryList, 'total_count': total_count}
        #results = {'data':queryList, 'total_data':total_count}

        return JsonResponse({'data': data, 'max': max_size, 'total_count': buffs_size, 'genesis_items': genesis_items, 'genesis_reserved': genesis_reserved, 'floor': floor, 'volume': volume, 'num_trades': num_trades, 'highest_trade': highest_trade, 'num_owners': num_owners}, safe=False)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     queryset["results"] = queryset["results"][0:120]
    #     data = self.plain_serializer_class.serialize_data(queryset)
    #     return Response(data)

def load_more(request):
    print('list more rang')
    queryset = BuffListing.get_queryset
    offset = BuffListing.get_start
    print(offset)
    limit = BuffListing.buff_per_page_limit
    queryset["results"] = queryset["results"][offset:offset+limit]
    #data = self.plain_serializer_class.serialize_data(queryset)
    return Response(data)


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
    redeemed = 75000 - left
    print('l')
    print(left)
    print(redeemed)
    redeemed = round(redeemed / 750, 2)
    print('here wild redeemed')
    print(redeemed)
    context['redeemed'] = redeemed

    buff = 0
    buff_riders = 0
    gamer_buff = 0
    darkness_gamer_buff = 0
    buff_soldier_gamer_buff = 0
    storm_born_gamer_buff = 0
    unholy_gamer_buff = 0
    art_buff = 0
    buff_maiden = 0
    buff_racer = 0
    clown_buff = 0
    cow_buff = 0
    dino_buff = 0
    dracula_buff = 0
    fire_god_buff = 0
    judge_buff = 0
    legionnaire_buff = 0
    lightsuit_buff = 0
    military_buff = 0
    radish_buff = 0
    robinhood_buff = 0
    roman_buff = 0
    rumble_man_buff = 0
    sinatra_buff = 0
    skull_fighter_buff = 0
    thanos_buff = 0
    thunder_god_buff = 0
    tiki_warrior_buff = 0
    trade_maiden_buff = 0
    voorhees_buff = 0
    war_maiden_buff = 0
    tiki_warrior_buff = 0
    one_million_cc = 0
    five_hundred_thousand_cc = 0
    thirty_thousand_cc = 0
    fifteen_thousand_cc = 0
    six_thousand_cc = 0
    three_thousand_cc = 0
    one_thousand_five_hundred_cc = 0
    seven_hundred_fifty_cc = 0
    five_hundred_cc = 0
    one_cc = 0
    ten_thousand_rds = 0
    five_thousand_rds = 0
    two_thousand_five_hundred_rds = 0
    one_thousand_rds = 0
    five_hundred_rds = 0
    two_hundred_fifty_rds = 0
    one_hundred_rds = 0
    one_hundred_fifty_xrd = 0
    one_hundred_xrd = 0
    sixty_xrd = 0
    thirty_xrd = 0
    fifteen_xrd = 0
    ten_fifty_xrd = 0
    three_xrd = 0
    print('hi')
    available_wild = read_pickle_file(production_wild_path)
    #print(available_wild)

    for wild in available_wild:
        if wild <= 15:
            buff += 1
        elif wild <= 27:
            buff_riders += 1
        elif wild <= 31:
            gamer_buff += 1
        elif wild <= 35:
            darkness_gamer_buff += 1
        elif wild <= 39:
            buff_soldier_gamer_buff += 1
        elif wild <= 43:
            storm_born_gamer_buff += 1
        elif wild <= 47:
            unholy_gamer_buff += 1
        elif wild <= 52:
            art_buff += 1
        elif wild <= 57:
            buff_maiden += 1
        elif wild <= 64:
            buff_racer += 1
        elif wild <= 65:
            clown_buff += 1
        elif wild <= 71:
            cow_buff += 1
        elif wild <= 75:
            dino_buff += 1
        elif wild <= 78:
            dracula_buff += 1
        elif wild <= 83:
            fire_god_buff += 1
        elif wild <= 84:
            judge_buff += 1
        elif wild <= 87:
            legionnaire_buff += 1
        elif wild <= 94:
            lightsuit_buff += 1
        elif wild <= 98:
            military_buff += 1
        elif wild <= 99:
            radish_buff += 1
        elif wild <= 104:
            robinhood_buff += 1
        elif wild <= 107:
            roman_buff += 1
        elif wild <= 112:
            rumble_man_buff += 1
        elif wild <= 113:
            sinatra_buff += 1
        elif wild <= 122:
            skull_fighter_buff += 1
        elif wild <= 123:
            thanos_buff += 1
        elif wild <= 128:
            thunder_god_buff += 1
        elif wild <= 137:
            tiki_warrior_buff += 1
        elif wild <= 142:
            trade_maiden_buff += 1
        elif wild <= 143:
            voorhees_buff += 1
        elif wild <= 151:
            war_maiden_buff += 1
        elif wild <= 155:
            wizard_buff += 1
        elif wild <= 165:
            one_million_cc += 1
        elif wild <= 190:
            five_hundred_thousand_cc += 1
        elif wild <= 225:
            thirty_thousand_cc += 1
        elif wild <= 300:
            fifteen_thousand_cc += 1
        elif wild <= 400:
            six_thousand_cc += 1
        elif wild <= 550:
            three_thousand_cc += 1
        elif wild <= 800:
            one_thousand_five_hundred_cc += 1
        elif wild <= 815:
            seven_hundred_fifty_cc += 1
        elif wild <= 845:
            five_hundred_cc += 1
        elif wild <= 1345:
            one_cc += 1
        elif wild <= 2345:
            ten_thousand_rds += 1
        elif wild <= 4845:
            five_thousand_rds += 1
        elif wild <= 9845:
            two_thousand_five_hundred_rds += 1
        elif wild <= 19845:
            one_thousand_rds += 1
        elif wild <= 42095:
            five_hundred_rds += 1
        elif wild <= 67595:
            two_hundred_fifty_rds += 1
        elif wild <= 71000:
            one_hundred_rds += 1
        elif wild <= 71020:
            one_hundred_fifty_xrd += 1
        elif wild <= 71050:
            one_hundred_xrd += 1
        elif wild <= 71100:
            sixty_xrd += 1
        elif wild <= 71200:
            thirty_xrd += 1
        elif wild <= 71400:
            fifteen_xrd += 1
        elif wild <= 72000:
            ten_fifty_xrd += 1
        else:
            three_xrd += 1

    context['buff']= buff
    context['buff_riders']= buff_riders
    context['gamer_buff']= gamer_buff
    context['darkness_gamer_buff']= darkness_gamer_buff
    context['buff_soldier_gamer_buff']= buff_soldier_gamer_buff
    context['storm_born_gamer_buff']= storm_born_gamer_buff
    context['unholy_gamer_buff']= unholy_gamer_buff
    context['art_buff']= art_buff
    context['buff_maiden']= buff_maiden
    context['buff_racer']= buff_racer
    context['clown_buff']= clown_buff
    context['cow_buff']= cow_buff
    context['dino_buff']= dino_buff
    context['dracula_buff']= dracula_buff
    context['fire_god_buff']= fire_god_buff
    context['judge_buff']= judge_buff
    context['legionnaire_buff']= legionnaire_buff
    context['lightsuit_buff']= lightsuit_buff
    context['military_buff']= military_buff
    context['radish_buff']= radish_buff
    context['robinhood_buff']= robinhood_buff
    context['roman_buff']= roman_buff
    context['rumble_man_buff']= rumble_man_buff
    context['sinatra_buff']= sinatra_buff
    context['skull_fighter_buff']= skull_fighter_buff
    context['thanos_buff']= thanos_buff
    context['thunder_god_buff']= thunder_god_buff
    context['tiki_warrior_buff']= tiki_warrior_buff
    context['trade_maiden_buff']= trade_maiden_buff
    context['voorhees_buff']= voorhees_buff
    context['war_maiden_buff']= war_maiden_buff
    context['wizard_buff']= wizard_buff
    context['one_million_cc']= one_million_cc
    context['five_hundred_thousand_cc']= five_hundred_thousand_cc
    context['thirty_thousand_cc']= thirty_thousand_cc
    context['fifteen_thousand_cc']= fifteen_thousand_cc
    context['six_thousand_cc']= six_thousand_cc
    context['three_thousand_cc']= three_thousand_cc
    context['one_thousand_five_hundred_cc']= one_thousand_five_hundred_cc
    context['seven_hundred_fifty_cc']= seven_hundred_fifty_cc
    context['five_hundred_cc']= five_hundred_cc
    context['one_cc']= one_cc
    context['ten_thousand_rds']= ten_thousand_rds
    context['five_thousand_rds']= five_thousand_rds
    context['two_thousand_five_hundred_rds']= two_thousand_five_hundred_rds
    context['one_thousand_rds']= one_thousand_rds
    context['five_hundred_rds']= five_hundred_rds
    context['two_hundred_fifty_rds']= two_hundred_fifty_rds
    context['one_hundred_rds']= one_hundred_rds
    context['one_hundred_fifty_xrd']= one_hundred_fifty_xrd
    context['one_hundred_xrd']= one_hundred_xrd
    context['sixty_xrd']= sixty_xrd
    context['thirty_xrd']= thirty_xrd
    context['fifteen_xrd']= fifteen_xrd
    context['ten_fifty_xrd']= ten_fifty_xrd
    context['three_xrd']= three_xrd

    return render(request, 'main/instructions.html', context)

def terms(request):
    return render(request, 'main/terms.html')

def test(request):
    return render(request, 'main/test.html')

def test4(request):
    return render(request, 'main/test4.html')

def error_404_view(request, exception):
    return render(request, 'main/404.html')

def error_500_view(request):
    return render(request, 'main/500.html')



# def getMatching(request):
#     print('get matching')
#     if request.method == "GET" and is_ajax(request):
#         # get all the varities from the database excluding
#         # null and blank values
#
#         matching = Image.objects.exclude(traits__matching="No").exclude(traits__matching_color__isnull=True).\
#         	exclude(traits__matching__exact='').exclude(traits__matching_color__icontains=',').\
#             order_by('traits__matching_color').values_list('traits__matching_color').distinct()
#         matching = [i[0] for i in list(matching)]
#         data = {
#             "matching": matching,
#         }
#         return JsonResponse(data, status = 200)
#
# def getCollections(request):
#     print('get collections')
#     if request.method == "GET" and is_ajax(request):
#         # get all the varities from the database excluding
#         # null and blank values
#
#         collections = Image.objects.exclude(traits__collections="No").exclude(traits__collections__isnull=True).\
#         	exclude(traits__collections='').exclude(traits__collections_name__icontains=',').\
#             order_by('traits__collections_name').values_list('traits__collections_name').distinct()
#         collections = [i[0] for i in list(collections)]
#         data = {
#             "collections": collections,
#         }
#         return JsonResponse(data, status = 200)
#
# def chest(request):
#     images = ImageTwo.objects.all()
#     images= sorted(images, key= lambda image:int(image.uniqueId))
#
#     context = {}
#
#     context['images'] = images
#     return render(request, 'main/chest.html', context)
#
#
# def trading(request):
#     print('a')
#     images = Image.objects.filter(~Q(forSale='No'))
#     print(type(images))
#     for i in images:
#         print(i)
#         print(type(i))
#         break
#     print('b')
#     images = sorted(images, key= lambda image:int(image.uniqueId))
#     print(type(images))
#     for i in images:
#         print(i)
#         print(type(i))
#         break
#     images2 = ImageTwo.objects.filter(~Q(forSale='No'))
#     images2 = sorted(images2, key= lambda image:int(image.uniqueId))
#     images = images + images2
#     images = sorted(images, key= lambda image:int(image.uniqueId))
#     traits = Trait.objects.all()
#     context = {}
#
#     context['images'] = images
#
#     return render(request, 'main/trading.html', context)
#
# def buffmassivedongs(request):
#     return render(request, 'main/buffmassivedongs.html', {})
#
# def collection(request):
#     images = Image.objects.all()
#     images= sorted(images, key= lambda image:int(image.uniqueId))
#
#     if request.GET.get('unlocked'):
#         print('here 1')
#         images = Image.objects.filter(~Q(ownerWallet='Locked'))
#         images= sorted(images, key=lambda image:int(image.uniqueId))
#
#     if request.GET.get('1of1'):
#         print('here 2')
#         images = Image.objects.filter(uniqueId__gte=9910)
#         images= sorted(images, key=lambda image:int(image.uniqueId))
#
#     if request.GET.get('1of1') and request.GET.get('unlocked'):
#         print('here 3')
#         images = Image.objects.filter(~Q(ownerWallet='Locked'), uniqueId__gte=9910)
#         images= sorted(images, key=lambda image:int(image.uniqueId))
#
#     page = request.GET.get('page', 1)
#     paginator = Paginator(images, 200)
#
#     try:
#         images = paginator.page(page)
#     except PageNotAnInteger:
#         images = paginator.page(1)
#     except EmptyPage:
#         images = paginator.page(paginator.num_pages)
#
#
#     context = {}
#
#     context['images'] = images
#     return render(request, 'main/collection.html', context)
#
# def walletLookup(request):
#     images=None
#     if request.GET.get('searchWal'):
#         search = request.GET.get('searchWal')
#         images = Image.objects.filter(ownerWallet=search)
#         images= sorted(images, key=lambda image:int(image.uniqueId))
#         images2 = ImageTwo.objects.filter(ownerWallet=search)
#         images2= sorted(images2, key=lambda image:int(image.uniqueId))
#         images = images + images2
#     try:
#         if request.GET.get('searchNum'):
#             search = request.GET.get('searchNum')
#             if int(search) > 10000:
#                 images = ImageTwo.objects.filter(uniqueId=search.lstrip('0'))
#                 images= sorted(images, key= lambda image:int(image.uniqueId))
#             else:
#                 images = Image.objects.filter(uniqueId=search.lstrip('0'))
#                 images= sorted(images, key= lambda image:int(image.uniqueId))
#
#     except ValueError: ## This prevents someone who searches for anything but a number from breaking the page
#             print("Invalid Search. Numbers only")
#
#
#     return render(request, 'main/walletLookup.html',{
#         'images': images,
#     })
