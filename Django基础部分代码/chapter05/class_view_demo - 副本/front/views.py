from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic import ListView
from django.core.paginator import Paginator,Page

def add_article(request):
    articles = []
    for x in range(0,102):
        article = Article(title='标题：%s'%x,content='内容：%s'%x)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse('article added successfully')

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(*kwargs)
        context['username'] = 'zhiliao'
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        print(page_obj.number)
        return context

    # def get_queryset(self):
    #     return Article.objects.filter(id__lte=9)