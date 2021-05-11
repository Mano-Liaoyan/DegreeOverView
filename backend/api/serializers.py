from userdb.models import Student, Lecturer, CourseDesigner
from userdb.models import Course, Cilo, Assessment
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


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cilo
        fields = '__all__'


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'
