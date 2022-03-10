from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse


class Image(models.Model):
    title=models.CharField(null=True, blank=True, max_length=200)
    ownerWallet=models.CharField(default='Locked', max_length=200)

    #Utility Variables
    uniqueId=models.CharField(null=True, blank=True, max_length=100)
    slug=models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created=models.DateTimeField(blank=True, null=True)
    last_updated=models.DateTimeField(blank=True, null=True)

    img_photo=models.ImageField(upload_to='unlocked_buffs/', null=True, blank=True)

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


        self.slug = slugify('{}'.format(self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Image, self).save(*args, **kwargs)
