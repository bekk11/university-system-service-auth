from rest_framework.generics import ListAPIView

from apps.main.student.models import Student
from apps.main.student.serializers.list_student_serializer import StudentListSerializer
from user.permissions.admin_permission import AdminPermission
from user.permissions.dean_permission import DeanPermission
from user.permissions.deputy_dean_permission import DeputyDeanPermission
from user.permissions.student_permission import StudentPermission


class ListStudent(ListAPIView):
    """
    This api is for getting list of students. But you should give params for request as "group__faculty__dean=dean_id"
    Without this part it will be big ERROR because we have more than 20,000 students!!!
    This API does not work for students, only for admin, dean, deputy_dean
    """
    queryset = Student.objects.all()  # Optimization will not help here, since filterset_fields() still makes additional queries to the Database
    serializer_class = StudentListSerializer
    permission_classes = [AdminPermission | DeanPermission | DeputyDeanPermission]
    filterset_fields = (
        'group',
        'gender',
        'nation',

        'group__faculty',
        'group__type_education',
        'group__language',
        'group__level',

        'group__faculty__dean',
    )
    search_fields = [
        'fullname',
    ]
