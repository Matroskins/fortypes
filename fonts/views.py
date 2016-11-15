from rest_framework import mixins
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.models import ImageObj
from core.serializers import ImageObjOutSerializer
from fonts.models import Font
from fonts.serializers import FontSerializer


class FontViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Font.objects.all()
    serializer_class = FontSerializer
    # TODO permissions
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        request.data.update({"owner_id": request.user.account.pk})
        return super().create(request, *args, **kwargs)


class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, filename, format=None):
        file_obj = request.data['file']
        img_obj = ImageObj()
        img_obj.image_original.save(filename, file_obj)
        # img_obj.image_thumbnail.save(filename, file_obj)
        # img_obj.save()
        return Response(data=ImageObjOutSerializer(img_obj).data, status=200)
