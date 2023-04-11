from rest_framework import serializers

from apps.group.models import Group
from apps.main.student.models import Student
from user.models import User


class StudentCreateExelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'fullname',
            'group',
            'gender',
            'date_of_birth',
            'region_of_birth',
            'nation',
            'type_of_school',
            'description',
            'from_course_to_course',
            'ID_CARD',
            'passport_series',
            'JSHIR',
            'order_date',
        ]

    def create(self, validated_data):
        ModelClass = self.Meta.model

        global_user_info = {
            'USER_ID': validated_data.get('ID_CARD'),
            'password': validated_data.get('passport_series'),
        }

        try:
            glob_user = User.objects.create_student(**global_user_info)
        except Exception as ex:
            raise Exception(ex)

        try:
            student = ModelClass.objects.create(**validated_data, user=glob_user)
        except Exception as ex:
            raise Exception(ex)

        return student
