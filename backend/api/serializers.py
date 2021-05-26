from userdb.models import Student, Lecturer, CourseDesigner
from userdb.models import Course, Cilo
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
    course_id = serializers.IntegerField(required=False)

    class Meta:
        model = Course
        fields = '__all__'


class CiloSerializer(serializers.ModelSerializer):
    cilo_id = serializers.IntegerField(required=False)
    parent_cilos = serializers.CharField(required=False)
    child_cilos = serializers.CharField(required=False)

    class Meta:
        model = Cilo
        fields = '__all__'
