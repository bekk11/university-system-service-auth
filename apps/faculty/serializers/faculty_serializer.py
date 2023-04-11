from rest_framework.serializers import ModelSerializer
from apps.faculty.models import Faculty


class FacultySerializer(ModelSerializer):

    class Meta:
        model = Faculty
        fields = '__all__'
        ref_name = 'FacultySerializer'
