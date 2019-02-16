# Author:ZJF
from django.shortcuts import render

def index(request):
    context={
        "one":[1,2,3,4,5,8,7,8,9],
        "two":'2',
    }
    return render(request, 'index.html', context=context)