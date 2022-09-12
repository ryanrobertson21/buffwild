from django.urls import path
from . views import *

urlpatterns = [
    path('', trading),
    path("buff_listing/", BuffListing.as_view(), name = 'listing'),
    path("ajax/background/", getBackground, name = 'get_background'),
    path("ajax/fur/", getFur, name = 'get_fur'),
    path("ajax/swag/", getSwag, name = 'get_swag'),
    path("ajax/horns/", getHorns, name = 'get_horns'),
    path("ajax/eyes/", getEyes, name = 'get_eyes'),
    path("ajax/mouth/", getMouth, name = 'get_mouth'),
    path("ajax/title/", getTitle, name = 'get_title'),
    path("ajax/ownerWallet/", getownerWallet, name = 'get_ownerWallet'),
]
