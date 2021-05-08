from django.shortcuts import render
from userdb.models import Student, Lecturer, CourseDesigner
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer, LecturerSerializer, CourseDesignerSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class LecturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Lecturers to be viewed or edited.
    """
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class CourseDesignerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CourseDesigners to be viewed or edited.
    """
    queryset = CourseDesigner.objects.all()
    serializer_class = CourseDesignerSerializer
