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
    course_id = serializers.IntegerField(required=False)
    pre_request_course_id = serializers.PrimaryKeyRelatedField(required=False, read_only=True, many=True)
    cilos = serializers.PrimaryKeyRelatedField(required=False, many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class CourseSearchSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(required=False)
    pre_request_course_id = serializers.PrimaryKeyRelatedField(required=False, read_only=True, many=True)
    cilos = serializers.PrimaryKeyRelatedField(required=False, many=True, read_only=True)

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


class CiloSearchSerializer(serializers.ModelSerializer):
    cilo_id = serializers.IntegerField(required=False)
    parent_cilos = serializers.CharField(required=False)
    child_cilos = serializers.CharField(required=False)

    class Meta:
        model = Cilo
        fields = '__all__'


class AssessmentSerializer(serializers.ModelSerializer):
    assessment_id = serializers.IntegerField(required=False)
    cilos = serializers.CharField(required=False)
    evaluation_method = serializers.JSONField()
    percentage = serializers.JSONField()
    cilos_arr = serializers.JSONField()

    class Meta:
        model = Assessment
        fields = '__all__'
