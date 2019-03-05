# ORM对数据库的基本操作：

## 添加数据：
只要使用ORM模型创建一个对象。然后再调用这个ORM模型的`save`方法就可以保存了。
示例代码如下：
```python
book = Book(name='西游记',author='吴承恩',price=100)
book.save()
```


## 查找数据：
所有的查找工作都是使用模型上的`objects`属性来完成的。当然也可以自定义查询对象。这部分功能会在后面讲到。
1. 根据主键进行查找：使用主键进行查找。可以使用`objects.get`方法。然后传递`pk=xx`的方式进行查找。示例代码如下：
    ```python
    book = Book.objects.get(pk=2)
    ```
2. 根据其他字段进行查找：可以使用`objects.filter`方法进行查找。示例代码如下：
    ```python
    books = Book.objects.filter(name='三国演义')
    ```
    使用`filter`方法返回来的是一个`QuerySet`对象。这个对象类似于列表。我们可以使用这个对象的`first`方法来获取第一个值。


## 删除数据：
首先查找到对应的数据模型。然后再执行这个模型的`delete`方法即可删除。示例代码如下：
```python
book = Book.objects.get(pk=1)
book.delete()
```


## 修改数据：
首先查找到对应的数据模型。然后修改这个模型上的属性的值。再执行`save`方法即可修改完成。示例代码如下：
```python
    book = Book.objects.get(pk=2)
    book.price = 200
    book.save()
```
