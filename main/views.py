from django.shortcuts import render
from .models import MyPost


def basePage(request):
    posts = MyPost.objects.all()[::-1]
    data = {
        'posts': posts,
    }
    return render(request, 'main/main.html', data)


def postPage(request, pk):
    post = MyPost.objects.filter(id=pk)[0]
    data = {
        'post': post,
    }
    return render(request, 'main/postPage.html', data)
