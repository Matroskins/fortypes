from rest_framework.response import Response

from fonts.serializers import CountSerializer


class CountViewMixin:
    serializer_class = CountSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(data={'count': queryset.count()})
        serializer.is_valid()
        return Response(serializer.data)
