from django.db import models
# pyrefly: ignore [missing-import]
from cloudinary_storage.storage import RawMediaCloudinaryStorage
# Create your models here.
from course.models import Course
from django.conf import settings
class Assessment(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    descritpion=models.TextField(blank=True)
    questions=models.FileField(upload_to='assessment/questions',blank=True,null=True,storage=RawMediaCloudinaryStorage())
    def __str__(self):
        return f"{self.course}...{self.title}"  

class AssessmentSubmission(models.Model):
    assessment=models.ForeignKey(Assessment,on_delete=models.CASCADE)
    student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    submitted_answers=models.FileField(upload_to='assessment/submissions',blank=True,null=True,storage=RawMediaCloudinaryStorage())        
    submitted_at=models.DateTimeField(auto_now_add=True)
    remarks=models.TextField(blank=True)

    def __str__(self):
        return f"{self.student}....{self.assessment}"   