from django.http import HttpResponse


def hello_polls(request):
    return HttpResponse('Hi from polls')
