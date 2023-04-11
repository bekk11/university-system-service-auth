import traceback

from rest_framework import serializers

from apps.main.student.models import Student
from user.models import User


class StudentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'group',
            'fullname',
            'gender',
            'date_of_birth',
            'region_of_birth',
            'nation',
            'type_of_school',
            'description',
            'from_course_to_course',
            'profile_image',
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

    def update(self, instance, validated_data):
        try:
            glob_user = User.objects.get(id=instance.user.id)
        except Exception as ex:
            raise Exception(ex)

        glob_user.USER_ID = validated_data.get('ID_CARD', glob_user.USER_ID)

        if validated_data.get('passport_series'):
            glob_user.set_password(str(validated_data['passport_series']))

        glob_user.save()

        instance.group = validated_data.get('group', instance.group)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.region_of_birth = validated_data.get('region_of_birth', instance.region_of_birth)
        instance.nation = validated_data.get('nation', instance.nation)
        instance.type_of_school = validated_data.get('type_of_school', instance.type_of_school)
        instance.description = validated_data.get('description', instance.description)
        instance.from_course_to_course = validated_data.get('from_course_to_course', instance.from_course_to_course)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.ID_CARD = validated_data.get('ID_CARD', instance.ID_CARD)
        instance.passport_series = validated_data.get('passport_series', instance.passport_series)
        instance.JSHIR = validated_data.get('JSHIR', instance.JSHIR)
        instance.order_date = validated_data.get('order_date', instance.order_date)

        return instance
