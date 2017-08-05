from myapp.models import *
import queue
from datetime import datetime


def main():
    diffs = [-3, -2, -1, 0, 1, 2, 3]
    for course in Course.objects.all():
        now = datetime.now()
        if course.count < 15 :
            continue

        taken_course_name = course.name

        for diff in diffs:
            print(taken_course_name, diff)
            occurence = dict()  # course를 듣고 diff 학기 후에 (들은 과목, 횟수)
            count = 0

            for taken in Taken.objects.filter(course=course):
                student_id = '20' + taken.student_id
                semester = taken.semester

                try:
                    takenlist = TakenList.objects.get(student_id=student_id, semester=semester + diff)
                    count += 1
                except:
                    continue

                for course_data in takenlist.course_list:
                    course_name = course_data['course_name']
                    if taken_course_name == course_name:
                        continue

                    try:
                        occurence[course_name] += 1
                    except:
                        occurence[course_name] = 1

            rate = queue.PriorityQueue()
            for name in occurence:
                rate.put((-1 * occurence[name] / count, name))
            while not rate.empty():
                r = rate.get()
                if r[0] * -1 < 0.1: 
                    continue
                Data.objects.create(rate=r[0] * -1, diff=diff, taken_course=taken_course_name, related_course=r[1])


def add_code():
    for data in Data.objects.all():
        taken_course_name = data.taken_course
        related_course_name = data.related_course
        taken_course = Course.objects.filter(name=taken_course_name)[0]
        related_course = Course.objects.filter(name=related_course_name)[0]

        data.taken_course_code = taken_course.code
        data.related_course_code = related_course.code
        data.save()
