from django.db.models import Q, Count
from rest_framework.decorators import action
from rest_framework.response import Response
from userdb.models import Student, Lecturer, CourseDesigner, Cilo, Course
from rest_framework import viewsets
from .serializers import StudentSerializer, LecturerSerializer, CourseDesignerSerializer, CourseSerializer, CiloSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


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


class CourseSearchViewSet(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('course_name', 'course_code', 'academic_start_year', 'program',
                     'type', 'cilos_id__content', 'pre_request_course_id_id__course_name')
    pass


class CiloSearchViewSet(ListAPIView):
    queryset = Cilo.objects.all()
    serializer_class = CiloSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('cilo_id', 'content')
    pass

# class SearchViewSet(viewsets.ViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
# 
#     # permission_classes = [permissions.IsAuthenticated]
#     @action(methods=['GET'], detail=False)
#     def course(self, request):
#         s = SearchSerializer(data=request.data)
#         if s.is_valid():
#             keywords = s['keywords'].value
#             res = Course.objects.filter(Q(course_name__contains=keywords) | Q(course_code__contains=keywords))
#             s_serializer = CourseSerializer(instance=res, many=True)
#             final_res = {'results': s_serializer.data, 'count': res.count()}
#             return Response(final_res)
#         else:
#             return Response(s.errors)
# 
#     @action(methods=['GET'], detail=True)
#     def cilo(self, request, *args, **kwargs):
#         s = SearchSerializer(data=request.data)
#         print('args: ', args)
#         if s.is_valid():
#             keywords = s['keywords'].value
#             res = Cilo.objects.filter(Q(cilo_id__contains=keywords) | Q(content__contains=keywords))
#             s_serializer = CiloSerializer(instance=res, many=True)
#             final_res = {'results': s_serializer.data, 'count': res.count()}
#             return Response(final_res)
#         else:
#             return Response(s.errors)
