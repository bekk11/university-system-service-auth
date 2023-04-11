from rest_framework.serializers import ModelSerializer

from apps.group.serializers.group_serializer import GroupSerializer
from apps.main.student.models import Student


class StudentDetailSerializer(ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Student
        fields = [
            'id',
            'group',
            'fullname',
            'profile_image',
            'ID_CARD',
            'passport_series',
        ]
