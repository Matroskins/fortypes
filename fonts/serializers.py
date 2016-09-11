from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import Font, Symbol


class SymbolSerializer(ModelSerializer):
    class Meta:
        model = Symbol
        fields = ('font', 'position', 'ul_point', 'ur_point', 'dl_point', 'dr_point')


class FontSerializer(ModelSerializer):
    symbols = SymbolSerializer(many=True, source='symbols')
    author_name = SerializerMethodField()

    def get_author_name(self, instance):
        return instance.author.user.get_full_name()

    def create(self, validated_data):
        symbols_data = validated_data.pop('symbols')
        font = Font.objects.create(**validated_data)
        for symbol_data in symbols_data:
            Symbol.objects.create(font=font, **symbol_data)
        return font

    class Meta:
        model = Font
        fields = ('title', 'author_name', 'status', 'id', 'image', 'image_thumbnail')
        read_only_fields = ('id', 'author_name', 'image_thumbnail')  #, 'status')
