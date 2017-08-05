import csv 
from random import randint
from myapp.models import Taken, Major, Course, TakenList

def read_csv():
    with open('./utils/db.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        id = 0; time = ''; semester = 0; course_list = []; first = True
        for row in reader:
            if id != row['학번']:
                if not first:
                    TakenList.objects.create(
                        student_id = id,
                        semester = semester,
                        course_list = { 'data': course_list }
                    ).save()
                first = False; id = row['학번']; semester = 1; course_list = []
                time = row['연도'] + row['학기'] 
            elif row['학기'] == '1' or row['학기'] == '3':
                if time != row['연도'] + row['학기']: 
                    time = row['연도'] + row['학기']
                    TakenList.objects.create(
                        student_id = id,
                        semester = semester,
                        course_list = course_list
                    ).save()
                    semester += 1; course_list = []
            if row['졸업일자'] == 'NULL':
                graduate = None
            else:
                if row['졸업일자'][5:7] == '02':
                    graduate = row['졸업일자'][2:4] + '1'
                else:
                    graduate = row['졸업일자'][2:4] + '2'
            grade = make_grade()
            course = Course.objects.get_or_create(name=row['과목명'], code=row['과목번호'])[0]
            course.count += 1
            course.save()
            Taken.objects.create(
                semester = semester,
                major = Major.objects.get(name=row['학과']),
                student_id = row['학번'][2:],
                credit = int(row['학']),
                course = course, 
                professor = row['교수명'],
                year = int(row['연도']),
                front_code = row['전산코드'].split('.')[0],
                back_code = row['전산코드'].split('.')[1],
                graduate = graduate,
                grade = grade
            ).save()
            course_list.append({
                'course_name': row['과목명'],
                'grade': grade,
                'credit': int(row['학'])
            })
        

def make_grade():
    a = randint(1, 10)
    choice = [-0.3, 0, 0.3]
    b = randint(0, 2)
    if a < 4:
        return 4 + choice[b]
    elif 4 <= a < 8:
        return 3 + choice[b]
    elif 8<= a < 10:
        return 2 + choice[b]
    else:
        return 1 + choice[b]




