# Generated by Django 2.1.3 on 2019-03-10 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190306_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=100, verbose_name='评论目标'),
        ),
    ]
