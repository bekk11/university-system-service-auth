from rest_framework import serializers

from apps.main.student.models import Student


class UpdateStudentAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['profile_image', ]

    def update(self, instance, validated_data):
        image = validated_data.pop('profile_image', None)

        if image:
            instance.profile_image = image
            instance.save()

        return instance
