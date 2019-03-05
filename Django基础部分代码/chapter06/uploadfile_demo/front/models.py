from django.db import models
from django.core import validators

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # thumbnial = models.FileField(upload_to='%Y/%m/%d/',validators=[validators.FileExtensionValidator(['txt'],message='thumbnial必须为txt格式的文件！')])
    thumbnial = models.ImageField(upload_to='%Y/%m/%d/')
