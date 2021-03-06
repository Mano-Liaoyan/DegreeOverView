from django.db.models import Q, Count
from rest_framework.decorators import action
from rest_framework.response import Response
from userdb.models import Student, Lecturer, CourseDesigner, Cilo, Course, Assessment
from rest_framework import viewsets
from .serializers import StudentSerializer, LecturerSerializer, CourseDesignerSerializer, CourseSerializer, CiloSerializer, AssessmentSerializer, \
    CiloSearchSerializer, CourseSearchSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'  # items per page


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

    def create(self, request, *args, **kwargs):
        print('daaaaaaaaaa', request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        assessment = Assessment.objects.get(assessment_id=data['assessment'])
        Course.objects.create(course_name=data['course_name'], course_code=data['course_code'], academic_start_year=data['academic_start_year'],
                              program=data['program'], type=data['type'], assessment=assessment)
        course = Course.objects.filter(course_name=data['course_name']).first()
        print('sssssss', data['cilos'])
        course.cilos.set(data['cilos'])
        # course.pre_request_course_id.set(data['pre_request_course_id'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    @action(methods=['GET'], detail=False)
    def get_all_program(self, request):
        courses = Course.objects.all()
        programs = courses.values('program').distinct().order_by('program')
        program_list = []
        for program in programs:
            program_list.append(program['program'])
        res_json = {
            'programs': program_list
        }
        return Response(res_json)


class CiloViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Cilo to be viewed or edited.
    """
    queryset = Cilo.objects.all()
    serializer_class = CiloSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        data = serializer.data
        Cilo.objects.create(content=data['content'])
        cilo = Cilo.objects.get(content=data['content'])
        if data['parent_cilos']:
            cilo.parent_cilos.set(data['parent_cilos'])
        headers = self.get_success_headers(serializer.data)
        data['cilo_id'] = cilo.cilo_id
        return Response(data, status=201, headers=headers)


class AssessmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Cilo to be viewed or edited.
    """
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        data = serializer.data
        Assessment.objects.create(evaluation_method=data['evaluation_method'], percentage=data['percentage'], cilos_arr=data['cilos_arr'])
        ass = Assessment.objects.get(Q(evaluation_method=data['evaluation_method']) & Q(percentage=data['percentage']) & Q(cilos_arr=data['cilos_arr']))
        # ass.cilos.set(data['cilos'])
        headers = self.get_success_headers(serializer.data)
        data['assessment_id'] = ass.assessment_id
        return Response(data, status=201, headers=headers)


class CourseSearchViewSet(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSearchSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('course_id', 'course_name', 'course_code', 'academic_start_year', 'program', 'type')
    pass


class CiloSearchViewSet(ListAPIView):
    queryset = Cilo.objects.all()
    serializer_class = CiloSearchSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('cilo_id', 'content')
    pass
