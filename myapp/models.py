from django.contrib.postgres.fields import JSONField
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    count = models.PositiveIntegerField(default=0)


class Major(models.Model):
    name = models.CharField(max_length=20)
    code = models.PositiveIntegerField()


class Taken(models.Model):
    major = models.ForeignKey(Major)
    student_id = models.CharField(max_length=10)
    credit = models.PositiveIntegerField(default=0)
    semester = models.PositiveIntegerField()
    professor = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    graduate = models.CharField(max_length=3, null=True)
    front_code = models.CharField(max_length=5)
    back_code = models.CharField(max_length=5)
    grade = models.FloatField()
    course = models.ForeignKey(Course)


class TakenList(models.Model):
    student_id = models.CharField(max_length=10)
    semester = models.PositiveIntegerField()
    course_list = JSONField()


class Data(models.Model):
    rate = models.FloatField()
    diff = models.IntegerField()
    taken_course = models.CharField(max_length=100)
    related_course = models.CharField(max_length=100)
