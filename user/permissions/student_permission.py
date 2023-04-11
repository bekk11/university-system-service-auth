from rest_framework.permissions import BasePermission

from apps.main.student.models import Student


class StudentPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_anonymous and request.user.ROLE == 'STUDENT')
