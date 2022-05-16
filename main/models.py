from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
import shortuuid
from django.urls import reverse


class Image(models.Model):
    id=models.IntegerField(null=False, blank=True, primary_key=True)
    title=models.CharField(null=True, blank=True, max_length=200)
    ownerWallet=models.CharField(default='Locked', max_length=200)
    #price=
    #buyCode=
    #sellCode=
    #cancelCode
    #For sale? or should include this in price? initially it has a price, then after first sale that price is set to
    #not for sale. then if they want to sell and it and perform the necessary transaction then update the price.
    # all codes should be the same except buy code prefaced with a B, sell code with an S, and cancel with an X

    #Utility Variables
    uniqueId=models.CharField(null=True, blank=True, max_length=100)
    tradeId=models.CharField(null=True, blank=True, max_length=100)
    slug=models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created=models.DateTimeField(blank=True, null=True)
    last_updated=models.DateTimeField(blank=True, null=True)

    img_photo=models.ImageField(upload_to='unlocked_buffs/', null=True, blank=True)
    img_url=models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return '{}'.format(self.uniqueId)


    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{}'.format(self.uniqueId))
        if self.tradeId is None:
            self.tradeId = shortuuid.random(length=6)


        self.slug = slugify('{}'.format(self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        x = str(self.img_photo).replace(' ', '%20')
        self.img_url = "https://buffwild.b-cdn.net/Buff Wild Collection - Metadata/images/" + x
        super(Image, self).save(*args, **kwargs)
