from django.shortcuts import render
from rest_framework import generics
from course.serializers import CategorySerializer,CourseSerializer,LessonSerializer,SectionSerializer
from course.models import Category,Course,Lesson,Section
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from accounts.permissions import IsAdminUser,IsStudent,IsTeacher
from rest_framework.decorators import api_view,permission_classes

class CategoryListCreateAPIView(generics.ListCreateAPIView): 
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        return [IsAdminUser()]
class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAdminUser]
class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return[IsAuthenticated()]
        else:
            return[IsAdminUser() or IsTeacher()]

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return[IsAuthenticated()]
        else:
            return[IsAdminUser() or IsTeacher()]

class SectionListCreateAPIView(generics.ListCreateAPIView):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return[IsAuthenticated()]
        else:
            return[IsAdminUser() or IsTeacher()]

class SectionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return[IsAuthenticated()]
        else:
            return[IsAdminUser() or IsTeacher()]

class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset=Lesson.objects.all()
    serializer_class=LessonSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return[IsAuthenticated()]
        else:
            return[IsAdminUser() or IsTeacher()]

class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Lesson.objects.all()
    serializer_class=LessonSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return[IsAuthenticated()]
        else:
            return[IsAdminUser() or IsTeacher()]