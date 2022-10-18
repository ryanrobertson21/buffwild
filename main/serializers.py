from rest_framework import serializers
from .models import Image, ImageTwo, Trait
import json

class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = ['total_buff_score',
        'background_feature', 'background_feature_rarity', 'background_specific', 'background_buff_score',
        'fur_feature', 'fur_feature_rarity', 'fur_specific', 'fur_buff_score',
        'swag_feature', 'swag_feature_rarity', 'swag_specific', 'swag_buff_score',
        'horns_feature', 'horns_feature_rarity', 'horns_specific', 'horns_buff_score',
        'eyes_feature', 'eyes_feature_rarity', 'eyes_specific', 'eyes_buff_score',
        'mouth_feature', 'mouth_feature_rarity', 'mouth_specific', 'mouth_buff_score',
        'smoking', 'smoking_rarity', 'smoking_buff_score',
        'double_baby_buff', 'double_baby_buff_rarity', 'double_baby_buff_buff_score',
        'matching', 'matching_color', 'matching_rarity', 'matching_buff_score', "matching_dictionary",
        'collections', 'collections_name', 'collections_rarity', 'collections_buff_score', "collections_dictionary"
]

class BuffSerializer(serializers.ModelSerializer):
    traits = TraitSerializer(read_only=True)

    class Meta:
	    model = Image
	    fields = ('title', 'ownerWallet', 'forSale', 'uniqueId', 'tradeId', 'date_created',
	    		'last_updated', 'img_photo', 'img_url', 'traits', 'date_listed')


class BuffSerializerTwo(serializers.ModelSerializer):
    class Meta:
	    model = ImageTwo
	    fields = ('title', 'ownerWallet', 'forSale', 'uniqueId', 'tradeId', 'date_created',
	    		'last_updated', 'img_photo', 'img_url', 'date_listed')

class SummarySerializer(serializers.Serializer):

    @classmethod
    def get_serializer(cls, model):
        if model == Image:
            return BuffSerializer
        elif model == ImageTwo:
            return BuffSerializerTwo

    def to_representation(self, instance):
        serializer = self.get_serializer(instance.__class__)
        return serializer(instance, context=self.context).data

class BuffPlainSerializer(object):


    @staticmethod
    def serialize_data(queryset):
        l = []
        d = {}
        print('we are in serializer')
        for entry in queryset:
            if type(entry) == Image and entry.uniqueId <= 9910:

                d[entry.uniqueId] ={
                        "title": entry.title,
                        "forSale": entry.forSale,
                        "uniqueId": entry.uniqueId,
                        "tradeId": entry.tradeId,
                        "ownerWallet": entry.ownerWallet,
                        "img_url": entry.img_url,
                        "date_listed": entry.date_listed,
                        "traits": {"total_buff_score": entry.traits.total_buff_score,
                            "background_feature": entry.traits.background_feature, "background_feature_rarity": entry.traits.background_feature_rarity, "background_specific": entry.traits.background_specific, "background_buff_score": entry.traits.background_buff_score,
                            "fur_feature": entry.traits.fur_feature, "fur_feature_rarity": entry.traits.fur_feature_rarity, "fur_specific": entry.traits.fur_specific, "fur_buff_score": entry.traits.fur_buff_score,
                            "swag_feature": entry.traits.swag_feature, "swag_feature_rarity": entry.traits.swag_feature_rarity, "swag_specific": entry.traits.swag_specific, "swag_buff_score": entry.traits.swag_buff_score,
                            "horns_feature": entry.traits.horns_feature, "horns_feature_rarity": entry.traits.horns_feature_rarity, "horns_specific": entry.traits.horns_specific, "horns_buff_score": entry.traits.horns_buff_score,
                            "eyes_feature": entry.traits.eyes_feature, "eyes_feature_rarity": entry.traits.eyes_feature_rarity, "eyes_specific": entry.traits.eyes_specific, "eyes_buff_score": entry.traits.eyes_buff_score,
                            "mouth_feature": entry.traits.mouth_feature, "mouth_feature_rarity": entry.traits.mouth_feature_rarity, "mouth_specific": entry.traits.mouth_specific, "mouth_buff_score": entry.traits.mouth_buff_score,
                            "smoking": entry.traits.smoking, "smoking_rarity": entry.traits.smoking_rarity, "smoking_buff_score": entry.traits.smoking_buff_score,
                            "double_baby_buff": entry.traits.double_baby_buff, "double_baby_buff_rarity": entry.traits.double_baby_buff_rarity, "double_baby_buff_buff_score": entry.traits.double_baby_buff_buff_score,
                            "matching": entry.traits.matching, "matching_color": entry.traits.matching_color, "matching_rarity": entry.traits.matching_rarity, "matching_buff_score": entry.traits.matching_buff_score, "matching_dictionary": entry.traits.matching_dictionary,
                            "collections": entry.traits.collections, "collections_name": entry.traits.collections_name, "collections_rarity": entry.traits.collections_rarity, "collections_buff_score": entry.traits.collections_buff_score, "collections_dictionary": entry.traits.collections_dictionary}
                    }
            else:

                d[entry.uniqueId] = {
                        "title": entry.title,
                        "forSale": entry.forSale,
                        "uniqueId": entry.uniqueId,
                        "tradeId": entry.tradeId,
                        "ownerWallet": entry.ownerWallet,
                        "img_url": entry.img_url,
                        "date_listed": entry.date_listed
                    }

        #d["total_count"] = queryset["total_count"]
        return d
