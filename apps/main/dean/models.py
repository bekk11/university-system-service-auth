from django.db import models

from user.models import User


class Dean(models.Model):
    GENDER = [
        ['MALE', 'MALE'],
        ['FEMALE', 'FEMALE'],
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    fullname = models.CharField(
        max_length=150
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER
    )

    profile_image = models.ImageField(
        upload_to='profile_images_dean/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'dean'
