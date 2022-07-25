from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
import shortuuid
from django.urls import reverse


class Image(models.Model):
    title=models.CharField(null=True, blank=True, max_length=200)
    ownerWallet=models.CharField(default='Locked', max_length=200)
    forSale=models.CharField(default='No', max_length=200)
    #price=
    #buyCode=
    #sellCode=
    #cancelCode
    #For sale? or should include this in price? initially it has a price, then after first sale that price is set to
    #not for sale. then if they want to sell and it and perform the necessary transaction then update the price.
    # all codes should be the same except buy code prefaced with a B, sell code with an S, and cancel with an X

    #Utility Variables
    uniqueId=models.IntegerField(null=False, primary_key=True)
    tradeId=models.CharField(null=True, blank=True, max_length=100)
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
        if self.tradeId is None:
            self.tradeId = shortuuid.random(length=6)

        if self.img_url is None:
            x = str(self.img_photo).replace(' ', '%20')
            self.img_url = "https://buffwild.b-cdn.net/Buff%20Wild%20Collection%20-%20Metadata/images/" + x
        super(Image, self).save(*args, **kwargs)



class ImageTwo(models.Model):
    id=models.IntegerField(null=False, blank=True, primary_key=True)
    title=models.CharField(null=True, blank=True, max_length=200)
    ownerWallet=models.CharField(default='Locked', max_length=200)
    forSale=models.CharField(default='No', max_length=200)
    #price=
    #buyCode=
    #sellCode=
    #cancelCode
    #For sale? or should include this in price? initially it has a price, then after first sale that price is set to
    #not for sale. then if they want to sell and it and perform the necessary transaction then update the price.
    # all codes should be the same except buy code prefaced with a B, sell code with an S, and cancel with an X

    #Utility Variables
    uniqueId=models.IntegerField(null=True, blank=True)
    tradeId=models.CharField(null=True, blank=True, max_length=100)
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
            self.uniqueId = 1
        if self.tradeId is None:
            self.tradeId = shortuuid.random(length=6)
        if self.img_url is None:
            x = str(self.img_photo).replace(' ', '%20')
            self.img_url = "https://buffwild.b-cdn.net/Airdrop%201%20of%201s/" + x
        super(ImageTwo, self).save(*args, **kwargs)

