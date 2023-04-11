from django.http import HttpResponse
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from apps.main.student.models import Student
from apps.main.student.serializers.update_student_avatar_serializer import UpdateStudentAvatarSerializer
from user.permissions.student_permission import StudentPermission


class UpdateAvatarStudent(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = UpdateStudentAvatarSerializer
    permission_classes = [StudentPermission, ]

    def update(self, request, *args, **kwargs):
        print(request.data)

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
