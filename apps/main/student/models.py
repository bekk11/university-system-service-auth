from django.db import models

from apps.group.models import Group
from user.models import User


class Student(models.Model):
    GENDER = [
        ['MALE', 'MALE'],
        ['FEMALE', 'FEMALE'],
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True
    )
    fullname = models.CharField(
        max_length=150
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    region_of_birth = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    nation = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    type_of_school = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    from_course_to_course = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    profile_image = models.ImageField(
        upload_to='profile_images_student/',
        null=True,
        blank=True
    )

    ID_CARD = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        default=None
    )

    passport_series = models.CharField(
        max_length=15,
        unique=True
    )

    JSHIR = models.CharField(
        max_length=14,
        unique=True,
        null=True,
        blank=True
    )

    order_date = models.DateField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'student'
        ordering = ['fullname', ]


class StudentExelData(models.Model):
    dean_id = models.IntegerField(null=False)
    exel_file = models.FileField(upload_to='student_exel_data/')

    def __str__(self):
        return str(self.dean_id)

    class Meta:
        db_table = 'student_exel_data'
        ordering = ['dean_id']
