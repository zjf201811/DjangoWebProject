from django.urls import path
from post import views

urlpatterns=[
    path("",views.index_view),
    path("index.html/",views.index_view),
    path('page/<num>',views.index_view),
    path('post/details/<post_id>',views.post_details_view),
]