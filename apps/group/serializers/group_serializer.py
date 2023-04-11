from apps.group.models import Group


from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.faculty.models import Faculty

class FacultySerializer(ModelSerializer):
    dean = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = [
            'id',
            'name',
            'dean',
        ]
        ref_name = 'FacultySerializer for GroupSerializer'

    def get_dean(self, obj):
        return str(obj.dean)


class GroupSerializer(ModelSerializer):
    faculty = FacultySerializer(help_text='FacultySerializer for GroupSerializer', read_only=True, many=False)

    class Meta:
        model = Group
        fields = [
            'id',
            'faculty',
            'name',
            'type_education',
            'language',
            'level',
        ]
