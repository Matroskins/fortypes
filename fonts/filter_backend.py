from rest_framework.compat import is_authenticated
from rest_framework.filters import BaseFilterBackend


class IsAdminOrModeratedFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if is_authenticated(request.user) and (request.user.is_superuser or request.user.is_staff):
            return queryset
        return queryset.exclude(admin_relation__isnull=True).filter(admin_relation__moderated=True)
