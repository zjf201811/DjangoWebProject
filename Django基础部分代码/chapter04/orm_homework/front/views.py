from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Score,Course,Teacher
from django.db.models import Avg,Count,Sum,Q
from django.db import connection

def index(request):
    # 1. 查询平均成绩大于60分的同学的id和平均成绩；
    students = Student.objects.annotate(score_avg=Avg("score__number")).filter(score_avg__gt=60).values('id','score_avg')
    for student in students:
        print(student)
    print(connection.queries)
    return HttpResponse("success")

def index2(request):
    # 2. 查询所有同学的id、姓名、选课的数量、总成绩；
    students = Student.objects.annotate(course_nums=Count("score"),total=Sum("score__number")).values('id','name',"course_nums","total")
    for student in students:
        print(student)
    return HttpResponse("index2")

def index3(reuqest):
    count = Teacher.objects.filter(name__startswith='李').count()
    print(count)
    return HttpResponse("index3")

def index4(reqeust):
    students = Student.objects.exclude(score__course__teacher__name='李老师').values('id','name')
    for student in students:
        print(student)
    return HttpResponse("index4")

def index5(reqeust):
    #查询学过课程id为1和2的所有同学的id、姓名；
    students = Student.objects.filter(score__course__in=[1,2]).values('id','name').distinct()
    for student in students:
        print(student)
    return HttpResponse("index5")


def index6(request):
    # 查询学过“黄老师”所教的“所有课”的同学的id、姓名；
    # 1. 首先先找到每一位学生学习的黄老师课程的数量；A
    # 2. 在课程的表中找到黄老师教的课程的数量；B
    # 3. 判断A是否等于B，如果相等，那么意味着这位学生学习了黄老师教的
    # 所有课程，如果不想等，那么意味着这位学生没有学完黄老师教的所有课程
    students = Student.objects.annotate(nums=Count("score__course",filter=Q(score__course__teacher__name='黄老师'))).filter(nums=Course.objects.filter(teacher__name='黄老师').count()).values('id','name')
    for student in students:
        print(student)
    return HttpResponse("index6")