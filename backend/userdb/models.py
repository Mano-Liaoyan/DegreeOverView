# Create your models here.
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Student(User):
    pass


class Lecturer(User):
    pass


class CourseDesigner(User):
    pass
