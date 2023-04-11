from rest_framework.generics import UpdateAPIView

from apps.blog.models import Blog
from apps.blog.serializers.blog_serializer import BlogListSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class BlogUpdateAPIView(UpdateAPIView):
    """
    This API is used to update only ONE BLOG and must contain all required fields.
    """
    queryset = Blog.objects.select_related('student').all()
    serializer_class = BlogListSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]
