from django.http import HttpResponse
from TestModel.models import Test

def testdb(request):
    test1 =Test(name = 'lu')
    test1.save()
    # test2 = Test.objects.get(id=2)
    # test2.name = 'lulu'
    # test2.save()

    # test2 = Test.objects.get(id=2).delete()

    return HttpResponse("<p> 添加数据成功！！！ </p>")