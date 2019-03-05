from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category
from datetime import datetime,time
from django.utils.timezone import make_aware

def index(request):
    # 在windows操作系统上，mysql的排序规则（collation）无论是什么
    # 都是大小写不敏感的
    # 在Linux操作系统上，Mysql的排序规则（collation）是utf8_bin
    # 那么就是大小写敏感的
    # article = Article.objects.filter(title__exact="Hello world")
    # article = Article.objects.filter(title__exact=None)
    # like hello hello
    # LIKE和=：大部分情况下都是等价的，只有少数情况下是不等价的。
    # exict和iexact：他们的区别其实就是LIKE和=的区别，因为exact会被翻译成=，而iexact会被翻译成LIKE。
    article = Article.objects.filter(title__iexact="hello world")
    print(article.query)
    print(article)
    return HttpResponse("success")

def index1(request):
    article = Article.objects.get(pk=1)
    print(article.query)
    return HttpResponse("success")


def index2(request):
    result = Article.objects.filter(title__icontains='hello')
    print(result.query)
    print(result)
    return HttpResponse("success")

def index3(request):
    # 查找id为1,2,3的文章的分类
    # articles = Article.objects.filter(id__in=[1,2,3])
    # for article in articles:
    #     print(article)

    # categories = Category.objects.filter(articles__in=[1,2,3])
    # for category in categories:
    #     print(category)

    # 所有标题中包含hello的分类
    articles = Article.objects.filter(title__icontains='hello')
    categories = Category.objects.filter(articles__in=articles)
    for cateogry in categories:
        print(cateogry)

    print(categories.query)
    return HttpResponse("success")

def index4(request):
    # 查找id大于2的所有文章
    # gt：greater than
    # gte：greater than equal
    # lt：lower than
    articles = Article.objects.filter(id__lte=3)
    print(articles)
    print(articles.query)
    return HttpResponse("index4")

def index5(request):
    # articles = Article.objects.filter(title__istartswith="hello")
    # print(articles.query)
    # print(articles)
    articles = Article.objects.filter(title__endswith="hello")
    print(articles.query)
    print(articles)
    return HttpResponse("index5")

def index6(request):
    start_time = make_aware(datetime(year=2018,month=4,day=4,hour=17,minute=0,second=0))
    end_time = make_aware(datetime(year=2018,month=4,day=4,hour=18,minute=0,second=0))
    articles = Article.objects.filter(create_time__range=(start_time,end_time))
    print(articles.query)
    print(articles)
    return HttpResponse("index6")

def index7(request):
    # articles = Article.objects.filter(create_time__date=datetime(year=2018,month=4,day=4))
    # articles = Article.objects.filter(create_time__year__gte=2018)
    # articles = Article.objects.filter(create_time__week_day=4)
    start_time = time(hour=17,minute=10,second=27)
    end_time = time(hour=17,minute=10,second=28)
    articles = Article.objects.filter(create_time__time__range=(start_time,end_time))
    print(articles.query)
    print(articles)
    return HttpResponse("index7")

def index8(request):
    # articles = Article.objects.filter(create_time__isnull=False)
    articles = Article.objects.filter(title__iregex=r"^hello")
    print(articles.query)
    print(articles)
    return HttpResponse("index8")

