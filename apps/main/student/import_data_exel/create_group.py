from django.core.exceptions import ObjectDoesNotExist

from apps.faculty.models import Faculty
from apps.group.models import Group


def create_group(cleared_datas):
    passed_groups = []
    faculties = {}

    list_faculties = Faculty.objects.all().values('id', 'name')

    for faculty in list_faculties:
        faculties[str(faculty['name'])] = faculty['id']

    for data in cleared_datas:
        if data['group'] not in passed_groups:
            try:
                Group.objects.get(name=str(data['group']), faculty__name=data['faculty'])
            except ObjectDoesNotExist:
                try:
                    Group.objects.create(
                        faculty_id=faculties[data['faculty']],
                        name=str(data['group']),
                        type_education="FULL_TIME",
                        language=str(data['lang']),
                        level=int(data['level']),
                    )
                except Exception as ex:
                    print(ex)
                else:
                    passed_groups.append(data['group'])
                    print("Group has been created!!!")
            else:
                passed_groups.append(data['group'])
                print("Group exists. Not created!!!")
