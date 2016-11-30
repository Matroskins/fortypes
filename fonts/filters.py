import django_filters
from django_filters.rest_framework import FilterSet

from fonts.models import Font


class FontFilter(FilterSet):
    content = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Font
        fields = ['content']
