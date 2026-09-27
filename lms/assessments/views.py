from accounts.permissions import IsStudent,IsAdminUserorTeacherorStudent
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from assessments.models import Assessment,AssessmentSubmission
from assessments.serializers import AssessmentSerializer,AssessmentSubmissionSerializer
from accounts.permissions import IsAdminUserOrTeacher
class AssessmentListCreateAPIView(generics.ListCreateAPIView):
    queryset=Assessment.objects.all()
    serializer_class=AssessmentSerializer
    
    def get_permissions(self):
        if self.request.method=='GET':
            return[IsAuthenticated()]
        else:
            return[IsAdminUserOrTeacher()]

class AssessmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Assessment.objects.all()
    serializer_class=AssessmentSerializer
    def get_permissions(self):
        if self.request.method=='GET':
            return[IsAuthenticated()] 
        else:
            return[IsAdminUserOrTeacher()]


class AssessmentSubmissionListCreateAPIView(generics.ListCreateAPIView):
    queryset=AssessmentSubmission.objects.all()
    serializer_class=AssessmentSubmissionSerializer
    def get_permissions(self):
        if self.request.method=='GET':
            return[IsAdminUserorTeacherorStudent()] 
        return[IsStudent()]
    def get_queryset(self):
        qs=super().get_queryset()
        if not self.request.user.is_staff:
            qs=qs.filter(student=self.request.user)
        return qs
    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class AssessmentSubmissionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=AssessmentSubmission.objects.all()
    serializer_class=AssessmentSubmissionSerializer
    def get_permissions(self):
        if self.request.method=='GET':
            return[IsAuthenticated()]  
        return[IsAuthenticated()]
    def get_queryset(self):
        qs=super().get_queryset()
        if not self.request.user.is_staff:
            qs=qs.filter(student=self.request.user)
        return qs
        