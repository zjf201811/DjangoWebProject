from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

def index(request):
    # 1. 使用ORM添加一条数据到数据库中
    # book = Book(name='西游记',author='吴承恩',price=100)
    # book.save()

    # 2. 查询
    # 2.1. 根据主键进行查找
    # primary key
    # book = Book.objects.get(pk=2)
    # print(book)
    # 2.2. 根据其他条件进行查找
    # books = Book.objects.filter(name='三国演义').first()
    # print(books)

    # 3. 删除数据
    # book = Book.objects.get(pk=1)
    # book.delete()

    # 4. 修改数据
    book = Book.objects.get(pk=2)
    book.price = 200
    book.save()
    return HttpResponse("图书添加成功！")
