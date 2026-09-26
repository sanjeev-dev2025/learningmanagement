from django.db import models

# Create your models here.
from course.models import Course
from django.conf import settings
class Assessment(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    descritpion=models.TextField(blank=True)
    total_marks=models.IntegerField(default=100)
    questions=models.JSONField(default=list,blank=True)
    def __str__(self):
        return f"{self.course}...{self.title}"  


    