from django.http import HttpResponse


# def hello(request):
#     return HttpResponse("Hello World!")
from django.shortcuts import render


def hello(request):
    context = {"hello": "Hello World!"}
    return render(request, 'hello.html', context)

