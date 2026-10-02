from cloudinary_storage.storage import MediaCloudinaryStorage
from django.db import models
from django.conf import settings
# pyrefly: ignore [missing-import]
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,related_name='courses'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    is_active=models.BooleanField(default=True)
    

    def __str__(self):
        return self.title


class Section(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,related_name='sections'
    )
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,related_name="lessons"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    videos=models.FileField(upload_to="lessons/videos",storage=MediaCloudinaryStorage(),blank=True,null=True)

    def __str__(self):
        return self.title