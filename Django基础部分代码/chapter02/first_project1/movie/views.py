#encoding: utf-8
from django.http import HttpResponse

def movie(request):
    return HttpResponse("电影首页")