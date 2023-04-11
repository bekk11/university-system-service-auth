from django.db import models

from apps.blog.models import Blog
from user.models import User


class Notification(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE
    )
    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.BooleanField(
        default=False
    )

    class Meta:
        db_table = 'notification'
