from django.urls import path

from user.api.auth.check_valid_token import CheckTokenValid
from user.api.auth.custom_token import CustomToken
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from user.api import UserListAPIView, UserRetrieveAPIView

urlpatterns = [
    path('token/', CustomToken.as_view(), name='token_obtain_pair'),
    path('token/check/', CheckTokenValid.as_view(), name='check_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('list/', UserListAPIView.as_view()),
    path('retrieve/<int:pk>/', UserRetrieveAPIView.as_view()),
]
