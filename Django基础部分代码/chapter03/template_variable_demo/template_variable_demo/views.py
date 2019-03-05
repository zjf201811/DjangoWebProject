from django.shortcuts import render

class Person(object):
    def __init__(self,username):
        self.username = username

def index(request):
    # p = Person("张三")
    # context = {
    #     'person': p
    # }
    # context = {
    #     'person': {
    #         'username':'zhiliao',
    #     }
    # }
    # person.keys()
    context = {
        'persons': (
            '鲁班一号',
            '程咬金',
            '阿珂'
        )
    }
    return render(request,'index.html',context=context)