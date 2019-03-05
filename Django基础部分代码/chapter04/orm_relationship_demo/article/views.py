from django.shortcuts import render
from .models import Category,Article,Tag
from frontuser.models import FrontUser,UserExtension
from django.http import HttpResponse
from django.template.defaultfilters import mark_safe

def index(request):
    # category = Category(name='最新文章')
    # category.save()
    # article = Article(title='abc',content='111')
    # article.category = category
    # article.save()
    article = Article.objects.first()
    print(article.category.name)
    return HttpResponse('success')


def delete_view(request):
    category = Category.objects.get(pk=6)
    category.delete()
    return HttpResponse("delete success")

def one_to_many_view(request):
    # 1. 一对多的关联操作
    # article = Article(title='钢铁是怎样练成的',content='abc')
    # category = Category.objects.first()
    # author = FrontUser.objects.first()
    #
    # article.category = category
    # article.author = author
    #
    # article.save()
    #
    # return HttpResponse("success")

    # 2. 获取某个分类下所有的文章
    category = Category.objects.first()
    # RelatedManager
    # article = category.article_set.first()
    # print(article)

    # articles = category.articles.all()
    # for article in articles:
    #     print(article)

    article = Article(title='ccc',content='nnn')
    article.author = FrontUser.objects.first()

    category.articles.add(article,bulk=False)

    return HttpResponse("success")


def one_to_one_view(request):
    # user = FrontUser.objects.first()
    #
    # extension = UserExtension(school='清华')
    # extension.user = user
    # extension.save()

    # extension = UserExtension.objects.first()
    # print(extension.user)

    user = FrontUser.objects.first()
    print(user.userextension)

    return HttpResponse("success")

def many_to_many_view(request):
    # article = Article.objects.first()
    # tag = Tag(name='冷门文章')
    # tag.save()
    # article.tag_set.add(tag)

    # tag = Tag.objects.get(pk=1)
    # article = Article.objects.get(pk=3)
    # tag.articles.add(article)

    article = Article.objects.get(pk=1)
    tags = article.tags.all()
    for tag in tags:
        print(tag)

    return HttpResponse("success")