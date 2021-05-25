from faker import Faker
from django.http import HttpResponseRedirect
from userdb.models import CourseDesigner, Student, Cilo, Assessment, Course


def index(request):
    # add_to_data_base()
    # add_cilo_to_data_base()
    # add_as_to_data_base()
    # add_course_to_data_base()
    return HttpResponseRedirect('api/')  # Jump to login page


def add_to_data_base():
    fake = Faker()
    for i in range(1000):
        username = fake.user_name()
        password = fake.password(length=16)
        fullname = fake.name()

        Student.objects.create(username=username, password=password, fullname=fullname)
        pass


def add_cilo_to_data_base():
    fake = Faker()
    for i in range(1000):
        content = fake.text(max_nb_chars=60, ext_word_list=None)

        Cilo.objects.create(content=content)
        pass


def add_as_to_data_base():
    fake = Faker()
    for i in range(100):
        evaluation_method = [fake.word(), fake.word(), fake.word(), fake.word()]
        percentage = ["10%", "20%", "30%", "40%"]
        # Assessment.objects.create(evaluation_method=evaluation_method, percentage=percentage)
        _as = Assessment.objects.get(assessment_id=i + 1)

        cilo1 = Cilo.objects.filter(cilo_id=fake.random_int(min=1, max=1000))
        cilo2 = Cilo.objects.filter(cilo_id=fake.random_int(min=1, max=1000))
        # cilo3 = Cilo.objects.filter(cilo_id=fake.random_int(min=1, max=1000))
        # cilo4 = Cilo.objects.filter(cilo_id=fake.random_int(min=1, max=1000))
        _as.cilos.add(*cilo1)
        _as.cilos.add(*cilo2)
        # _as.save()
        # _as.cilos.add(cilo2)
        # _as.cilos.add(cilo3)
        # _as.cilos.add(cilo4)
        pass


def add_course_to_data_base():
    course_name = "Operating System"
    course_code = "FS1001"
    academic_start_year = 2019
    program = "DST"
    type = "MR"
    cilos = Cilo.objects.filter(cilo_id=1)
    assessment = Assessment.objects.get(assessment_id=1)
    pre_request_course_id = None

    # course = Course.objects.create(course_name=course_name, course_code=course_code,
    #                                academic_start_year=academic_start_year, program=program,
    #                                type=type, assessment=assessment)

    course = Course.objects.get(course_id=1)
    course.cilos.add(*cilos)
    # course.cilos.set(pre_request_course_id)
    # course.pre_request_course_id.add(*cilos)
    # course.assessment.add(*assessment)
    # course.save()
    pass
