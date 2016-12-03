from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, ModelField, IntegerField
from rest_framework.serializers import ModelSerializer

from core.consts import IMAGE_NOT_EXIST
from core.models import ImageObj
from core.serializers import ImageObjOutSerializer
from .models import Font, Symbol


class SymbolForFontSerializer(ModelSerializer):
    class Meta:
        model = Symbol
        fields = ('value', 'point_one_x', 'point_one_y', 'point_two_x', 'point_two_y')


class FontImageSerializer(ModelSerializer):
    class Meta:
        model = ImageObj


class FontSerializer(ModelSerializer):
    symbols = SymbolForFontSerializer(many=True)
    author_name = SerializerMethodField()
    owner_id = IntegerField(required=False, write_only=True)
    image_id = IntegerField(write_only=True)
    image = ImageObjOutSerializer(required=False)

    def get_author_name(self, instance):
        return instance.author_name or instance.owner.get_full_name()

    def create(self, validated_data):
        owner = validated_data.pop('owner_id')
        symbols_data = validated_data.pop('symbols')
        try:
            image_id = ImageObj.objects.get(pk=validated_data.pop('image_id')).pk
        except ImageObj.DoesNotExist:
            raise ValidationError(IMAGE_NOT_EXIST)

        font = Font.objects.create(owner_id=owner, image_id=image_id, **validated_data)
        for symbol_data in symbols_data:
            Symbol.objects.create(font=font, **symbol_data)
        return font

    class Meta:
        model = Font
        fields = ('content', 'author_name', 'status', 'id', 'symbols', 'owner_id', 'image_id', 'image')
        read_only_fields = ('id', 'author_name', 'image_thumbnail')  #, 'status')
        extra_kwargs = {'owner_id': {'write_only': True}, 'image_id': {'write_only': True}}


class FontCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()
