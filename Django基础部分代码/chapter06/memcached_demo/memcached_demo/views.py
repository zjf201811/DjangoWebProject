#encoding: utf-8

from django.http import HttpResponse
from django.core.cache import cache
from django.core.cache.backends.memcached import MemcachedCache

# 如何查看memcached中所有的key
# > stats items
# > stats cachedump [items_id] 0

def index(request):
    cache.set("password",'zhiliao',100)
    username = cache.get("username")
    print(username)
    return HttpResponse('index')