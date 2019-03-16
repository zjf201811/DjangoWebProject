from django.shortcuts import get_object_or_404
from .models import Post, Tag, Category
from django.contrib.auth.models import User
from config.models import SiderBar
from django.views.generic import ListView, DetailView
from django.db.models import Q, F
from comment.forms import CommentForm
from comment.models import Comment

import xadmin
from xadmin import views

# 创建xadmin的最基本管理器配置，并与view绑定
# class BaseSetting(object):
#     # 开启主题功能
#     enable_themes = True
#     use_bootswatch = True
#
# # 将基本配置管理与view绑定
# xadmin.site.register(views.BaseAdminView,BaseSetting)

class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SiderBar.get_all(),
        })
        context.update(Category.get_navs())
        return context


class IndexView(CommonViewMixin, ListView):

    paginate_by = 5
    # context_object_name = "post_list"
    template_name = "blog/list.html"

    def get_queryset(self):
        queryset = Post.latest_posts()
        return queryset


class SearchView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'keyword': self.request.GET.get("keyword"," ")
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword)|Q(desc__icontains=keyword))


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get("category_id")
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            "category": category,
        })
        return context

    def get_queryset(self):
        queryset= super().get_queryset()
        category_id = self.kwargs.get("category_id")
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        print(self.kwargs)
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id=tag_id)


class PostDetailView(CommonViewMixin, DetailView):
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update({
    #         ' ': CommentForm,
    #         'comment_list': Comment.get_by_target(self.request.path),
    #     })
    #     return context

    def get(self, request, *args, **kwargs):
        response = super().get(request,*args, kwargs)
        Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1, uv=F('uv')+1)
        # from django.db import connection
        # print(connection.queries)
        return response


class AuthorView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner_id = self.kwargs.get("owner_id")
        owner = get_object_or_404(User, pk=owner_id)
        context.update({
            "owner": owner,
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')

        return queryset.filter(owner_id=author_id)
# def post_list(request, category_id=None, tag_id=None):
#     tag = None
#     category = None
#     if tag_id:
#         post_list, tag = Post.get_by_tag(tag_id)
#     elif category_id:
#         post_list, category = Post.get_by_category(category_id)
#     else:
#         post_list = Post.latest_posts()
#     context = {
#         'category': category,
#         'tag': tag,
#         'post_list': post_list,
#         'sidebars': SiderBar.get_all(),
#     }
#     context.update(Category.get_navs())
#     return render(request, 'blog/list.html', context=context)
# def post_detail(request, post_id=None):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
#     context = {
#         'post': post,
#     }
#     context.update(Category.get_navs())
#     return render(request, 'blog/detail.html', context=context)
