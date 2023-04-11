from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_anonymous and request.user.ROLE == 'ADMIN')
