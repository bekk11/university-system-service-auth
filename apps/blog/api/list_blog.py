from rest_framework.generics import ListAPIView
from apps.blog.models import Blog
from apps.blog.serializers.blog_serializer import BlogListSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission


class BlogListAPIView(ListAPIView):
    """
    This API is used to list entire BLOG.
    """
    queryset = Blog.objects.select_related('student').all()
    serializer_class = BlogListSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]

    # User can search, filter by student fullname, group, student_id - 18-19 lines
    search_fields = ['fullname', 'group', ]
    filterset_fields = ['id', 'student', ]
