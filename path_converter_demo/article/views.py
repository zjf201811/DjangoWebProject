from django.shortcuts import render,reverse
from django.http import HttpResponse
# Create your views here.

def article(requiest):
    return HttpResponse("文章首页")

def article_list(request,categories):
    print('categories:%s'%categories)
    print(reverse('list',kwargs={'categories':categories}))
    text = "您填写的分类是，%s"%categories
    return HttpResponse(text)

def article_detail(request,article_id):
    reverse('detail',kwargs={'article_id':article_id})
    print(type(article_id))
    return HttpResponse('文章详情')
