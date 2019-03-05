from django.db import models

# class ArticleTag(models.Model):
#     article = models.ForeignKey('Article', models.DO_NOTHING, primary_key=True)
#     tag = models.ForeignKey('Tag', models.DO_NOTHING)
#
#     class Meta:
#         db_table = 'article_tag'
#         unique_together = (('article', 'tag'),)


class Article(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey('front.User', models.SET_NULL, blank=True, null=True)
    # 使用ManyToManyField模型到表，生成的中间表的规则是：article_tags
    # 但现在已经存在的表的名字叫做：article_tag
    # 可以使用db_table，指定中间表的名字
    tags = models.ManyToManyField("Tag",db_table='article_tag')

    class Meta:
        db_table = 'article'


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'tag'
