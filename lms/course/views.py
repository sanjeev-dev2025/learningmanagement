from rest_framework.parsers import MultiPartParser, FormParser
from accounts.permissions import IsAdminUserOrTeacher
from django.shortcuts import render
from rest_framework import generics
from course.serializers import CategorySerializer,CourseSerializer,LessonSerializer,SectionSerializer
from course.models import Category,Course,Lesson,Section
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from accounts.permissions import IsAdminUser, IsStudent, IsTeacher
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination 
from rest_framework import filters
from course.filters import CourseFilter 

class CategoryListCreateAPIView(generics.ListCreateAPIView): 
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    pagination_class=PageNumberPagination
    search_fields=['name']
    ordering_fields=['name']
    
    def get_permissions(self):
        if self.request.method=="GET":
            return [AllowAny()]
        return [IsAdminUser()]

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAdminUser]

class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    filterset_class=CourseFilter
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields=['title','description']
    ordering_fields=['title','description']
    def get_permissions(self):
        if self.request.method=="GET":
            return [AllowAny()]
        return [IsAdminUserOrTeacher()] 

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return [AllowAny()]
        return [IsAdminUserOrTeacher()]

class SectionListCreateAPIView(generics.ListCreateAPIView):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return[IsAuthenticated()]
        return[IsAdminUserOrTeacher()]

class SectionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return[IsAuthenticated()]
        return[IsAdminUserOrTeacher()]

class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset=Lesson.objects.all()
    serializer_class=LessonSerializer
    parser_classes = [MultiPartParser, FormParser]
    def get_permissions(self):
        if self.request.method=="GET":
            return[IsAuthenticated()]
        return[IsAdminUserOrTeacher()]

class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Lesson.objects.all()
    serializer_class=LessonSerializer
    def get_permissions(self):
        if self.request.method=="GET":
            return[IsAuthenticated()]
        return[IsAdminUserOrTeacher()]