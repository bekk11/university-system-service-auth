# Rest-Framework
from rest_framework.serializers import ModelSerializer

# Project
from apps.main.dean.models import Dean
from user.models import User


class DeanSerializer(ModelSerializer):
    """
    This SERIALIZER is used to list, retrieve, destroy DEAN.
    """
    class Meta:
        model = Dean
        fields = [
            'id',
            'user_id',
            'fullname',
            'gender',
            'profile_image'
        ]
