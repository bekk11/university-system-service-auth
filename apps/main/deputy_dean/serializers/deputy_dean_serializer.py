# Rest-Framework
from rest_framework.serializers import ModelSerializer

# Project
from apps.main.deputy_dean.models import DeputyDean


class DeputyDeanSerializer(ModelSerializer):
    class Meta:
        model = DeputyDean
        fields = ['id',
                  'fullname',
                  'gender',
                  'profile_image',
                  'user_id',
                  'dean_id',
                  ]
        ordering = ["-id"]
