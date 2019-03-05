from django.shortcuts import render
from .models import Article
from django.views.decorators.http import require_http_methods,require_GET,require_POST,require_safe
from django.http import HttpResponse

# require_GET = @require_http_methods(['GET'])

# require_safe = @require_http_methods(['GET','HEAD'])

@require_GET
def index(request):
    # 首页返回所有的文章
    # 只能使用GET请求来访问这个视图函数
    articles = Article.objects.all()
    return render(request,'index.html',context={"articles":articles})

@require_http_methods(['POST','GET'])
def add_article(request):
    # 如果使用GET请求来访问这个视图函数，那么就返回一个添加文章的HTML页面
    # 如果使用POST请求来访问这个视图函数，那么就获取提交上来的数据，然后保存
    # 到数据库中
    if request.method == 'GET':
        return render(request,'add_article.html')
    else:
        title = request.POST.get("title")
        content = request.POST.get('content')
        Article.objects.create(title=title,content=content)
        return HttpResponse('success')