from rest_framework import response, schemas
from rest_framework import schemas
from rest_framework.decorators import detail_route
from rest_framework.viewsets import ModelViewSet
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


class BaseModelViewSet(ModelViewSet):
    renderer_classes = [SwaggerUIRenderer, OpenAPIRenderer]

    @detail_route(methods=['get'], url_path='docs')
    def get_docs(self, request, *args, **kwargs):
        """
        Get documentation for this viewset
        """
        generator = schemas.SchemaGenerator(title='Docs for API')
        return response.Response(generator.get_schema(request=request))
