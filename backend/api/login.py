from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from userdb.models import User


def login_form(request):
    return render(request, 'login.html')


# receive the data
def login(request):
    request.encoding = 'utf-8'

    username = request.POST['username']
    password = request.POST['password']

    if username and password:
        try:
            if User.objects.get(username=username).password == password:  # this should be database identifier in the future
                data = {
                    'code': 0,
                    'message': 'Success!'
                }
            else:
                data = {
                    'code': 1002,
                    'message': 'Not correct username or password!'
                }
        except:
            data = {
                'code': 1002,
                'message': 'Not correct username or password!'
            }
    else:
        data = {
            'code': 1001,
            'message': 'Parameter incomplete!'
        }
    return JsonResponse(data)
