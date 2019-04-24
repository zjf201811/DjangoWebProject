from django.db import models
from django.contrib.auth.models import User
import mistune


class Category(models.Model):  # 文章的分类模型
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name ='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField(max_length=10, verbose_name='标签')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    updated = models.DateTimeField(auto_now=True, verbose_name='最近修改')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'
        ordering = ['-created']


class Post(models.Model):  # 博客的文章模型
    STATUS_NORMAL = 0
    STATUS_DELETE = 1
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )
    title = models.CharField(max_length=30, verbose_name='标题')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS, verbose_name='状态')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    updated = models.DateTimeField(auto_now=True, verbose_name='最近修改')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='正文', help_text='正文必须为MarkDown格式')
    content_html = models.TextField(verbose_name='正文html代码', blank=True, editable=False)
    category = models.ForeignKey(Category, verbose_name='种类', on_delete=models.CASCADE)
    visits = models.PositiveIntegerField(default=0, verbose_name='访问量')
    tags = models.ManyToManyField(Tag,null=True,verbose_name='标签')
    def save(self, *args, **kwargs):
        self.content_html = mistune.markdown(self.content)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-created']




class Comment(models.Model):  # 评论模型

    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    post = models.ForeignKey(Post, verbose_name='评论目标', on_delete=models.CASCADE)
    content = models.CharField(max_length=200, verbose_name='内容')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    website = models.URLField(verbose_name='网站')
    email = models.EmailField(verbose_name='邮箱')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.post.title

    @classmethod
    def get_by_post(cls, post):
        return cls.objects.filter(post=post, status=cls.STATUS_NORMAL)

    class Meta:
        verbose_name = verbose_name_plural = '评论'

