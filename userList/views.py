from django.shortcuts import render
from .models import MyInformation


def myPage(request, pk):
    mydata = MyInformation.objects.all()[pk]
    data = {
        'me': mydata,
    }
    return render(request, 'userList/userList.html', data)
