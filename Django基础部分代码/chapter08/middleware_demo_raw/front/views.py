from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.generic import View
from .models import User
from django.contrib import messages

def index(request):
    return HttpResponse('index')

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username,password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect(reverse('index'))
        else:
            messages.info(request,'用户名或密码错误！')
            return redirect(reverse('login'))