class Trait(models.Model):
    uniqueId = models.OneToOneField(
        Image,
        related_name="traits",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    total_buff_score=models.IntegerField(null=True, blank=True)

    background_feature=models.CharField(null=True, blank=True, max_length=200)
    background_feature_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    background_specific=models.CharField(null=True, blank=True, max_length=200)
    background_buff_score=models.IntegerField(null=True, blank=True)

    fur_feature=models.CharField(null=True, blank=True, max_length=200)
    fur_feature_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    fur_specific=models.CharField(null=True, blank=True, max_length=200)
    fur_buff_score=models.IntegerField(null=True, blank=True)

    swag_feature=models.CharField(null=True, blank=True, max_length=200)
    swag_feature_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    swag_specific=models.CharField(null=True, blank=True, max_length=200)
    swag_buff_score=models.IntegerField(null=True, blank=True)

    horns_feature=models.CharField(null=True, blank=True, max_length=200)
    horns_feature_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    horns_specific=models.CharField(null=True, blank=True, max_length=200)
    horns_buff_score=models.IntegerField(null=True, blank=True)

    eyes_feature=models.CharField(null=True, blank=True, max_length=200)
    eyes_feature_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    eyes_specific=models.CharField(null=True, blank=True, max_length=200)
    eyes_buff_score=models.IntegerField(null=True, blank=True)

    mouth_feature=models.CharField(null=True, blank=True, max_length=200)
    mouth_feature_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    mouth_specific=models.CharField(null=True, blank=True, max_length=200)
    mouth_buff_score=models.IntegerField(null=True, blank=True)

    smoking=models.CharField(null=True, blank=True, max_length=200)
    smoking_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    smoking_buff_score=models.IntegerField(null=True, blank=True)

    double_baby_buff=models.CharField(null=True, blank=True, max_length=200)
    double_baby_buff_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    double_baby_buff_buff_score=models.IntegerField(null=True, blank=True)

    cyborg=models.CharField(null=True, blank=True, max_length=200)
    cyborg_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    cyborg_buff_score=models.IntegerField(null=True, blank=True)

    cowboy=models.CharField(null=True, blank=True, max_length=200)
    cowboy_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    cowboy_buff_score=models.IntegerField(null=True, blank=True)

    dbz=models.CharField(null=True, blank=True, max_length=200)
    dbz_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    dbz_buff_score=models.IntegerField(null=True, blank=True)

    matrix=models.CharField(null=True, blank=True, max_length=200)
    matrix_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    matrix_buff_score=models.IntegerField(null=True, blank=True)

    nono=models.CharField(null=True, blank=True, max_length=200)
    nono_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    nono_buff_score=models.IntegerField(null=True, blank=True)

    undead=models.CharField(null=True, blank=True, max_length=200)
    undead_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    undead_buff_score=models.IntegerField(null=True, blank=True)

    albino=models.CharField(null=True, blank=True, max_length=200)
    albino_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    albino_buff_score=models.IntegerField(null=True, blank=True)

    rice_farmer=models.CharField(null=True, blank=True, max_length=200)
    rice_farmer_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    rice_farmer_buff_score=models.IntegerField(null=True, blank=True)

    super_hero=models.CharField(null=True, blank=True, max_length=200)
    super_hero_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    super_hero_buff_score=models.IntegerField(null=True, blank=True)

    trippy=models.CharField(null=True, blank=True, max_length=200)
    trippy_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    trippy_buff_score=models.IntegerField(null=True, blank=True)

    gentleman=models.CharField(null=True, blank=True, max_length=200)
    gentleman_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    gentleman_buff_score=models.IntegerField(null=True, blank=True)

    joseph_smith=models.CharField(null=True, blank=True, max_length=200)
    joseph_smith_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    joseph_smith_buff_score=models.IntegerField(null=True, blank=True)

    day_walker=models.CharField(null=True, blank=True, max_length=200)
    day_walker_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    day_walker_buff_score=models.IntegerField(null=True, blank=True)

    jordan=models.CharField(null=True, blank=True, max_length=200)
    jordan_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    jordan_buff_score=models.IntegerField(null=True, blank=True)

    hells_kitchen=models.CharField(null=True, blank=True, max_length=200)
    hells_kitchen_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    hells_kitchen_buff_score=models.IntegerField(null=True, blank=True)

    golded=models.CharField(null=True, blank=True, max_length=200)
    golded_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    golded_buff_score=models.IntegerField(null=True, blank=True)

    girl=models.CharField(null=True, blank=True, max_length=200)
    girl_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    girl_buff_score=models.IntegerField(null=True, blank=True)

    rasta=models.CharField(null=True, blank=True, max_length=200)
    rasta_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    rasta_buff_score=models.IntegerField(null=True, blank=True)

    radix=models.CharField(null=True, blank=True, max_length=200)
    radix_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    radix_buff_score=models.IntegerField(null=True, blank=True)

    bloody=models.CharField(null=True, blank=True, max_length=200)
    bloody_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    bloody_buff_score=models.IntegerField(null=True, blank=True)

    bamf=models.CharField(null=True, blank=True, max_length=200)
    bamf_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    bamf_buff_score=models.IntegerField(null=True, blank=True)

    frat_buff=models.CharField(null=True, blank=True, max_length=200)
    frat_buff_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    frat_buff_buff_score=models.IntegerField(null=True, blank=True)

    demigod=models.CharField(null=True, blank=True, max_length=200)
    demigod_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    demigod_buff_score=models.IntegerField(null=True, blank=True)

    regrets=models.CharField(null=True, blank=True, max_length=200)
    regrets_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    regrets_buff_score=models.IntegerField(null=True, blank=True)

    raver=models.CharField(null=True, blank=True, max_length=200)
    raver_buff_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    raver_buff_buff_score=models.IntegerField(null=True, blank=True)

    kiddie_pool=models.CharField(null=True, blank=True, max_length=200)
    kiddie_pool_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    kiddie_pool_buff_score=models.IntegerField(null=True, blank=True)

    mutated=models.CharField(null=True, blank=True, max_length=200)
    mutated_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    mutated_buff_score=models.IntegerField(null=True, blank=True)

    half_dead=models.CharField(null=True, blank=True, max_length=200)
    half_dead_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    half_dead_buff_score=models.IntegerField(null=True, blank=True)

    oversized=models.CharField(null=True, blank=True, max_length=200)
    oversized_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    oversized_buff_score=models.IntegerField(null=True, blank=True)

    easter_celebration=models.CharField(null=True, blank=True, max_length=200)
    easter_celebration_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    easter_celebration_buff_score=models.IntegerField(null=True, blank=True)

    brads_and_chads=models.CharField(null=True, blank=True, max_length=200)
    brads_and_chads_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    brads_and_chads_buff_score=models.IntegerField(null=True, blank=True)

    chromed_out=models.CharField(null=True, blank=True, max_length=200)
    chromed_out_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    chromed_out_buff_score=models.IntegerField(null=True, blank=True)

    natural_evolution=models.CharField(null=True, blank=True, max_length=200)
    natural_evolution_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    natural_evolution_buff_score=models.IntegerField(null=True, blank=True)

    pride=models.CharField(null=True, blank=True, max_length=200)
    pride_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    pride_buff_score=models.IntegerField(null=True, blank=True)

    buffs_mafia=models.CharField(null=True, blank=True, max_length=200)
    buffs_mafia_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    buffs_mafia_buff_score=models.IntegerField(null=True, blank=True)

    family_guy=models.CharField(null=True, blank=True, max_length=200)
    family_guy_rarity=models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)
    family_guy_buff_score=models.IntegerField(null=True, blank=True)






    def __str__(self):
        return '{}'.format(self.uniqueId)
