from django.db import models

# Create your models here.
class Taken(models.Model):
    major = models.PositiveIntegerField()
    student_id = models.CharField(max_length=10)
    semester = models.CharField(max_length=1)
    course_name = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    graduate = models.CharField(max_length=3)
    course_id = models.CharField(max_length=10)
    front_code = models.PositiveIntegerField()
    back_code = models.PositiveIntegerField()
