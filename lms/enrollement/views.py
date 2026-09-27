from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from enrollement.models import Enrollement
from enrollement.serializers import EnrollementSerializer
from accounts.permissions import IsStudent,IsAdminUser,IsTeacher,IsAdminUserOrTeacher

class EnrollmentListCreateAPIView(generics.ListCreateAPIView):
    queryset=Enrollement.objects.all()
    serializer_class=EnrollementSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        return[IsStudent()]
    def get_queryset(self):
        qs=super().get_queryset()
        if not self.request.user.is_staff:
            qs=qs.filter(student=self.request.user)
        return qs
    def perform_create(self,serializer):
        serializer.save(student=self.request.user)

class EnrollementRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Enrollement.objects.all()
    serializer_class=EnrollementSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return [AllowAny()]
        return[IsStudent()]
    def get_queryset(self):
        qs=super().get_queryset()
        if not self.request.user.is_staff:
            qs=qs.filter(student=self.request.user)
        return qs