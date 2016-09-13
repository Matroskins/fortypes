from rest_framework.fields import SerializerMethodField, ModelField, IntegerField
from rest_framework.serializers import ModelSerializer

from accounts.models import Account
from .models import Font, Symbol


class SymbolForFontSerializer(ModelSerializer):
    class Meta:
        model = Symbol
        fields = ('value', 'point_one_x', 'point_one_y', 'point_two_x', 'point_two_y')


class FontSerializer(ModelSerializer):
    symbols = SymbolForFontSerializer(many=True)
    author_name = SerializerMethodField()
    author_id = IntegerField(required=False)

    def get_author_name(self, instance):
        return instance.author.user.get_full_name()

    def create(self, validated_data):
        author = validated_data.pop('author_id')
        symbols_data = validated_data.pop('symbols')
        font = Font.objects.create(author_id=author, **validated_data)
        for symbol_data in symbols_data:
            Symbol.objects.create(font=font, **symbol_data)
        return font

    class Meta:
        model = Font
        fields = ('content', 'author_name', 'status', 'id', 'image', 'image_thumbnail', 'symbols', 'author_id')
        read_only_fields = ('id', 'author_name', 'image_thumbnail')  #, 'status')
        extra_kwargs = {'author_id': {'write_only': True}}
