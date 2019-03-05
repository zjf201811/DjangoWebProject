from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article,Tag
from .models import User

def index(request):
    article = Article.objects.first()
    tag1 = Tag.objects.create(name='Python')
    tag2 = Tag.objects.create(name='Django')
    article.tags.add(tag1,tag2)
    article.save()
    return HttpResponse("success")
