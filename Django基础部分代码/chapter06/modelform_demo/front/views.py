from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddBookForm,RegisterForm
from django.views.decorators.http import require_POST

def index(request):
    return HttpResponse('index')

def add_book(request):
    form = AddBookForm(request.POST)
    if form.is_valid():
        # title = form.cleaned_data.get('title')
        # page = form.cleaned_data.get("page")
        # price = form.cleaned_data.get("price")
        # print('title:%s'%title)
        # print('page:%s'%page)
        # print('price:%s'%price)
        form.save()
        return HttpResponse('success')
    else:
        print(form.errors.get_json_data())
        return HttpResponse('FAIL')

@require_POST
def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.password = form.cleaned_data.get('pwd1')
        user.save()
        return HttpResponse('success')
    else:
        return HttpResponse('fail')
