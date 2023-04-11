from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from apps.main.dean.models import Dean
from apps.main.deputy_dean.models import DeputyDean
from apps.main.student.models import Student


class CustomStudentTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['ROLE'] = user.ROLE

        if user.ROLE == 'STUDENT':
            token['user_detail_id'] = Student.objects.get(user=user.id).id
        elif user.ROLE == 'DEAN':
            token['user_detail_id'] = Dean.objects.get(user=user.id).id
        elif user.ROLE == 'DEPUTY_DEAN':
            token['user_detail_id'] = DeputyDean.objects.get(user=user.id).id

        return token
