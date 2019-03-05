#encoding: utf-8

from django.urls import path
from . import views

app_name = 'errors'

urlpatterns = [
    path('400.html',views.view_400,name='400'),
    path('403.html',views.view_403,name='403')
]