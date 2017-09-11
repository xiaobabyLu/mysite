from django.shortcuts import render
from test1 import models
# Create your views here.

# user_list = [{"user": "jack", "pwd": "abc"}, {"user": "tom", "pwd": "123"}, ]


def index(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        #添加到数据库
        models.UserInfo.objects.create(user=username,pwd=password)

    user_list = models.UserInfo.objects.all()

        # print(username, password)
        # temp = {"user": username, "pwd":password}
        # user_list.append(temp)
    return render(request, "index.html",{"data": user_list})
