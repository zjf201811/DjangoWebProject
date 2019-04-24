"""python_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view() , name='index'),
    path('category/<int:category_id>', CategoryView.as_view() ,name='category'),
    path('detail/<int:post_id>',detail,name='detail'),
    path('comment/',comment , name='comment')
]
# from django.views.generic import RedirectView
# urlpatterns += [
#     path('accounts/login/', RedirectView.as_view(url='/admin/login/', permanent=True)),
# ]