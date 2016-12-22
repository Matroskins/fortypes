from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from core.permissions import IsOwner
from fonts.models import Font
from user_font_relation.filter_backends import IsOwnerFilterBackend
from user_font_relation.models import UserFontRelation
from user_font_relation.serializers import UserFontRelationSerializer


class UserFontRelationsViewSet(mixins.UpdateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.ListModelMixin,
                               GenericViewSet):
    queryset = UserFontRelation.objects.all()
    serializer_class = UserFontRelationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwner)
    filter_backends = (IsOwnerFilterBackend,)
    lookup_field = 'font'

    def get_object(self):
        font_id = self.kwargs[self.lookup_field]
        font = get_object_or_404(Font.objects.all(), **{'pk': font_id})
        filter_kwargs = {self.lookup_field: font}
        UserFontRelation.objects.get_or_create(user=self.request.user, **filter_kwargs)
        return super().get_object()
