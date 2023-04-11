# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.dean.models import Dean
from user.models import User


class DeanCreateSerializer(serializers.ModelSerializer):
    """
    This SERIALIZER id used to create DEAN.
    This SERIALIZER creates USER first before creating DEAN.
    """
    user_id = serializers.CharField(max_length=150, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = Dean
        fields = [
            'user_id',
            'password',
            'fullname',
            'gender',
            'profile_image'
        ]

    def create(self, validated_data):
        """
        This method is used to create USER and DEAN
        """
        user_id = validated_data.get('user_id')
        password = validated_data.get('password')
        fullname = validated_data.get('fullname')
        gender = validated_data.get('gender')
        profile_image = validated_data.get('profile_image')

        try:
            user = User.objects.create_dean(USER_ID=user_id, password=password)
            dean = Dean.objects.create(
                fullname=fullname,
                gender=gender,
                profile_image=profile_image,
                user=user
            )
        except Exception as ex:
            raise Exception(ex)

        return dean
