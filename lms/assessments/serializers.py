from rest_framework import serializers
from assessments.models import Assessment,AssessmentSubmission

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assessment
        fields='__all__'

class AssessmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=AssessmentSubmission
        fields="__all__"

  