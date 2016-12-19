import django_filters
from django_filters.rest_framework import FilterSet

from fonts.models import Font


class FontFilter(FilterSet):
    content_contains = django_filters.CharFilter(lookup_expr='contains', name='content')
    content_exact = django_filters.CharFilter(lookup_expr='exact', name='content')

    class Meta:
        model = Font
        fields = ['content']
