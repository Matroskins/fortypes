import django_filters
from rest_framework import mixins
from rest_framework import status
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
from fonts.serializers import FontCreateSerializer, FontCountSerializer, FontGetSerializer


class FontViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Font.objects.all()
    serializer_class = FontGetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrSafe)
    filter_class = FontFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, IsAdminOrModeratedFilterBackend)

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        self.serializer_class = FontCreateSerializer
        request.data.update({"owner_id": request.user.pk})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(FontGetSerializer(instance).data, status=status.HTTP_201_CREATED, headers=headers)


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

# TODO Uploader view (include works count, likes) ??? Uploader or Author?
# TODO add (ex. write tools) tags, get tags
# TODO login, logout view
# TODO support only jpg and png
# TODO - how many letters - keep count in constance?
# TODO collections

# TODO - BACKLOG -  change font, change symbol views
