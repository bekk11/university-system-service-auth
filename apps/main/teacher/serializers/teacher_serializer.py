from rest_framework.serializers import ModelSerializer

from apps.main.teacher.models import Teacher


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
