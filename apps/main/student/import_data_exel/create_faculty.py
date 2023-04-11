from django.core.exceptions import ObjectDoesNotExist
from apps.faculty.models import Faculty

SERVER = 'http://127.0.0.1:8000'


def create_faculty(cleared_datas, dean_id):
    passed_faculties = []
    for data in cleared_datas:
        if data['faculty'] not in passed_faculties:
            try:
                Faculty.objects.get(name=str(data['faculty']), dean__id=dean_id)
            except ObjectDoesNotExist:
                try:
                    Faculty.objects.create(
                        name=str(data['faculty']),
                        dean_id=dean_id
                    )
                except Exception as ex:
                    print(ex)
                else:
                    passed_faculties.append(data['faculty'])
                    print("Faculty has been created!!!")
            else:
                passed_faculties.append(data['faculty'])
                print("Faculty exists. Not created!!!")
