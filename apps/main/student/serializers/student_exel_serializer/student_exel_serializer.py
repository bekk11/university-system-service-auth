from rest_framework import serializers

from apps.main.student.models import StudentExelData


class StudentExelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExelData
        fields = "__all__"
