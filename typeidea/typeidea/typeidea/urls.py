from django.contrib import admin
from django.urls import path
# from .custom_site import custom_site
from comment.views import CommentView
from blog.views import (
        IndexView, CategoryView, TagView,
        PostDetailView, SearchView, AuthorView,
)
from config.views import LinkListView
import xadmin

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("category/<category_id>/", CategoryView.as_view(), name="category-list"),
    path("tag/<tag_id>/", TagView.as_view(), name="tag-list"),
    path("post/<post_id>.html/", PostDetailView.as_view(), name="post-detail"),
    path('super_admin/', admin.site.urls, name="super_admin"),
    path('admin/', xadmin.site.urls, name="xadmin"),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<owner_id>', AuthorView.as_view(), name='author'),
    path('links/', LinkListView.as_view(), name='links'),
    path('comment/', CommentView.as_view(), name='comment'),
]
