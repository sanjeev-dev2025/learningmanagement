from course.models import Course,Category,Lesson,Section
from rest_framework import serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']
        read_only_fields = ['id']
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id','title','description','teacher','category']
        read_only_fields = ['id']
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields=['id','title','content','section']
        read_only_fields = ['id']
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Section
        fields=['id','title','course']
        read_only_fields = ['id']
        