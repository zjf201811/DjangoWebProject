from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('CMS首页')
    else:
        currect_namespace = request.resolver_match.namespace
        return redirect(reverse("%s:login"%currect_namespace))


def login(request):
    return HttpResponse('CMS登录页面')


