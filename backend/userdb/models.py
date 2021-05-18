# Create your models here.
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Student(User):
    s_id = models.IntegerField(primary_key=True, auto_created=True)
    pass


class Lecturer(User):
    lec_id = models.IntegerField(primary_key=True, auto_created=True)
    pass


class CourseDesigner(User):
    cd_id = models.IntegerField(primary_key=True, auto_created=True)
    pass


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True, auto_created=True)
    course_name = models.CharField(max_length=40, unique=True)
    course_code = models.CharField(max_length=10, unique=True)
    academic_start_year = models.IntegerField()
    program = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    cilos = models.ForeignKey("Cilo", on_delete=models.CASCADE)
    assessment = models.CharField(max_length=1000)
    pre_request_course_id = models.ForeignKey("self", on_delete=models.DO_NOTHING)


class Cilo(models.Model):
    cilo_id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.TextField()

    def get_clio(self):
        return self.content


class Assessment(models.Model):
    assessment_id = models.IntegerField(primary_key=True, auto_created=True)
    evaluation_method = models.TextField()
    percentage = models.TextField()
    cilos = models.ForeignKey("Cilo", on_delete=models.CASCADE)
