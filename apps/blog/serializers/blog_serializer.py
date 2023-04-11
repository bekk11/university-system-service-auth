from rest_framework.serializers import ModelSerializer
from apps.blog.models import Blog


class BlogListSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
