from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Person,Author
from django.utils.timezone import now,localtime

def index(request):
    # article = Article(removed=False)
    # article.save()
    # article = Article()
    # article.save()
    # import pytz
    # from datetime import datetime
    # now = datetime.now()  # 这是一个navie类型的时间
    # utc_timezone = pytz.timezone("UTC")  # 定义UTC的时区对象
    # utc_now = now.astimezone(utc_timezone)  # 将当前的时间转换为UTC时区的时间
    # article = Article(title='aaa')
    # article.save()
    article = Article.objects.get(pk=3)
    article.title = '111'
    article.save()
    # article = Article.objects.get(pk=1)
    # create_time = article.create_time
    # print('='*30)
    # print(create_time)
    # print(localtime(create_time))
    # print('='*30)
    return HttpResponse("success")
    # return render(request,'index.html',context={'create_time':create_time})


def email_view(request):
    p = Person(email='aaaa')
    p.save()
    return HttpResponse('success')


def null_text_field_view(request):
    author = Author(username='zhiliao')
    author.save()
    return HttpResponse("success")

def unique_view(request):
    author = Author(username='aaa',telephone='222')
    author.save()
    return HttpResponse("success")

def order_view(request):
    authors = Author.objects.all()
    for author in authors:
        # <Author object>
        print(author)
    return HttpResponse('success')