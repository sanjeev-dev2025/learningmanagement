from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from assessments.models import Assessment
from assessments.serializers import AssessmentSerializer
from accounts.permissions import IsAdminUserOrTeacher
class AssessmentListCreateAPIView(generics.ListCreateAPIView):
    queryset=Assessment.objects.all()
    serializer_class=AssessmentSerializer
    
    def get_permissions(self):
        if self.request.method=='GET':
            return[IsAuthenticated]
        else:
            return[IsAdminUserOrTeacher()]

class AssessmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Assessment.objects.all()
    serializer_class=AssessmentSerializer
    def get_permissions(self):
        if self.request.method=='GET':
            return[IsAuthenticated] 
        else:
            return[IsAdminUserOrTeacher()]


