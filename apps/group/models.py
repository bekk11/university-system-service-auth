from django.db import models

from apps.faculty.models import Faculty


class Group(models.Model):
    TYPES_OF_EDUCATION = [
        ['FULL_TIME', 'FULL_TIME'],
        ['EVENING', 'EVENING'],
        ['DISTANCE_LEARNING', 'DISTANCE_LEARNING'],
    ]

    LANGUAGE = [
        ['EN', 'EN'],
        ['UZ', 'UZ'],
        ['RU', 'RU'],
        ['KOR', 'KOR'],
    ]

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(
        max_length=150,
        unique=True,
    )
    type_education = models.CharField(
        max_length=20,
        choices=TYPES_OF_EDUCATION
    )
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE
    )
    level = models.SmallIntegerField(
        default=1,
        null=True,
    )

    class Meta:
        db_table = 'group'

    def __str__(self):
        return self.name
