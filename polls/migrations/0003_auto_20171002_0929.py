# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 01:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.CharField(max_length=100, null=True, verbose_name='提交人'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='问题描述'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('python', 'python编程'), ('sql', 'sql数据库'), ('java', 'java编程')], default=('python', 'python编程'), max_length=200, verbose_name='问题类型'),
        ),
    ]
