from urllib.request import Request

from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request: Request, view, obj):
        return request.method in SAFE_METHODS or request.user == obj.author

    def has_permission(self, request: Request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.id == int(request.data.get('author', None)):
            return True
