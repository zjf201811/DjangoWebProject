from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Post, Category, Tag
from .adminforms import PostAdminForm
# from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
from django.contrib.admin.models import LogEntry
from xadmin.layout import Row, Fieldset
from xadmin.filters import RelatedFieldListFilter, manager
import xadmin


# @xadmin.sites.register(LogEntry)
# class LogEntryAdmin(object):
#     list_display = ['object_repr', 'object_id', 'action_flag', 'user','change_message']


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('id', 'name', 'owner', 'status', 'is_nav', 'created_time','post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


class CategoryOwnerFilter(RelatedFieldListFilter):

    # title = '分类过滤器'
    # parameter_name = 'owner_category'
    #
    # def lookups(self, request, model_admin):
    #     return Category.objects.filter(owner=request.user).values_list('id', 'name')
    #
    # def queryset(self, request, queryset):
    #     category_id = self.value()
    #     if category_id:
    #         return queryset.filter(category_id=self.value())
    #     return queryset
    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, admin_view, field_path):
        super().__init__(field, request, params, model, admin_view, field_path)
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id','name')

manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator'
    ]
    list_display_links = []

    list_filter = ['category', ]
    search_fields = ['title', 'category__name']

    actions_on_top = True

    save_on_top = True
    exclude = ['owner', ]
    # filter_horizontal = ('tag',)
    filter_vertical = ('tags',)
    # fieldsets = (
    #     ('基础配置', {
    #         'description':'基础配置描述',
    #         'fields': (
    #             ('title', 'category',),
    #             'status',
    #         ),
    #     }),
    #     ('内容', {
    #         'fields': (
    #             'desc',
    #             'content',
    #         ),
    #     }),
    #     ('额外信息', {
    #         'classes': ('wide',),
    #         'fields': ('tag',),
    #     })
    # )

    form_layout = (
        Fieldset(
            '基础信息',Row('title', 'category'),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'content',
        )
    )


    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'

    # class Media:
    #     css = {
    #         'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
    #     }
    #     js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)
