from django.contrib import admin

from apps.main.student.models import Student, StudentExelData


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fullname',
        'ID_CARD',
        'passport_series',
        'user',
        'group',
        'gender',
        'date_of_birth',
        'region_of_birth',
        'nation',
        'type_of_school',
        'description',
        'from_course_to_course',

    ]


@admin.register(StudentExelData)
class StudentExelDataAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'dean_id',
        'exel_file'
    ]
