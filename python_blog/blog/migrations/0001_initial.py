# Generated by Django 2.0 on 2019-04-15 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='标题')),
                ('content', models.CharField(max_length=20, verbose_name='内容')),
                ('nickname', models.CharField(max_length=50, verbose_name='昵称')),
                ('website', models.URLField(verbose_name='网站')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('status', models.PositiveIntegerField(default=0, verbose_name='状态')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='最近修改')),
                ('content', models.TextField(help_text='正文必须为MarkDown格式', verbose_name='正文')),
                ('content_html', models.TextField(blank=True, editable=False, verbose_name='正文html代码')),
                ('visits', models.PositiveIntegerField(default=0, verbose_name='访问量')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='种类')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='评论目标'),
        ),
    ]
