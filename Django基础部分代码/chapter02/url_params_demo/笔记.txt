# url传递参数：

## url映射：
1. 为什么会去urls.py文件中寻找映射呢？
是因为在`settings.py`文件中配置了`ROOT_URLCONF`为`urls.py`。所有django会去`urls.py`中寻找。
2. 在`urls.py`中我们所有的映射，都应该放在`urlpatterns`这个变量中。
3. 所有的映射不是随便写的，而是使用`path`函数或者是`re_path`函数进行包装的。

## url传参数：
1. 采用在url中使用变量的方式：在path的第一个参数中，使用`<参数名>`的方式可以传递参数。然后在视图函数中也要写一个参数，视图函数中的参数必须和url中的参数名称保持一致，不然就找不到这个参数。另外，url中可以传递多个参数。
2. 采用查询字符串的方式：在url中，不需要单独的匹配查询字符串的部分。只需要在视图函数中使用`request.GET.get('参数名称')`的方式来获取。示例代码如下：
    ```python
    def author_detail(request):
        author_id = request.GET['id']
        text = '作者的id是：%s' % author_id
        return HttpResponse(text)
    ```
    因为查询字符串使用的是`GET`请求，所以我们通过`request.GET`来获取参数。并且因为`GET`是一个类似于字典的数据类型，所有获取值跟字典的方式都是一样的。

## url参数的转换器：
1. str：除了斜杠`/`以外所有的字符都是可以的。
2. int：只有是一个或者多个的阿拉伯数字。
3. path：所有的字符都是满足的。
4. uuid：只有满足`uuid.uuid4()`这个函数返回的字符串的格式。
5. slug：英文中的横杆或者英文字符或者阿拉伯数字或者下划线才满足。
