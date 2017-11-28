from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# import time
# Create your models here.
question_type =(('python','python编程'),
                ('sql','sql数据库'),
                ('java', 'java编程'),
                )


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.CharField("问题描述",max_length=200)
    question_type = models.CharField("问题类型",max_length=200,choices=question_type,default=question_type[0])
    pub_date = models.DateTimeField("发布时间",default=timezone.now)
    author = models.CharField("提交人",max_length=100,null=True,blank=False)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=5) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently!'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class CommBase(models.Model):
    # id = models.AutoField()
    user_name = models.CharField(max_length=200)
    content = models.CharField(max_length=300)
    pub_date = models.DateField()

    class Meta:
        abstract = True


TYPES = (('x1', 'xxx'),)


class Member(CommBase):
    user_type = models.CharField(max_length=20,choices=TYPES)


class User(models.Model):
    username = models.CharField(max_length=300,blank=False)
    password = models.CharField(max_length=50,blank=False)
    email = models.CharField(max_length=100,blank=False)


