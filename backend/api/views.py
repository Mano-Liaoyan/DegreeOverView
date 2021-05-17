from django.db.models import Q
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from userdb.models import Student, Lecturer, CourseDesigner, Cilo
from userdb.models import Course
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer, LecturerSerializer, CourseDesignerSerializer, CourseSerializer, SearchSerializer, CiloSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # permission_classes = [permissions.IsAuthenticated]
    @action(methods=['POST'], detail=False)
    def login(self, request):
        s = request.data
        student = Student.objects.filter(username=s['username'])
        if student:
            if s['password'] == student[0].password:
                res_json = {
                    'code': 0,
                    'message': 'Success!'
                }
            else:
                res_json = {
                    'code': 1002,
                    'message': 'Not correct username or password!'
                }
        else:
            res_json = {
                'code': 1002,
                'message': 'Not correct username or password!'
            }
        return Response(res_json)


class LecturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Lecturers to be viewed or edited.
    """
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

    # permission_classes = [permissions.IsAuthenticated]
    @action(methods=['POST'], detail=False)
    def login(self, request):
        s = request.data
        lecturer = Lecturer.objects.filter(username=s['username'])
        if lecturer:
            if s['password'] == lecturer[0].password:
                res_json = {
                    'code': 0,
                    'message': 'Success!'
                }
            else:
                res_json = {
                    'code': 1002,
                    'message': 'Not correct username or password!'
                }
        else:
            res_json = {
                'code': 1002,
                'message': 'Not correct username or password!'
            }
        return Response(res_json)


class CourseDesignerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CourseDesigners to be viewed or edited.
    """
    queryset = CourseDesigner.objects.all()
    serializer_class = CourseDesignerSerializer

    # permission_classes = [permissions.IsAuthenticated]
    @action(methods=['POST'], detail=False)
    def login(self, request):
        s = request.data
        designer = CourseDesigner.objects.filter(username=s['username'])
        if designer:
            if s['password'] == designer[0].password:
                res_json = {
                    'code': 0,
                    'message': 'Success!'
                }
            else:
                res_json = {
                    'code': 1002,
                    'message': 'Not correct username or password!'
                }
        else:
            res_json = {
                'code': 1002,
                'message': 'Not correct username or password!'
            }
        return Response(res_json)


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Course to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SearchViewSet(viewsets.ViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # permission_classes = [permissions.IsAuthenticated]
    @action(methods=['GET'], detail=False)
    def course(self, request):
        s = request.data
        res = Course.objects.filter(Q(course_name__contains=s['keywords']) | Q(course_code__contains=s['keywords']))
        s_serializer = CourseSerializer(instance=res, many=True)
        # print(s_serializer.data)
        return Response(s_serializer.data)

    @action(methods=['GET'], detail=False)
    def cilo(self, request):
        s = request.data
        res = Cilo.objects.filter(Q(cilo_id__contains=s['keywords']) | Q(content__contains=s['keywords']))
        s_serializer = CiloSerializer(instance=res, many=True)
        # print(s_serializer.data)
        return Response(s_serializer.data)
