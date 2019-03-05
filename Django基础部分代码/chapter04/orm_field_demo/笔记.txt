# 常用Field笔记：


## navie时间和aware时间：
### 什么是navie时间？什么是aware时间？
1. navie时间：不知道自己的时间表示的是哪个时区的。也就是不知道自己几斤几两。比较幼稚。
2. aware时间：知道自己的时间表示的是哪个时区的。也就是比较清醒。

### pytz库：
专门用来处理时区的库。这个库会经常更新一些时区的数据，不需要我们担心。并且这个库在安装Django的时候会默认的安装。如果没有安装，那么可以通过`pip install pytz`的方式进行安装。

### astimezone方法：
将一个时区的时间转换为另外一个时区的时间。这个方法只能被`aware`类型的时间调用。不能被`navie`类型的时间调用。
示例代码如下：
```python
import pytz
from datetime import datetime
now = datetime.now() # 这是一个navie类型的时间
utc_timezone = pytz.timezone("UTC") # 定义UTC的时区对象
utc_now = now.astimezone(utc_timezone) # 将当前的时间转换为UTC时区的时间
>> ValueError: astimezone() cannot be applied to a naive datetime # 会抛出一个异常，原因就是因为navie类型的时间不能调用astimezone方法


now = now.replace(tzinfo=pytz.timezone('Asia/Shanghai'))
utc_now = now.astimezone(utc_timezone)
# 这时候就可以正确的转换。
```

### replace方法：
可以将一个时间的某些属性进行更改。

### django.utils.timezone.now方法：
会根据`settings.py`中是否设置了`USE_TZ=True`获取当前的时间。如果设置了，那么就获取一个`aware`类型的`UTC`时间。如果没有设置，那么就会获取一个`navie`类型的时间。

### django.utils.timezone.localtime方法：
会根据`setting.py`中的`TIME_ZONE`来将一个`aware`类型的时间转换为`TIME_ZONE`指定时区的时间。

## DateField：

日期类型。在`Python`中是`datetime.date`类型，可以记录年月日。在映射到数据库中也是`date`类型。使用这个`Field`可以传递以下几个参数：
1. `auto_now`：在每次这个数据保存的时候，都使用当前的时间。比如作为一个记录修改日期的字段，可以将这个属性设置为`True`。
2. `auto_now_add`：在每次数据第一次被添加进去的时候，都使用当前的时间。比如作为一个记录第一次入库的字段，可以将这个属性设置为`True`。

## DateTimeField：

日期时间类型，类似于`DateField`。不仅仅可以存储日期，还可以存储时间。映射到数据库中是`datetime`类型。这个`Field`也可以使用`auto_now`和`auto_now_add`两个属性。

## TimeField：

时间类型。在数据库中是`time`类型。在`Python`中是`datetime.time`类型。

### navie和aware介绍以及在django中的用法：
https://docs.djangoproject.com/en/2.0/topics/i18n/timezones/


## EmailField：
类似于`CharField`。在数据库底层也是一个`varchar`类型。最大长度是254个字符。

## FileField：
用来存储文件的。这个请参考后面的文件上传章节部分。

### ImageField：
用来存储图片文件的。这个请参考后面的图片上传章节部分。

### FloatField：
浮点类型。映射到数据库中是`float`类型。

### IntegerField：
整形。值的区间是`-2147483648——2147483647`。

### BigIntegerField：
大整形。值的区间是`-9223372036854775808——9223372036854775807`。

### PositiveIntegerField：
正整形。值的区间是`0——2147483647`。

### SmallIntegerField：
小整形。值的区间是`-32768——32767`。

### PositiveSmallIntegerField：
正小整形。值的区间是`0——32767`。

### TextField：
大量的文本类型。映射到数据库中是longtext类型。

### UUIDField：
只能存储`uuid`格式的字符串。`uuid`是一个32位的全球唯一的字符串，一般用来作为主键。

### URLField：
类似于`CharField`，只不过只能用来存储`url`格式的字符串。并且默认的`max_length`是200。


## Field常用的参数

### null：

如果设置为`True`，`Django`将会在映射表的时候指定是否为空。默认是为`False`。在使用字符串相关的`Field`（CharField/TextField）的时候，官方推荐尽量不要使用这个参数，也就是保持默认值`False`。因为`Django`在处理字符串相关的`Field`的时候，即使这个`Field`的`null=False`，如果你没有给这个`Field`传递任何值，那么`Django`也会使用一个空的字符串`""`来作为默认值存储进去。因此如果再使用`null=True`，`Django`会产生两种空值的情形（NULL或者空字符串）。如果想要在表单验证的时候允许这个字符串为空，那么建议使用`blank=True`。如果你的`Field`是`BooleanField`，那么对应的可空的字段则为`NullBooleanField`。

### blank：

标识这个字段在表单验证的时候是否可以为空。默认是`False`。
这个和`null`是有区别的，`null`是一个纯数据库级别的。而`blank`是表单验证级别的。

### db\_column：

这个字段在数据库中的名字。如果没有设置这个参数，那么将会使用模型中属性的名字。

### default：

默认值。可以为一个值，或者是一个函数，但是不支持`lambda`表达式。并且不支持列表/字典/集合等可变的数据结构。

### primary\_key：

是否为主键。默认是`False`。

### unique：

在表中这个字段的值是否唯一。一般是设置手机号码/邮箱等。

更多`Field`参数请参考官方文档：[https://docs.djangoproject.com/zh-hans/2.0/ref/models/fields/](https://docs.djangoproject.com/zh-hans/2.0/ref/models/fields/)



## 模型中`Meta`配置：

对于一些模型级别的配置。我们可以在模型中定义一个类，叫做`Meta`。然后在这个类中添加一些类属性来控制模型的作用。比如我们想要在数据库映射的时候使用自己指定的表名，而不是使用模型的名称。那么我们可以在`Meta`类中添加一个`db_table`的属性。示例代码如下：
```python
class Book(models.Model):
    name = models.CharField(max_length=20,null=False)
    desc = models.CharField(max_length=100,name='description',db_column="description1")

class Meta:
    db_table = 'book_model'
```

以下将对`Meta`类中的一些常用配置进行解释。

### db_table：
这个模型映射到数据库中的表名。如果没有指定这个参数，那么在映射的时候将会使用模型名来作为默认的表名。

### ordering：
设置在提取数据的排序方式。后面章节会讲到如何查找数据。比如我想在查找数据的时候根据添加的时间排序，那么示例代码如下：
```python
class Book(models.Model):
name = models.CharField(max_length=20,null=False)
desc = models.CharField(max_length=100,name='description',db_column="description1")
pub_date = models.DateTimeField(auto_now_add=True)

class Meta:
db_table = 'book_model'
ordering = ['pub_date']
```

更多的配置后面会慢慢介绍到。
官方文档：https://docs.djangoproject.com/en/2.0/ref/models/options/
