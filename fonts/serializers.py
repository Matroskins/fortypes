from rest_framework.serializers import ModelSerializer

from .models import Font, Symbol


class FontSerializer(ModelSerializer):
    class Meta:
        model = Font
        fields = ('title', 'author', 'status', 'id')


class SymbolSerializer(ModelSerializer):
    class Meta:
        model = Symbol
        fields = ('title', 'author', 'status', 'id')
