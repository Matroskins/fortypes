import django_filters
from django_filters.rest_framework import FilterSet

from fonts.models import Font, Author


class FontFilter(FilterSet):
    content_contains = django_filters.CharFilter(lookup_expr='contains', name='content')
    content_exact = django_filters.CharFilter(lookup_expr='exact', name='content')

    class Meta:
        model = Font
        fields = ['content']


class AuthorFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Author
        fields = ['name']
