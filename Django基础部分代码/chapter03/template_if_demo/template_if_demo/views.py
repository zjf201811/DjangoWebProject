from django.shortcuts import render

def index(request):
    # context = {
    #     'age': 20
    # }
    context = {
        'heros':[
            '项羽',
            '程咬金'
        ]
    }
    return render(request ,'index.html',context=context)