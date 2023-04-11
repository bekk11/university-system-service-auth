# Rest-Framework
from rest_framework import serializers

# Project
from apps.notification.models import Notification


class NotificationUpdateSerializer(serializers.ModelSerializer):
    updated = serializers.HiddenField(default=False)

    class Meta:
        model = Notification
        fields = [
            'blog',
            'message',
            'updated'
        ]

    def update(self, instance, validated_data):
        blog = instance.blog

        blog.student = validated_data.get('blog__student', blog.student)
        blog.paid_contract_sum = validated_data.get('blog__paid_contract_sum', blog.paid_contract_sum)
        blog.save()

        if instance.message != validated_data.get('message'):
            instance.updated = True
        instance.update = False

        instance.message = validated_data.get('message', instance.message)
        instance.save()

        return instance
