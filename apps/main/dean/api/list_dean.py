# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.main.dean.models import Dean
from apps.main.dean.serializers.dean_serializer import DeanSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission


class DeanListAPIView(ListAPIView):
    """
    This API is used to list entire DEAN.
    """
    queryset = Dean.objects.select_related('user').values('id',
                                                          'user_id',
                                                          'fullname',
                                                          'gender',
                                                          'profile_image')
    serializer_class = DeanSerializer
    permission_classes = [AdminPermission | DeanPermission]

    # User can search, filter by dean fullname, user role, user user_id, gender - 29-30 lines
    # User can be ordering by dean gender (for example: MALE or FEMALE) - 31 line
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["fullname", "user__ROLE", "user__USER_ID", "gender"]
    filterset_fields = ["fullname", "user__ROLE", "user__USER_ID", "gender"]
    ordering_fields = ["gender"]
    ordering = ["-id"]
