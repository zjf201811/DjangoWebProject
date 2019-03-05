#encoding: utf-8
from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware

def index(request):
    response = HttpResponse("index")
    expires = datetime(year=2018,month=5,day=9,hour=20,minute=0,second=0)
    expires = make_aware(expires)
    response.set_cookie('user_id','abc',expires=expires,max_age=180,path='/cms/')
    return response

def delete_cookie(request):
    response = HttpResponse('delete')
    response.delete_cookie('username')
    return response

def my_list(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

def cms_view(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

def session_view(request):
    request.session['username'] = 'zhiliao'
    username = request.session.get('username')
    # username = request.session.pop('username')
    # request.session['username'] = 'zhiliao'
    # request.session['userid'] = 10
    # request.session.clear()
    # request.session.flush()
    # print(username)
    # request.session.set_expiry(None)
    # request.session.set_expiry(-1)
    # request.session.clear_expired()
    return HttpResponse('session view')