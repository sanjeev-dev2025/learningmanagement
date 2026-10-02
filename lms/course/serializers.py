from course.models import Course, Category, Lesson, Section
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']

class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.ReadOnlyField(source='teacher.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'is_active', 'teacher', 'teacher_name', 'category', 'category_name']
        read_only_fields = ['id']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'section','videos']
        read_only_fields = ['id']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'title', 'course']
        read_only_fields = ['id']
    