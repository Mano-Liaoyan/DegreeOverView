from faker import Faker
from django.http import HttpResponseRedirect
from userdb.models import CourseDesigner


def index(request):
    # add_to_data_base()
    return HttpResponseRedirect('login-form/')  # Jump to login page


def add_to_data_base():
    fake = Faker()
    for i in range(1000):
        username = fake.user_name()
        password = fake.password(length=16)
        fullname = fake.name()

        CourseDesigner.objects.create(username=username, password=password, fullname=fullname)
        pass
