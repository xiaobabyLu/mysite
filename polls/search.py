# -*- coding:utf-8 -*-


from django.http import HttpResponse
from django.shortcuts import render_to_response


# 表单
def search_form(request):
    return render_to_response('./polls/search_form.html')


# 接收请求数据
def search(request):
    request.encoding='utf-8'
    if len(request.GET['q']) > 0 :
        message = '你搜索的内容为：' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)