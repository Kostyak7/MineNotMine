from django.shortcuts import render
from .models import MyPost
from django.views import View


class BasePageView(View):

    def get(self, request, *args, **kwargs):
        posts = MyPost.objects.all()[::-1]
        data = {
            'posts': posts,
        }
        return render(request, 'main/main.html', data)


class PostPageView(View):

    def get(self, request, pk, *args, **kwargs):
        post = MyPost.objects.filter(id=pk)[0]
        data = {
            'post': post,
        }
        return render(request, 'main/postPage.html', data)
