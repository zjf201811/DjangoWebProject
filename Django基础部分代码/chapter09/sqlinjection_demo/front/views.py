from django.shortcuts import render
from django.db import connection

# def index(request):
#     user_id = request.GET.get('user_id')
#     context = {}
#     if user_id:
#         cursor = connection.cursor()
#         user_id = '1 or 1=1'
#         sql = 'select id,username from front_user where id=' + user_id
#         cursor.execute("select id,username from front_user where id=%s"%user_id)
#         sql = 'select id,username from front_user where id=1 or 1=1'
#         rows = cursor.fetchall()
#         context['rows'] = rows
#     return render(request,'index.html',context=context)


def index(request):
    username = request.GET.get('username')
    context = {}
    if username:
        cursor = connection.cursor()
        sql = "select id,username from front_user where username=%s"
        cursor.execute(sql,(username,))
        rows = cursor.fetchall()
        context['rows'] = rows
    return render(request,'index.html',context=context)
