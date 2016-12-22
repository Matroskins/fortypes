from rest_framework import permissions


class IsOwnerOrSafe(permissions.BasePermission):
    message = 'Access to object not allowed.'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.method in permissions.SAFE_METHODS


class IsOwner(permissions.BasePermission):
    message = 'Access to object not allowed.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
