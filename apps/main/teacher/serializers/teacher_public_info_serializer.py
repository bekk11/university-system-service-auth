from rest_framework import serializers

from apps.main.teacher.models import Teacher


class TeacherPublicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'id',
            'firstname',
            'lastname',
            'fathername'
        ]
