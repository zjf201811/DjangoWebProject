from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        'value': '张三',
        'mytime': datetime(year=2018,month=2,day=7,hour=18,minute=55,second=0)
    }
    return render(request,'index.html',context=context)
