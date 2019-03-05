#encoding: utf-8
from django.http import HttpResponse

def book(request):
    return HttpResponse("图书首页")