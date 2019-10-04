from django.shortcuts import render
import time
from .models import Fibo


def fibo_view(num):
    if num < 2:
        return 1
    else:
        num1 = 1
        num2 = 1
        for i in range(2, num):
            temp = num1 + num2
            num1 = num2
            num2 = temp
        return num2


def fibo_no(request):
    num = 0
    result = 0
    time = 0

    if request.GET.get('number'):
        start_time=time.time()
        number = request.GET.get('number')
        num = int(number)
        result = fibo_view(num)
        end_time = time.time()-start_time
        time = str(end_time)[0:4]

        obj = Fibo.objects.create(
            number=num, result=result, time=time)
        obj.save()

    return render(request,'index.html',
                  {'number': num, 'result': result,'time': time}
    )
