from django.db import models

from apps.main.student.models import Student


class Blog(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
    )
    paid_contract_sum = models.FloatField(
        default=0,
        null=True
    )

    class Meta:
        db_table = 'blog'
