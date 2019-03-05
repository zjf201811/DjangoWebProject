from django.shortcuts import render
from post.models import *
# Create your views here.


def index_view(request, num='1'):
    page,page_range = Post.get_posts_by_page(num,2)
    return render(request, 'index.html',context={'page': page,'page_range':page_range})

def post_details_view(request,post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return 0
    return render(request, 'details.html', {'post': post})