from django.db import models

from user.models import User


class Teacher(models.Model):
    GENDER = [
        ['MALE', 'MALE'],
        ['FEMALE', 'FEMALE'],
    ]
    # ----------------------------------------
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    # ----------------------------------------
    firstname = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    # ----------------------------------------
    lastname = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    # ----------------------------------------
    fathername = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    # ----------------------------------------
    profile_image = models.ImageField(
        upload_to='profile_images_teacher/',
        null=True,
        blank=True
    )
    # ----------------------------------------
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    # ----------------------------------------
    gender = models.CharField(
        max_length=10,
        choices=GENDER
    )
    # ----------------------------------------
    ID_CARD = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        default=None
    )
    # ----------------------------------------
    passport_series = models.CharField(
        max_length=15,
        unique=True
    )
    # ----------------------------------------
    speciality = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    # ----------------------------------------
    description = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )
    # ----------------------------------------

    def __str__(self):
        return str(self.firstname + self.lastname + self.fathername)

    class Meta:
        db_table = 'teacher'
