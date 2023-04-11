from rest_framework_simplejwt.views import TokenObtainPairView

from user.serializers.auth.custom_token_serializer import CustomStudentTokenSerializer


class CustomToken(TokenObtainPairView):
    serializer_class = CustomStudentTokenSerializer
