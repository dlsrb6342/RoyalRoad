from django.shortcuts import render
from django.shortcuts import get_object_or_404
from myapp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from haystack.query import SearchQuerySet


class MainView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'myapp/base.html'

    def get(self, request):
        return Response()
        

class DataView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'myapp/search.html'

    def get(self, request):
        course_code = request.data.get('course_code')
        course = get_object_or_404(Course, code=course_code)
        course_name = course.name
        data = dict()

        data['course_name'] = course_name
        data['0'] = dataQuery(course_name, 0)
        data['1'] = dataQuery(course_name, 1)
        data['2'] = dataQuery(course_name, 2)
        data['3'] = dataQuery(course_name, 3)
        data['-1'] = dataQuery(course_name, -1)
        data['-2'] = dataQuery(course_name, -2)
        data['-3'] = dataQuery(course_name, -3)

        return Response(data)

    def post(self, request):
        course_code = request.data.get('course_code')
        function_code = request.data.get('function_code')

        course = get_object_or_404(Course, code=course_code)
        course_name = course.name
        data = dict()

        data['course_name'] = course_name

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
        search_string = request.data.get('q')
        search_result = search(search_string)

        return Response({'data': search_result, 'flag': True})


def search(q):
    sqs_name = SearchQuerySet().autocomplete(name__startswith=q)[:7]
    sqs_code = SearchQuerySet().autocomplete(code__startswith=q)[:7]

    suggestions = []

    for r in sqs_name:
        suggestions.append({ "code": r.code, "name": r.name })

    for r in sqs_code:
        suggestions.append({ "code": r.code, "name": r.name })

    return suggestions
