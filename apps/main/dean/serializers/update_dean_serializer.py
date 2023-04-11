# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.dean.models import Dean


class DeanUpdateSerializer(serializers.ModelSerializer):
    """
    This SERIALIZER id used to update DEAN.
    This SERIALIZER updates USER first before creating DEAN.
    """
    user_id = serializers.CharField(max_length=150, write_only=True, allow_blank=True, allow_null=True)
    role = serializers.CharField(max_length=15, write_only=True, allow_blank=True, allow_null=True)
    password = serializers.CharField(max_length=128, write_only=True, allow_blank=True, allow_null=True)

    class Meta:
        model = Dean
        fields = [
            'user_id',
            'role',
            'password',
            'fullname',
            'gender',
            'profile_image'
        ]

    def update(self, instance, validated_data):
        """
        This method is used to update USER and DEAN
        """
        user = instance.user

        user.USER_ID = validated_data.get('user_id', user.USER_ID)
        user.ROLE = validated_data.get('role', user.ROLE)
        user.set_password(str(validated_data.get('password')))
        user.save()

        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.save()

        return instance
