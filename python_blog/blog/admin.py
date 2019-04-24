from django.contrib import admin
from .models import Post, Category, Comment,Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated', 'owner', 'category', 'visits')
    # filter_horizontal = ('tag',)
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    pass


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass

