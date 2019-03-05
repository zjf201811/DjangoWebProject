from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

def index(request):
    if not request.GET.get('username'):
        return redirect(reverse('errors:400'))
    return HttpResponse('首页')

