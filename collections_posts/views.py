from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from collections_posts.models import CollectionPost
from collections_posts.serializers import CollectionPostSerializer


class CollectionPostViewSet(mixins.ListModelMixin,
                            GenericViewSet):
    queryset = CollectionPost.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CollectionPostSerializer
