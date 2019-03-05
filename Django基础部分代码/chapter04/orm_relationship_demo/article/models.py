from django.db import models
from frontuser.models import FrontUser

class Category(models.Model):
    name = models.CharField(max_length=100)

# app.模型的名字

def default_category():
    return Category.objects.get(pk=4)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField("Article",related_name='tags')

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("Category",on_delete=models.CASCADE,null=True,related_name='articles')
    author = models.ForeignKey("frontuser.FrontUser",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "<Article:(id:%s,title:%s)>" % (self.id,self.title)


class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey("Comment",on_delete=models.CASCADE)


# category:
# id,name
# 1,最新

# article：
# id,title,category
# 1,xxx,1
