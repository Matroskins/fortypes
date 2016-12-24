from rest_framework.serializers import ModelSerializer

from collections_posts.models import CollectionImagesBlock, CollectionImage, CollectionText, CollectionPost
from core.serializers import ImageObjOutSerializer


class ImageBlockSerializer(ModelSerializer):
    class Meta:
        model = CollectionImagesBlock
        fields = ('id', 'order')


class CollectionImageSerializer(ModelSerializer):
    image = ImageObjOutSerializer()

    class Meta:
        model = CollectionImage
        fields = ('id', 'order', 'image', 'block')


class CollectionTextSerializer(ModelSerializer):
    class Meta:
        model = CollectionText
        fields = ('id', 'text', 'order')


class CollectionPostSerializer(ModelSerializer):
    images_blocks = ImageBlockSerializer(many=True)
    images = CollectionImageSerializer(many=True)
    texts = CollectionTextSerializer(many=True)

    class Meta:
        model = CollectionPost
        fields = ('id', 'title', 'up_title', 'status', 'images_blocks', 'images', 'texts')
