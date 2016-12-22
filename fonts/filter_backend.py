from rest_framework.compat import is_authenticated
from rest_framework.filters import BaseFilterBackend

from fonts.models import STATUS_PUBLIC


class IsAdminOrModeratedFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if is_authenticated(request.user) and (request.user.is_superuser or request.user.is_staff):
            return queryset
        return queryset.filter(status=STATUS_PUBLIC)
