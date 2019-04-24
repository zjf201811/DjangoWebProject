from django.shortcuts import render,HttpResponse,reverse,redirect
from .models import Post, Category, Comment
from .forms import CommentForm
from django.db.models import Q, F
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator,Page
from django.shortcuts import get_object_or_404

class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorys = Category.objects.all()
        context.update({
            'form': CommentForm,
            'categorys': categorys,
            # 'sidebars': SiderBar.get_all(),
        })

        return context


class IndexView(CommonViewMixin, ListView):
    paginate_by = 1
    context_object_name = "post_list"
    template_name = "index.html"

    def get_queryset(self):
        queryset = Post.objects.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['username'] = 'zhiliao'
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj,1)
        context.update(pagination_data)
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=1):
        current_page = page_obj.number
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = False

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page - around_count, current_page)

        if current_page >= num_pages - around_count - 1:
            right_pages = range(current_page + 1, num_pages + 1)
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + around_count + 1)

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': num_pages
        }


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

    # def get_queryset(self,category_id=None):
    #     category = Category.objects.get(id=category_id)
    #     categorys = Category.objects.all()
    #
    #     return categorys
    #
    # def get_context_data(self, **kwargs):
    #     # category = Category.objects.get(id=category_id)
    #     # categorys = Category.objects.all()
    #     # post_list = category.post_set.all().select_related('owner', 'category')
    #     # print(category_id)
    #     # context = {
    #     #     # 'categorys': categorys,
    #     #     'post_list': post_list
    #     # }
    #     # return context
    #     pass



# def category(request, category_id=None):
#     category = Category.objects.get(id=category_id)
#     categorys = Category.objects.all()
#     post_list = category.post_set.all().select_related('owner', 'category')
#     # print(category_id)
#     context = {
#         'categorys': categorys,
#         'post_list': post_list
#     }
#     return render(request, 'index.html', context)



def detail(request, post_id):
    categorys = Category.objects.all()
    post=Post.objects.get(id=post_id)
    comments=Comment.objects.all()
    Post.objects.filter(pk=post_id).update(visits=F('visits') + 1)
    context = {
        'post':post,
        'categorys': categorys,
        "CommentForm":CommentForm(),
        'comments':comments
    }
    return render(request,'detail.html',context)


def comment(request, *args, **kwargs):

    print(request)
    comment_form = CommentForm(request.POST)
    post_id = request.POST.get('post')

    if comment_form.is_valid():

        post=Post.objects.get(id=post_id)
        print(type(post))
        instance = comment_form.save(commit=False)  #
        instance.post = post
        instance.save()
        # return HttpResponse('评论成功')
        return redirect(request.POST.get('path'))
    else:
        return HttpResponse('评论失败')
