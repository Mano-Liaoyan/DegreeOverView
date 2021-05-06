from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# receive the data
def search(request):
    request.encoding = 'utf-8'

    keywords = request.GET['keywords']

    # TODO change to database expression in the future

    if 'keywords' in request.GET and keywords:
        data = {
            'code': 0,
            'message': 'Search success!'
        }
    else:
        data = {
            'code': 1001,
            'message': 'No keywords!'
        }
    return JsonResponse(data)
