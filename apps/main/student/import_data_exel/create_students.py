from django.core.exceptions import ObjectDoesNotExist

from apps.group.models import Group
from apps.main.student.models import Student
from apps.main.student.serializers.student_create_update_serializer import StudentCreateUpdateSerializer


def create_student(cleaned_data):
    groups = {}

    list_groups = Group.objects.all().values('id', 'name')

    for group in list_groups:
        groups[str(group['name'])] = group['id']

    for data in cleaned_data:
        try:
            Student.objects.get(
                fullname=str(data['fio']),
                group_id=int(groups[str(data['group'])])
            )
        except ObjectDoesNotExist:
            try:
                serializer = StudentCreateUpdateSerializer(data={
                    "group": int(groups[str(data['group'])]),
                    "fullname": str(data['fio']),
                    "gender": str(data['sex']),
                    "date_of_birth": data['date_birth'],
                    "region_of_birth": data['region_birth'],
                    "nation": str(data['nation']),
                    "type_of_school": str(data['type_school']),
                    "description": str(data['description']),
                    "from_course_to_course": str(data['course_from_course']),
                    "ID_CARD": str(data['id_card']),
                    "passport_series": str(data['passport']),
                    "order_date": str(data['order_date'])
                })
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except Exception as ex:
                print(ex)
            else:
                print("Student has been created!!!")
        else:
            print("Student exists. Not created!!!")
