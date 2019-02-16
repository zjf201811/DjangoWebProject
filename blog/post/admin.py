from django.contrib import admin
from post.models import *
# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','desc','created','category']
    list_filter = ['category__name']

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostModelAdmin)
