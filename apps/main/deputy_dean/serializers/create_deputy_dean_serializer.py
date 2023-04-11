# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.deputy_dean.models import DeputyDean
from user.models import User


class DeputyDeanCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(max_length=150, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = DeputyDean
        fields = [
            'user_id',
            'password',
            'dean',
            'fullname',
            'gender',
            'profile_image'
        ]

    def create(self, validated_data):
        user_id = validated_data.get('user_id')
        password = validated_data.get('password')
        fullname = validated_data.get('fullname')
        gender = validated_data.get('gender')
        profile_image = validated_data.get('profile_image')
        dean = validated_data.get('dean')

        try:
            user = User.objects.create_deputy_dean(USER_ID=user_id, password=password)
            deputy_dean = DeputyDean.objects.create(
                fullname=fullname,
                gender=gender,
                profile_image=profile_image,
                dean=dean,
                user=user
            )
        except Exception as ex:
            raise Exception(ex)

        return deputy_dean
