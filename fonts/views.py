from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from fonts.models import Font
from fonts.serializers import FontSerializer


class FontViewSet(ModelViewSet):
    queryset = Font.objects.all()
    serializer_class = FontSerializer
    # TODO permissions
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        request.data.update({"owner_id": request.user.account.pk})
        return super().create(request, *args, **kwargs)
