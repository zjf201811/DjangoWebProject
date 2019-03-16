from django.contrib import admin
from .models import Comment
import xadmin
# from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.


@xadmin.sites.register(Comment)
class CommentAdmin(object):
    list_display = ("target", 'nickname', 'content', 'website', 'created_time')