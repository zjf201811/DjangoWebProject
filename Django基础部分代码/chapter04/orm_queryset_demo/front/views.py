from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author,BookOrder,Publisher
from django.db.models.manager import Manager
from django.db.models.query import QuerySet
from django.db.models import Q,F,Count,Prefetch
from django.db import connection

def index(request):
    print(type(Book.objects))
    return HttpResponse("index")

def index2(request):
    # 链式调用
    # books = Book.objects.filter(id__gte=2).exclude(id=3)
    # for book in books:
    #     print(book)
    books = Book.objects.annotate(author_name=F("author__name"))
    for book in books:
        print('%s/%s' % (book.name,book.author_name))
    print(connection.queries)
    return HttpResponse("index2")

def index3(request):
    # 1. 根据create_time从小到大进行排序
    # orders = BookOrder.objects.order_by("create_time")
    # 2. 根据create_time从大到小进行排序
    # orders = BookOrder.objects.order_by("-create_time")
    # 3. 首先根据create_time从大到小进行排序，如果create_time是一样的
    # 那么根据price从大到小进行排序
    # orders = BookOrder.objects.order_by("-create_time",'-price')
    # 4. 要根据订单的图书的评分来进行排序(从小到大)
    # orders = BookOrder.objects.order_by("-book__rating")
    # orders = BookOrder.objects.order_by("create_time").order_by("price")
    # orders = BookOrder.objects.all()
    # for order in orders:
    #     print("%s/%s/%s"%(order.id,order.create_time,order.price))

    # 5. 提取图书数据，根据图书的销量进行排序（从大到小进行排序）
    books = Book.objects.annotate(order_nums=Count("bookorder")).order_by("-order_nums")
    for book in books:
        print('%s/%s'%(book.name,book.order_nums))
    return HttpResponse("index3")

def index4(request):
    # books = Book.objects.values("id","name",author=F("author__name"))
    # books = Book.objects.values('id','name',order_nums=Count("bookorder"))
    # books = Book.objects.values()
    books = Book.objects.values_list('id',"name",flat=True)
    print(type(books))
    for book in books:
        print(book)
    return HttpResponse("index4")

def index5(request):
    books = Book.objects.all()
    print(books)
    for book in books:
        print(book.name)
    return HttpResponse("index5")

def index6(request):
    # books = Book.objects.all()
    # books = Book.objects.select_related("author","publisher")
    books = Book.objects.select_related("bookorder")
    for book in books:
        print(book.author.name)
        print(book.publisher.name)
    print(connection.queries)
    return HttpResponse("index6")

def index7(request):
    # books = Book.objects.prefetch_related("bookorder_set")
    # for book in books:
    #     print('='*30)
    #     print(book.name)
    #     orders = book.bookorder_set.all()
    #     for order in orders:
    #         print(order.id)

    # books = Book.objects.prefetch_related("author")
    # for book in books:
    #     print(book.author.name)
    prefetch = Prefetch("bookorder_set",queryset=BookOrder.objects.filter(price__gte=90))
    books = Book.objects.prefetch_related(prefetch)
    for book in books:
        print('='*30)
        print(book.name)
        orders = book.bookorder_set.all()
        for order in orders:
            print(order.id)

    print(connection.queries)
    return HttpResponse("index7")

def index8(request):
    # books = Book.objects.defer("name")
    # for book in books:
    #     print(book.name)
        # print(type(book))
    books = Book.objects.only('name')
    for book in books:
        print('%s/%s'%(book.id,book.price))
    print(connection.queries)
    return HttpResponse("index8")


def index9(request):
    book = Book.objects.get(id=5)
    print(book)
    print(connection.queries)
    return HttpResponse("index9")

def index10(request):
    # publisher = Publisher(name='知了出版社')
    # publisher.save()
    publisher = Publisher.objects.create(name='知了课堂出版社')
    print(connection.queries)
    return HttpResponse("index10")

def index11(request):
    # result = Publisher.objects.get_or_create(name='知了abc出版社')
    # print(result[0])

    publisher = Publisher.objects.bulk_create([
        Publisher(name='123出版社'),
        Publisher(name='abc出版社'),
    ])
    return HttpResponse("index11")

def index12(request):
    # books = Book.objects.all()
    # print(len(books))
    # count = Book.objects.count()
    # print(count)
    result = Book.objects.filter(name='三国演义').exists()
    print(result)
    print(connection.queries)
    return HttpResponse("index12")

def index13(request):
    books = Book.objects.filter(bookorder__price__gte=80).order_by('bookorder__price').distinct()
    for book in books:
        print(book)
    print(connection.queries)
    return HttpResponse("index13")

def index14(request):
    # Book.objects.update(price=F("price")+5)
    # books = Book.objects.all()
    # for book in books:
    #     book.price = book.price + 5
    #     book.save()
    Author.objects.filter(id__gte=3).delete()
    return HttpResponse('index14')


def index15(request):
    # 0,1 = [0:2]  1-1 = 1
    books = Book.objects.all()[1:2]
    for book in books:
        print(book)
    print(connection.queries)
    return HttpResponse("index15")

def index16(request):
    books = Book.objects.all()
    if books:
        print('有数据')
    print(connection.queries)
    return HttpResponse("index16")