from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)


class Major(models.Model):
    name = models.CharField(max_length=20)
    code = models.PositiveIntegerField()


class Taken(models.Model):
    major = models.ForeignKey(Major)
    student_id = models.CharField(max_length=10)
    semester = models.CharField(max_length=1)
    professor = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    graduate = models.CharField(max_length=3, null=True)
    front_code = models.CharField(max_length=5)
    back_code = models.CharField(max_length=5)
    grade = models.FloatField()
    course = models.ForeignKey(Course)
