from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author,BookOrder
from django.db.models import Avg,Count,Max,Min,Sum,F,Q
from django.db import connection


def index(request):
    # 获取所有图书的定价的平均价
    result = Book.objects.aggregate(avg=Avg("price"))
    print(result)
    # QuerySet
    # print(result.query)
    print(connection.queries)
    return HttpResponse("index")

def index2(request):
    # 我要获取每一本图书销售的平均价格
    # result = Book.objects.aggregate(avg=Avg("bookorder__price"))
    # print(result)
    # print(connection.queries)
    print('='*40)
    books = Book.objects.annotate(avg=Avg("bookorder__price"))
    for book in books:
        print('%s/%s'%(book.name,book.avg))
    print(connection.queries)
    return HttpResponse("index2")

def index3(request):
    # book表中总共有多少本书（book表中总共有多少个id）
    # result = Book.objects.aggregate(book_nums=Count("id"))
    # print(result)
    # print(connection.queries)

    # 要统计作者表中总共有多少个不同的邮箱
    # result = Author.objects.aggregate(email_nums=Count('email',distinct=True))
    # print(result)
    # print(connection.queries)

    # annotate
    # 统计每本书的销量
    books = Book.objects.annotate(book_nums=Count("bookorder"))
    for book in books:
        print('%s/%s' % (book.name,book.book_nums))
    print(connection.queries)
    return HttpResponse("index3")

def index4(request):
    # result = Author.objects.aggregate(max=Max("age"),min=Min("age"))
    # print(result)
    # print(connection.queries)

    # 获取每一本图书售卖时候的最大价格以及最小价格
    books = Book.objects.annotate(max=Max("bookorder__price"),min=Min("bookorder__price"))
    for book in books:
        print('%s/%s/%s'%(book.name,book.max,book.min))
    print(connection.queries)
    return HttpResponse("index4")

def index5(request):
    # 1. 求所有图书的销售总额
    # result = BookOrder.objects.aggregate(total=Sum('price'))
    # print(result)
    # print(connection.queries)

    # 2. 每一本图书的销售总额
    # books = Book.objects.annotate(total=Sum("bookorder__price"))
    # for book in books:
    #     print("%s/%s"%(book.name,book.total))
    # print(connection.queries)

    # 3. 先求2018年度，销售总额
    # result = BookOrder.objects.filter(create_time__year=2018).aggregate(total=Sum('price'))
    # print(result)
    # print(connection.queries)

    # 4. 求每一本图书在2018年度的销售总额
    books = Book.objects.filter(bookorder__create_time__year=2018).annotate(total=Sum("bookorder__price"))
    for book in books:
        print("%s/%s"%(book.name,book.total))
    print(connection.queries)
    return HttpResponse('index5')

def index6(request):
    # 给每一本图书的售价增加10元
    # Book.objects.update(price=F("price")+10)
    # print(connection.queries[-1])
    authors = Author.objects.filter(name=F("email"))
    for author in authors:
        print('%s/%s'%(author.name,author.email))
    print(connection.queries[-1])

    return HttpResponse("index6")

def index7(request):
    # 1. 获取价格大于100，并且评分在4.85分以上的图书
    # books = Book.objects.filter(price__gte=100,rating__gte=4.85)
    # books = Book.objects.filter(Q(price__gte=100)&Q(rating__gte=4.85))

    # 2. 获取价格低于100元，或者评分低于4分的图书
    # books = Book.objects.filter(Q(price__lt=100) | Q(rating__lt=4))

    # 3. 获取价格大于100，并且图书名字中不包含”传“字的图书
    books = Book.objects.filter(Q(price__gte=100)&~Q(name__icontains='传'))
    for book in books:
        print("%s/%s/%s"%(book.name,book.price,book.rating))
    print(connection.queries[-1])
    return HttpResponse("index7")