from rest_framework import serializers
from enrollement.models import Enrollement

class EnrollementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enrollement
        fields="__all__"   
    def validate_course(self, value):
        request = self.context['request']

        if Enrollement.objects.filter(
            student=request.user,
            course=value
        ).exists():
            raise serializers.ValidationError(
                "You are already enrolled in this course."
            )

        return value