from django.shortcuts import render
from .forms import MyForm
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import Article

def save_file(file):
    with open('somefile.txt','wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        form = MyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            print(form.get_errors())
            return HttpResponse('fail')