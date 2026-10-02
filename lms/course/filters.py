import django_filters
from course.models import Course
class CourseFilter(django_filters.FilterSet):
    class Meta:
        model=Course
        fields={
            "title":["exact"],
            "teacher":["exact"],
            "category":["exact"],
            "price":["exact","gte","lte"],
            "is_active":["exact"],
        }       