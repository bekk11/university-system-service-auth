from rest_framework.serializers import ModelSerializer

from apps.main.student.models import Student


class StudentListSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "fullname",
            "gender",
            "date_of_birth",
            "region_of_birth",
            "nation",
            "type_of_school",
            "description",
            "from_course_to_course",
            "profile_image",
            "ID_CARD",
            "passport_series",
            "JSHIR",
            "order_date",
            "user_id",
            "group_id"
        ]
