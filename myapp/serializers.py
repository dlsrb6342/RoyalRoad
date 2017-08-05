from rest_framework import serializers
from myapp.models import *


class CourseSerializer(serializers.ModelSerializer):

	class Meta:
		model = Course
		fields = ('id', 'name', 'code', 'count')


class MajorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Major 
		fields = ('id', 'name', 'code')


class TakenSerializer(serializers.ModelSerializer):
	course = CourseSerializer(read_only=True)
	major = MajorSerializer(read_only=True)

	class Meta:
		model = Taken
		fields = ('id', 'major', 'student_id', 'credit', 'semester', 'professor', 'year', 'graduate', 'front_code', 'back_code', 'grade', 'course')


class TakenListSerializer(serializers.ModelSerializer):

	class Meta:
		model = TakenList
		fields = ('student_id', 'semester', 'course_list')


class DataSerializer(serializers.ModelSerializer):

	class Meta:
		model = Data 
		fields = ('rate', 'diff', 'taken_course', 'related_course')