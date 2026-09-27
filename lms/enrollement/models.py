from django.db import models
from django.conf import settings
from course.models import Course

class Enrollement(models.Model):
    student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolled_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.student}....{self.course}"
