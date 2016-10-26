from rest_framework.serializers import ModelSerializer, ImageField

from core.models import ImageObj


class ImageObjOutSerializer(ModelSerializer):
    image_original = ImageField()

    class Meta:
        model = ImageObj
        # TODO add image_thumbnail
        fields = ('image_original',)  # , 'image_thumbnail')


class ImageObjInSerializer(ModelSerializer):
    class Meta:
        model = ImageObj
        fields = ('id',)
