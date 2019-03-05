from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def index(request):
    username = request.GET.get('username')
    if not username:
        return redirect(reverse('errors:403'))
    return HttpResponse('首页')

