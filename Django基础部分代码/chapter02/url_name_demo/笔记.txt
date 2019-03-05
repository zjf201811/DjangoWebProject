# url命名：

## 为什么需要url命名？
因为url是经常变化的。如果在代码中写死可能会经常改代码。给url取个名字，以后使用url的时候就使用他的名字进行反转就可以了，就不需要写死url了。

## 如何给一个url指定名称？
在`path`函数中，传递一个`name`参数就可以指定。示例代码如下：
```python
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login')
]
```

## 应用命名空间：
在多个app之间，有可能产生同名的url。这时候为了避免反转url的时候产生混淆，可以使用应用命名空间，来做区分。定义应用命名空间非常简单，只要在`app`的`urls.py`中定义一个叫做`app_name`的变量，来指定这个应用的命名空间即可。示例代码如下：
```python
# 应用命名空间
app_name = 'front'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login')
]
```
以后在做反转的时候就可以使用`应用命名空间:url名称`的方式进行反转。示例代码如下：
```python
login_url = reverse('front:login')
```

## 应用(app)命名空间和实例命名空间：
一个app，可以创建多个实例。可以使用多个url映射同一个app。所以这就会产生一个问题。以后在做反转的时候，如果使用应用命名空间，那么就会发生混淆。为了避免这个问题。我们可以使用实例命名空间。实例命名空间也是非常简单，只要在`include`函数中传递一个`namespace`变量即可。示例代码如下：
```python
urlpatterns = [
    path('',include('front.urls')),
    # 同一个app下有两个实例
    path('cms1/',include('cms.urls',namespace='cms1')),
    path('cms2/',include('cms.urls',namespace='cms2')),
]
```
以后在做反转的时候，就可以根据实例命名空间来指定具体的url。示例代码如下：
```python
def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse('CMS首页')
    else:
        # 获取当前的命名空间
        current_namespace = request.resolver_match.namespace
        return redirect(reverse("%s:login"%current_namespace))
```