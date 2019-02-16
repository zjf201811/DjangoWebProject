# Author:ZJF
from django.shortcuts import render

class Person(object):
    def __init__(self,username):
        self.username = username


def index(request):
    # P = Person('zhiliao')
    abc='lishuai'
    context={
        'person':[
            "1","2","3",
        ],"abc":1234
    }
    return render(request,'index.html',context=context)