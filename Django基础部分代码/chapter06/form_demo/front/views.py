from django.shortcuts import render
from django.views.generic import View
from .forms import MesssageBoardForm
from django.http import HttpResponse
from django.forms.utils import ErrorDict

class IndexView(View):
    def get(self,request):
        form = MesssageBoardForm()
        return render(request,'index.html',context={"form":form})

    def post(self,request):
        form = MesssageBoardForm(request.POST)
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
            print(form.errors.get_json_data())
            return HttpResponse('fail')