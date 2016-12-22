from rest_framework.serializers import ModelSerializer

from user_font_relation.models import UserFontRelation


class UserFontRelationSerializer(ModelSerializer):
    class Meta:
        model = UserFontRelation
        fields = ('font', 'like', 'shared_facebook', 'shared_vk', 'shared_twitter')
