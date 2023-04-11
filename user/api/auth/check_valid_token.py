from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class CheckTokenValid(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self):
        return Response(status=status.HTTP_200_OK)
