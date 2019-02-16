from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request, book_id, category_id):
    text = "书的id是%s,种类是%s"%(book_id,category_id)
    return HttpResponse(text)


def author_detail(request):
    author_id = request.GET.get('id')
    text = "作者的id是%s"%author_id
    return HttpResponse(text)


def publisher_detail(request,publisher_id):
    text = '出版社的id是%s'%publisher_id
    return HttpResponse(text)
