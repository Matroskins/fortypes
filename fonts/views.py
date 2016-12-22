import django_filters
from rest_framework import mixins
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.models import ImageObj
from core.permissions import IsOwnerOrSafe
from core.serializers import ImageObjOutSerializer
from fonts.filter_backend import IsAdminOrModeratedFilterBackend
from fonts.filters import FontFilter
from fonts.models import Font
from fonts.serializers import FontSerializer, FontCountSerializer


class FontViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Font.objects.all()
    serializer_class = FontSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrSafe)
    filter_class = FontFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, IsAdminOrModeratedFilterBackend)

    def create(self, request, *args, **kwargs):
        request.data.update({"owner_id": request.user.pk})
        return super().create(request, *args, **kwargs)


class FontCountView(mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Font.objects.all()
    serializer_class = FontCountSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_class = FontFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(data={'count': queryset.count()})
        serializer.is_valid()
        return Response(serializer.data)


class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, filename, format=None):
        file_obj = request.data['file']
        img_obj = ImageObj()
        img_obj.image_original.save(filename, file_obj)
        # TODO FIXME
        # img_obj.image_thumbnail.save(filename, file_obj)
        # img_obj.save()
        return Response(data=ImageObjOutSerializer(img_obj).data, status=200)

# TODO like view
# TODO Uploader view (include works count, likes)
# TODO add (ex. write tools) tags, get tags
# TODO login, logout view
# TODO support only jpg and png
# TODO - how many letters - keep count in constance?
# TODO collections

# TODO - BACKLOG -  change font, change symbol views
