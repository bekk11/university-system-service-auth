from django.db import transaction
from rest_framework.serializers import ModelSerializer

from apps.main.teacher.models import Teacher
from user.models import User


class TeacherCreateSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'id',
            'firstname',
            'lastname',
            'fathername',
            'profile_image',
            'date_of_birth',
            'gender',
            'ID_CARD',
            'passport_series',
            'speciality',
            'description',
        ]

    @transaction.atomic
    def create(self, validated_data):
        ModelClass = self.Meta.model

        global_user_info = {
            'USER_ID': validated_data.get('ID_CARD'),
            'password': validated_data.get("passport_series"),
        }

        try:
            glob_user = User.objects.create_teacher(**global_user_info)
        except Exception as ex:
            raise Exception(ex)

        try:
            teacher = ModelClass.objects.create(**validated_data, user=glob_user)
        except Exception as ex:
            raise Exception(ex)

        return teacher
