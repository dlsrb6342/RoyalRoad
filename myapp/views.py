from django.shortcuts import render
from django.shortcuts import get_object_or_404
from myapp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class DataView(APIView):
    def post(self, request):
        course_code = request.data.get('course_code')
        function_code = request.data.get('function_code')

        course = get_object_or_404(Course, code=course_code)
        course_name = course.name
        data = dict()

        if function_code == 'after':
            data['0'] = dataQuery(course_name, 0)
            data['1'] = dataQuery(course_name, 1)
            data['2'] = dataQuery(course_name, 2)
            data['3'] = dataQuery(course_name, 3)
        elif function_code == 'before':
            data['0'] = dataQuery(course_name, 0)
            data['-1'] = dataQuery(course_name, -1)
            data['-2'] = dataQuery(course_name, -2)
            data['-3'] = dataQuery(course_name, -3)
        elif function_code == 'whole':
            data['0'] = dataQuery(course_name, 0)
            data['1'] = dataQuery(course_name, 1)
            data['2'] = dataQuery(course_name, 2)
            data['3'] = dataQuery(course_name, 3)
            data['-1'] = dataQuery(course_name, -1)
            data['-2'] = dataQuery(course_name, -2)
            data['-3'] = dataQuery(course_name, -3)

        return Response(data)


def dataQuery(course_name, diff):
    datas = list()
    data = Data.objects.filter(taken_course=course_name, diff=diff)[:4]
    for d in data:
        datas.append(d)

    return DataSerializer(datas, many=True).data

class SearchView(APIView):
    def post(self, request):
        search_string = request.data.get('search_string')
        search_result = search(search_string)

        return Response({'data': search_result})
