import django_filters
from rest_framework import mixins
from rest_framework import status
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.mixins import CountViewMixin
from core.models import ImageObj
from core.permissions import IsOwnerOrSafe
from core.serializers import ImageObjOutSerializer
from fonts.filter_backend import IsAdminOrModeratedFilterBackend
from fonts.filters import FontFilter, AuthorFilter
from fonts.models import Font, Author, Tag, Symbol
from fonts.serializers import FontCreateSerializer, CountSerializer, FontGetSerializer, AuthorSerializer, \
    TagSerializer


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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(FontGetSerializer(instance).data, status=status.HTTP_201_CREATED, headers=headers)


class FontCountView(CountViewMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Font.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_class = FontFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


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


class AuthorView(mixins.ListModelMixin,
                 GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_class = AuthorFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class TagView(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        request.data['owner'] = request.user.pk
        return super().create(request, *args, **kwargs)


class SymbolsCountView(CountViewMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    queryset = Symbol.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

# TODO collections (new app)

# TODO - BACKLOG - update user serializer - change author
# TODO - BACKLOG -  change font, change symbol views
# TODO - BACKLOG - support only jpg and png ???
