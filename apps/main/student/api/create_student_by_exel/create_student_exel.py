from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.main.student.import_data_exel.start import start_importing
from apps.main.student.models import StudentExelData
from apps.main.student.serializers.student_exel_serializer.student_exel_serializer import StudentExelSerializer


class CreateStudentExel(CreateAPIView):
    queryset = StudentExelData.objects.all()
    serializer_class = StudentExelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        start_importing(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
