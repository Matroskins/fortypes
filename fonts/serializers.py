from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, ModelField, IntegerField
from rest_framework.serializers import ModelSerializer, CharField

from core.consts import IMAGE_NOT_EXIST, AUTHOR_NAME_TAKEN
from core.models import ImageObj
from core.serializers import ImageObjOutSerializer
from fonts.models import Author
from user_font_relation.models import UserFontRelation
from .models import Font, Symbol


class SymbolForFontSerializer(ModelSerializer):
    class Meta:
        model = Symbol
        fields = ('value', 'point_one_x', 'point_one_y', 'point_two_x', 'point_two_y')


class FontImageSerializer(ModelSerializer):
    class Meta:
        model = ImageObj


class FontCreateSerializer(serializers.Serializer):
    symbols = SymbolForFontSerializer(many=True, required=True)
    author_name = CharField(required=False)
    owner_id = IntegerField(required=False, write_only=True)
    image_id = IntegerField(write_only=True)
    image = ImageObjOutSerializer(required=False)

    def validate_author_name(self, value):
        if Author.objects.filter(name=value).exclude(user=self.context['request'].user).exists():
            raise ValidationError(AUTHOR_NAME_TAKEN)
        return value

    def create(self, validated_data):
        user = self.context['request'].user

        symbols_data = validated_data.pop('symbols')
        author_name = validated_data.pop('author_name', None)
        try:
            image_id = ImageObj.objects.get(pk=validated_data.pop('image_id')).pk
        except ImageObj.DoesNotExist:
            raise ValidationError(IMAGE_NOT_EXIST)

        if author_name:
            author, created = Author.objects.get_or_create(name=author_name)
        else:
            author, _ = Author.objects.get_or_create(user=user, name=user.get_full_name())

        validated_data['author'] = author
        font = Font.objects.create(owner=user, image_id=image_id, **validated_data)
        for symbol_data in symbols_data:
            Symbol.objects.create(font=font, **symbol_data)
        return font


class FontGetSerializer(ModelSerializer):
    symbols = SymbolForFontSerializer(many=True)
    author_name = serializers.CharField(source='author.name')
    image = ImageObjOutSerializer(required=False)

    class Meta:
        model = Font
        fields = ('content', 'status', 'id', 'symbols', 'owner_id', 'image_id', 'image', 'author_name')


class FontCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class AuthorSerializer(ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    works_count = serializers.SerializerMethodField()

    def get_likes_count(self, instance):
        return UserFontRelation.objects.filter(like=True, font__author=instance).count()

    def get_works_count(self, instance):
        return Font.objects.filter(author=instance).count()

    class Meta:
        model = Author
        fields = ('name', 'likes_count', 'works_count')
