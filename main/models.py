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
    uniqueId=models.IntegerField(primary_key=True)
    tradeId=models.CharField(null=True, blank=True, max_length=100)
    date_created=models.DateTimeField(blank=True, null=True)
    last_updated=models.DateTimeField(blank=True, null=True)

    img_photo=models.ImageField(upload_to='unlocked_buffs/', null=True, blank=True)
    img_url=models.CharField(null=True, blank=True, max_length=100)
    date_listed=models.DateTimeField(blank=True, null=True)

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
    id=models.IntegerField(blank=True, null=True)
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
    uniqueId=models.IntegerField(blank=True, primary_key=True)
    tradeId=models.CharField(null=True, blank=True, max_length=100)
    date_created=models.DateTimeField(blank=True, null=True)
    last_updated=models.DateTimeField(blank=True, null=True)

    img_photo=models.ImageField(upload_to='unlocked_buffs/', null=True, blank=True)
    img_url=models.CharField(null=True, blank=True, max_length=100)
    date_listed=models.DateTimeField(blank=True, null=True)

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
        to_field='uniqueId',
        related_name="traits",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    total_buff_score=models.IntegerField(null=True, blank=True)

    background_feature=models.CharField(null=True, blank=True, max_length=200)
    background_feature_rarity=models.CharField(null=True, blank=True, max_length=200)
    background_specific=models.CharField(null=True, blank=True, max_length=200)
    background_buff_score=models.IntegerField(null=True, blank=True)

    fur_feature=models.CharField(null=True, blank=True, max_length=200)
    fur_feature_rarity=models.CharField(null=True, blank=True, max_length=200)
    fur_specific=models.CharField(null=True, blank=True, max_length=200)
    fur_buff_score=models.IntegerField(null=True, blank=True)

    swag_feature=models.CharField(null=True, blank=True, max_length=200)
    swag_feature_rarity=models.CharField(null=True, blank=True, max_length=200)
    swag_specific=models.CharField(null=True, blank=True, max_length=200)
    swag_buff_score=models.IntegerField(null=True, blank=True)

    horns_feature=models.CharField(null=True, blank=True, max_length=200)
    horns_feature_rarity=models.CharField(null=True, blank=True, max_length=200)
    horns_specific=models.CharField(null=True, blank=True, max_length=200)
    horns_buff_score=models.IntegerField(null=True, blank=True)

    eyes_feature=models.CharField(null=True, blank=True, max_length=200)
    eyes_feature_rarity=models.CharField(null=True, blank=True, max_length=200)
    eyes_specific=models.CharField(null=True, blank=True, max_length=200)
    eyes_buff_score=models.IntegerField(null=True, blank=True)

    mouth_feature=models.CharField(null=True, blank=True, max_length=200)
    mouth_feature_rarity=models.CharField(null=True, blank=True, max_length=200)
    mouth_specific=models.CharField(null=True, blank=True, max_length=200)
    mouth_buff_score=models.IntegerField(null=True, blank=True)

    smoking=models.CharField(null=True, blank=True, max_length=200)
    smoking_rarity=models.CharField(null=True, blank=True, max_length=200)
    smoking_buff_score=models.IntegerField(null=True, blank=True)

    double_baby_buff=models.CharField(null=True, blank=True, max_length=200)
    double_baby_buff_rarity=models.CharField(null=True, blank=True, max_length=200)
    double_baby_buff_buff_score=models.IntegerField(null=True, blank=True)

    cyborg=models.CharField(null=True, blank=True, max_length=200)
    cyborg_rarity=models.CharField(null=True, blank=True, max_length=200)
    cyborg_buff_score=models.IntegerField(null=True, blank=True)

    cowboy=models.CharField(null=True, blank=True, max_length=200)
    cowboy_rarity=models.CharField(null=True, blank=True, max_length=200)
    cowboy_buff_score=models.IntegerField(null=True, blank=True)

    dbz=models.CharField(null=True, blank=True, max_length=200)
    dbz_rarity=models.CharField(null=True, blank=True, max_length=200)
    dbz_buff_score=models.IntegerField(null=True, blank=True)

    matrix=models.CharField(null=True, blank=True, max_length=200)
    matrix_rarity=models.CharField(null=True, blank=True, max_length=200)
    matrix_buff_score=models.IntegerField(null=True, blank=True)

    nono=models.CharField(null=True, blank=True, max_length=200)
    nono_rarity=models.CharField(null=True, blank=True, max_length=200)
    nono_buff_score=models.IntegerField(null=True, blank=True)

    undead=models.CharField(null=True, blank=True, max_length=200)
    undead_rarity=models.CharField(null=True, blank=True, max_length=200)
    undead_buff_score=models.IntegerField(null=True, blank=True)

    albino=models.CharField(null=True, blank=True, max_length=200)
    albino_rarity=models.CharField(null=True, blank=True, max_length=200)
    albino_buff_score=models.IntegerField(null=True, blank=True)

    rice_farmer=models.CharField(null=True, blank=True, max_length=200)
    rice_farmer_rarity=models.CharField(null=True, blank=True, max_length=200)
    rice_farmer_buff_score=models.IntegerField(null=True, blank=True)

    super_hero=models.CharField(null=True, blank=True, max_length=200)
    super_hero_rarity=models.CharField(null=True, blank=True, max_length=200)
    super_hero_buff_score=models.IntegerField(null=True, blank=True)

    trippy=models.CharField(null=True, blank=True, max_length=200)
    trippy_rarity=models.CharField(null=True, blank=True, max_length=200)
    trippy_buff_score=models.IntegerField(null=True, blank=True)

    gentleman=models.CharField(null=True, blank=True, max_length=200)
    gentleman_rarity=models.CharField(null=True, blank=True, max_length=200)
    gentleman_buff_score=models.IntegerField(null=True, blank=True)

    joseph_smith=models.CharField(null=True, blank=True, max_length=200)
    joseph_smith_rarity=models.CharField(null=True, blank=True, max_length=200)
    joseph_smith_buff_score=models.IntegerField(null=True, blank=True)

    day_walker=models.CharField(null=True, blank=True, max_length=200)
    day_walker_rarity=models.CharField(null=True, blank=True, max_length=200)
    day_walker_buff_score=models.IntegerField(null=True, blank=True)

    jordan=models.CharField(null=True, blank=True, max_length=200)
    jordan_rarity=models.CharField(null=True, blank=True, max_length=200)
    jordan_buff_score=models.IntegerField(null=True, blank=True)

    hells_kitchen=models.CharField(null=True, blank=True, max_length=200)
    hells_kitchen_rarity=models.CharField(null=True, blank=True, max_length=200)
    hells_kitchen_buff_score=models.IntegerField(null=True, blank=True)

    golded=models.CharField(null=True, blank=True, max_length=200)
    golded_rarity=models.CharField(null=True, blank=True, max_length=200)
    golded_buff_score=models.IntegerField(null=True, blank=True)

    girl=models.CharField(null=True, blank=True, max_length=200)
    girl_rarity=models.CharField(null=True, blank=True, max_length=200)
    girl_buff_score=models.IntegerField(null=True, blank=True)

    rasta=models.CharField(null=True, blank=True, max_length=200)
    rasta_rarity=models.CharField(null=True, blank=True, max_length=200)
    rasta_buff_score=models.IntegerField(null=True, blank=True)

    radix=models.CharField(null=True, blank=True, max_length=200)
    radix_rarity=models.CharField(null=True, blank=True, max_length=200)
    radix_buff_score=models.IntegerField(null=True, blank=True)

    bloody=models.CharField(null=True, blank=True, max_length=200)
    bloody_rarity=models.CharField(null=True, blank=True, max_length=200)
    bloody_buff_score=models.IntegerField(null=True, blank=True)

    bamf=models.CharField(null=True, blank=True, max_length=200)
    bamf_rarity=models.CharField(null=True, blank=True, max_length=200)
    bamf_buff_score=models.IntegerField(null=True, blank=True)

    frat_buff=models.CharField(null=True, blank=True, max_length=200)
    frat_buff_rarity=models.CharField(null=True, blank=True, max_length=200)
    frat_buff_buff_score=models.IntegerField(null=True, blank=True)

    demigod=models.CharField(null=True, blank=True, max_length=200)
    demigod_rarity=models.CharField(null=True, blank=True, max_length=200)
    demigod_buff_score=models.IntegerField(null=True, blank=True)

    regrets=models.CharField(null=True, blank=True, max_length=200)
    regrets_rarity=models.CharField(null=True, blank=True, max_length=200)
    regrets_buff_score=models.IntegerField(null=True, blank=True)

    raver=models.CharField(null=True, blank=True, max_length=200)
    raver_rarity=models.CharField(null=True, blank=True, max_length=200)
    raver_buff_score=models.IntegerField(null=True, blank=True)

    kiddie_pool=models.CharField(null=True, blank=True, max_length=200)
    kiddie_pool_rarity=models.CharField(null=True, blank=True, max_length=200)
    kiddie_pool_buff_score=models.IntegerField(null=True, blank=True)

    mutated=models.CharField(null=True, blank=True, max_length=200)
    mutated_rarity=models.CharField(null=True, blank=True, max_length=200)
    mutated_buff_score=models.IntegerField(null=True, blank=True)

    half_dead=models.CharField(null=True, blank=True, max_length=200)
    half_dead_rarity=models.CharField(null=True, blank=True, max_length=200)
    half_dead_buff_score=models.IntegerField(null=True, blank=True)

    oversized=models.CharField(null=True, blank=True, max_length=200)
    oversized_rarity=models.CharField(null=True, blank=True, max_length=200)
    oversized_buff_score=models.IntegerField(null=True, blank=True)

    easter_celebration=models.CharField(null=True, blank=True, max_length=200)
    easter_celebration_rarity=models.CharField(null=True, blank=True, max_length=200)
    easter_celebration_buff_score=models.IntegerField(null=True, blank=True)

    brads_and_chads=models.CharField(null=True, blank=True, max_length=200)
    brads_and_chads_rarity=models.CharField(null=True, blank=True, max_length=200)
    brads_and_chads_buff_score=models.IntegerField(null=True, blank=True)

    chromed_out=models.CharField(null=True, blank=True, max_length=200)
    chromed_out_rarity=models.CharField(null=True, blank=True, max_length=200)
    chromed_out_buff_score=models.IntegerField(null=True, blank=True)

    natural_evolution=models.CharField(null=True, blank=True, max_length=200)
    natural_evolution_rarity=models.CharField(null=True, blank=True, max_length=200)
    natural_evolution_buff_score=models.IntegerField(null=True, blank=True)

    pride=models.CharField(null=True, blank=True, max_length=200)
    pride_rarity=models.CharField(null=True, blank=True, max_length=200)
    pride_buff_score=models.IntegerField(null=True, blank=True)

    buffs_mafia=models.CharField(null=True, blank=True, max_length=200)
    buffs_mafia_rarity=models.CharField(null=True, blank=True, max_length=200)
    buffs_mafia_buff_score=models.IntegerField(null=True, blank=True)

    agent_zero=models.CharField(null=True, blank=True, max_length=200)
    agent_zero_rarity=models.CharField(null=True, blank=True, max_length=200)
    agent_zero_buff_score=models.IntegerField(null=True, blank=True)

    family_guy=models.CharField(null=True, blank=True, max_length=200)
    family_guy_rarity=models.CharField(null=True, blank=True, max_length=200)
    family_guy_buff_score=models.IntegerField(null=True, blank=True)

    playboy=models.CharField(null=True, blank=True, max_length=200)
    playboy_rarity=models.CharField(null=True, blank=True, max_length=200)
    playboy_buff_score=models.IntegerField(null=True, blank=True)

    battle_hardened=models.CharField(null=True, blank=True, max_length=200)
    battle_hardened_rarity=models.CharField(null=True, blank=True, max_length=200)
    battle_hardened_buff_score=models.IntegerField(null=True, blank=True)

    fire=models.CharField(null=True, blank=True, max_length=200)
    fire_rarity=models.CharField(null=True, blank=True, max_length=200)
    fire_buff_score=models.IntegerField(null=True, blank=True)

    collections=models.CharField(null=True, blank=True, max_length=200)
    collections_name=models.CharField(null=True, blank=True, max_length=200)
    collections_rarity=models.CharField(null=True, blank=True, max_length=200)
    collections_buff_score=models.IntegerField(null=True, blank=True)

    green=models.CharField(null=True, blank=True, max_length=200)
    green_num=models.IntegerField(null=True, blank=True)
    green_rarity=models.CharField(null=True, blank=True, max_length=200)
    green_buff_score=models.IntegerField(null=True, blank=True)

    red=models.CharField(null=True, blank=True, max_length=200)
    red_num=models.IntegerField(null=True, blank=True)
    red_rarity=models.CharField(null=True, blank=True, max_length=200)
    red_buff_score=models.IntegerField(null=True, blank=True)

    purple=models.CharField(null=True, blank=True, max_length=200)
    purple_num=models.IntegerField(null=True, blank=True)
    purple_rarity=models.CharField(null=True, blank=True, max_length=200)
    purple_buff_score=models.IntegerField(null=True, blank=True)

    blue=models.CharField(null=True, blank=True, max_length=200)
    blue_num=models.IntegerField(null=True, blank=True)
    blue_rarity=models.CharField(null=True, blank=True, max_length=200)
    blue_buff_score=models.IntegerField(null=True, blank=True)

    pink=models.CharField(null=True, blank=True, max_length=200)
    pink_num=models.IntegerField(null=True, blank=True)
    pink_rarity=models.CharField(null=True, blank=True, max_length=200)
    pink_buff_score=models.IntegerField(null=True, blank=True)

    yellow=models.CharField(null=True, blank=True, max_length=200)
    yellow_num=models.IntegerField(null=True, blank=True)
    yellow_rarity=models.CharField(null=True, blank=True, max_length=200)
    yellow_buff_score=models.IntegerField(null=True, blank=True)

    brown=models.CharField(null=True, blank=True, max_length=200)
    brown_num=models.IntegerField(null=True, blank=True)
    brown_rarity=models.CharField(null=True, blank=True, max_length=200)
    brown_buff_score=models.IntegerField(null=True, blank=True)

    black=models.CharField(null=True, blank=True, max_length=200)
    black_num=models.IntegerField(null=True, blank=True)
    black_rarity=models.CharField(null=True, blank=True, max_length=200)
    black_buff_score=models.IntegerField(null=True, blank=True)

    orange=models.CharField(null=True, blank=True, max_length=200)
    orange_num=models.IntegerField(null=True, blank=True)
    orange_rarity=models.CharField(null=True, blank=True, max_length=200)
    orange_buff_score=models.IntegerField(null=True, blank=True)

    matching=models.CharField(null=True, blank=True, max_length=200)
    matching_color=models.CharField(null=True, blank=True, max_length=200)
    matching_rarity=models.CharField(null=True, blank=True, max_length=200)
    matching_buff_score=models.IntegerField(null=True, blank=True)

    matching_dictionary=models.CharField(null=True, blank=True, max_length=200)

    collections_dictionary=models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return '{}'.format(self.uniqueId)

    def get_matching_list(self):
        if self.matching_color != "No":
            l = self.matching_color.split(',')
        else:
            l = ""
        return l

    def get_matching_data(self):
        d = {}
        print('models get matching data function')
        for attr, value in self.__dict__.items():
            if attr == "green" or attr == "red" or attr == "purple" or attr == "blue" or attr == "pink" or attr == "yellow" or attr == "brown" or attr == "black" or attr == "orange":
                if value == "Yes":
                    d[attr] = [attr, eval("self." + attr + "_num"), eval("self." + attr + "_rarity"), eval("self." + attr + "_buff_score")]

        return d

    def get_matching_specific(self):
        if self.uniqueId == 2255:
            s = (self.matching_buff_score / 2)
            print('lol')
            print(s)
            r = str(s) + "matches"
        else:
            s = self.matching_buff_score
            r = str(s) + " matches"
        return r

    def get_collection_list(self):
        if self.collections_name != "N/A":
            l = self.collections_name.split(',')
        else:
            l = ""
        return l

    def get_colletion_data(self):
        d = {}
        for attr, value in self.__dict__.items():
            if attr != "smoking" and attr != "double_baby_buff" and attr != "collections" and attr != "matching" and attr != "green" and attr != "red" and attr != "purple" and attr != "blue" and attr != "pink" and attr != "yellow" and attr != "brown" and attr != "black" and attr != "orange":
                if value == "Yes":
                    display_name = attr.replace("_", " ")
                    d[display_name] = ["Yes", display_name, eval("self." + attr + "_rarity"), eval("self." + attr + "_buff_score")]
        return d
