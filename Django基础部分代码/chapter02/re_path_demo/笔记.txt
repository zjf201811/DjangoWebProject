# re_path笔记：
1. re_path和path的作用都是一样的。只不过`re_path`是在写url的时候可以用正则表达式，功能更加强大。
2. 写正则表达式都推荐使用原生字符串。也就是以`r`开头的字符串。
3. 在正则表达式中定义变量，需要使用圆括号括起来。这个参数是有名字的，那么需要使用`?P<参数的名字>`。然后在后面添加正则表达式的规则。示例代码如下：
    ```python
    from django.urls import re_path
    from . import views

    urlpatterns = [
        # r""：代表的是原生字符串（raw）
        re_path(r'^$',views.article),
        # /article/list/<year>/
        re_path(r"^list/(?P<year>\d{4})/$",views.article_list),
        re_path(r"^list/(?P<month>\d{2})/$",views.article_list_month)
    ]
    ```
4. 如果不是特别要求。直接使用`path`就够了，省的把代码搞的很麻烦（因为正则表达式其实是非常晦涩的，特别是一些比较复杂的正则表达式，今天写的明天可能就不记得了）。除非是url中确实是需要使用正则表达式来解决才使用`re_path`。