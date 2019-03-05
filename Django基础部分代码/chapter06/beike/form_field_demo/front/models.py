from django.db import models
from django.core import validators

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to="%Y/%m/%d/")
