from django.shortcuts import render
from .forms import MessageBoardForm
from django.views.generic import View
from django.http import HttpResponse

class IndexView(View):
    def get(self,request):
        form = MessageBoardForm()
        return render(request,'index.html',{'form':form})

    def post(self,request):
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            print('='*30)
            print(title)
            print(content)
            print(email)
            print(reply)
            print('='*30)
            return HttpResponse('success')
        else:
            print(form.errors)
            return HttpResponse('fail')
