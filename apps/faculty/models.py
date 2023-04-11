from django.db import models

from apps.main.dean.models import Dean


class Faculty(models.Model):
    name = models.CharField(
        max_length=150
    )
    dean = models.ForeignKey(
        Dean,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'faculty'

    def __str__(self):
        return self.name
