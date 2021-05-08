from userdb.models import Student, Lecturer, CourseDesigner
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'


class CourseDesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDesigner
        fields = '__all__'
