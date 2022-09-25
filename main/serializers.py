from rest_framework import serializers
from .models import Image, ImageTwo, Trait

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
        read_only_fields = fields

class BuffSerializer(serializers.ModelSerializer):
    traits = TraitSerializer(read_only=True)

    class Meta:
        model = Image
        fields = ('title', 'ownerWallet', 'forSale', 'uniqueId', 'tradeId', 'date_created', 'last_updated', 'img_photo', 'img_url', 'traits')
        read_only_fields = fields


class BuffSerializerTwo(serializers.ModelSerializer):
    class Meta:
        model = ImageTwo
        fields = ('title', 'ownerWallet', 'forSale', 'uniqueId', 'tradeId', 'date_created',
	    		'last_updated', 'img_photo', 'img_url')
        read_only_fields = fields

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
