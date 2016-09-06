from core.views import BaseModelViewSet
from fonts.models import Font
from fonts.serializers import FontSerializer


class FontViewSet(BaseModelViewSet):
    queryset = Font.objects.all()
    serializer_class = FontSerializer
