from django.contrib import admin

from apps.main.teacher.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'firstname',
        'lastname',
        'fathername',
        'profile_image',
        'date_of_birth',
        'gender',
        'ID_CARD',
        'passport_series',
        'speciality',
        'description',
    ]
