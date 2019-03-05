from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import User
from .forms import LoginForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Permission,ContentType,Group
from .models import Article
# from .models import Person

def index(request):
    # user = User.objects.create_user(username='zhiliao',email='zhiliao@qq.com',password='111111')
    # user = User.objects.create_superuser(username='abc',email='abc@qq.com',password='111111')
    # user = User.objects.get(pk=1)
    # user.set_password('222222')
    # user.save()
    # username = 'zhiliao'
    # password = '111111'
    # user = authenticate(request,username=username,password=password)
    # if user:
    #     print('登录成功：',user.username)
    # else:
    #     print('用户名或密码错误！')
    # user = User.objects.create_user(telephone='18899997777',username='zhiliao',password='111111')
    # return HttpResponse("success")

    return render(request,'index.html')


def proxy_view(request):
    # blacklist = Person.get_blacklist()
    # for person in blacklist:
    #     print(person.username)
    return HttpResponse('proxy')


# def my_authenticate(telephone,password):
#     user = User.objects.filter(extension__telephone=telephone).first()
#     if user:
#         is_correct = user.check_password(password)
#         if is_correct:
#             return user
#         else:
#             return None
#     else:
#         return None

def one_view(request):
    # user = User.objects.create_user(username='zhiliao1',email='zhiliao@qq.com',password='111111')
    # user = User.objects.create_user(username='zhiliao2',email='zhiliao2@qq.com',password='111111')
    # user.extension.telephone = '18899997777'
    # user.save()
    # telephone = request.GET.get('telephone')
    # password = request.GET.get('password')
    # user = my_authenticate(telephone,password)
    # if user:
    #     print('验证成功：%s'%user.username)
    # else:
    #     print('验证失败！')
    return HttpResponse('一对一扩展User模型')


def inherit_view(request):
    # telephone = '18899997777'
    # password = '111111'
    # username = 'zhiliao1'
    # user = User.objects.create_superuser(telephone=telephone,username=username,password=password)
    # print(user.username)
    # user = authenticate(request,username='18899997777',password='111111')
    # if user:
    #     print('验证成功！')
    #     print(user.username)
    # else:
    #     print('验证失败！')


    # User.objects.create_user(telephone='18899997777',password='111111',username='zhiliao')
    user = authenticate(request,username='18899997777',password='111111')
    if user:
        print(user.username)
        print('验证成功！')
    else:
        print('验证失败！')
    return HttpResponse('继承AbstractUser扩展用户')


# 切记：这里一定不要定义login视图函数
# 可以其他的名字
def my_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request,username=telephone,password=password)
            if user and user.is_active:
                login(request,user)
                if remember:
                    # 设置为None，则表示使用全局的过期时间
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return HttpResponse('登录成功')
            else:
                return HttpResponse('手机号码或者密码错误！')
        else:
            print(form.errors)
            return redirect(reverse('login'))

def my_logout(request):
    logout(request)
    return HttpResponse('成功退出登录！')

@login_required(login_url='/login/')
def profile(request):
    return HttpResponse('这是个人中心，只有登录了以后才能查看到！')


def add_permission(request):
    content_type = ContentType.objects.get_for_model(Article)
    permission = Permission.objects.create(codename='black_article',name='拉黑文章',content_type=content_type)
    return HttpResponse('权限创建成功！')


def operate_permission(request):
    user = User.objects.first()
    content_type = ContentType.objects.get_for_model(Article)
    permissions = Permission.objects.filter(content_type=content_type)
    for permission in permissions:
        print(permission)
    user.user_permissions.set(permissions)
    user.save()
    # user.user_permissions.clear()
    # user.user_permissions.remove(*permissions)
    if user.has_perm('front.view_article'):
        print('这个拥有view_article权限！')
    else:
        print('这个没有view_article权限！')
    print(user.get_all_permissions())
    return HttpResponse('操作权限的视图！')

@permission_required(['front.add_article','front.view_article'],login_url='/login/',raise_exception=True)
def add_article(request):
    # 1. 判断这个用户有没有登录
    # if request.user.is_authenticated:
    #     print('已经登陆了！')
    #     if request.user.has_perm('front.add_article'):
    #         return HttpResponse('这是添加文章的页面！')
    #     else:
    #         return HttpResponse('您没有访问该页面的权限',status=403)
    # else:
    #     return redirect(reverse('login'))
    return HttpResponse('这是添加文章的页面！')


def operate_group(request):
    # group = Group.objects.create(name='运营')
    # content_type = ContentType.objects.get_for_model(Article)
    # permissions = Permission.objects.filter(content_type=content_type)
    # group.permissions.set(permissions)
    # group.save()
    # group = Group.objects.filter(name='运营').first()
    # user = User.objects.first()
    # user.groups.add(group)
    # user.save()
    user = User.objects.first()
    # permissions = user.get_group_permissions()
    # print(permissions)
    # user.has_perm：
    # 1. 首先判断user.permissions下有没有这个权限，如果有，就True
    # 2. 如果user.permissions下没有这个权限，那么就会判断
    # 他所属的分组下有没有这个权限
    if user.has_perms(['front.add_article','front.change_article']):
        print('有这个添加文章的权限！')
    else:
        print('没有添加文章的权限！')
    return HttpResponse("操作分组！")