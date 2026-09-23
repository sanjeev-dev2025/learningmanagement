from django.contrib import admin
from course.models import Course,Category,Lesson,Section
# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Section)