from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Section(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title