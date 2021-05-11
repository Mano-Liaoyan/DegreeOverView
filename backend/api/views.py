from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from userdb.models import Student, Lecturer, CourseDesigner
from userdb.models import Course, Cilo, Assessment
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer, LecturerSerializer, CourseDesignerSerializer
from .serializers import CourseSerializer, CiloSerializer, AssessmentSerializer


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

    @action(methods=['POST'], detail=False)
    def login(self, request):
        lec = request.data
        lecturer = Lecturer.objects.filter(username=lec['username'])
        if Lecturer:
            if lec['password'] == lecturer[0].password:
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

    @action(methods=['POST'], detail=False)
    def login(self, request):
        cd = request.data
        course_designer = CourseDesigner.objects.filter(username=cd['username'])
        if Lecturer:
            if cd['password'] == course_designer[0].password:
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


class CiloViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Course to be viewed or edited.
    """
    queryset = Cilo.objects.all()
    serializer_class = CiloSerializer


class AssessmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Course to be viewed or edited.
    """
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
