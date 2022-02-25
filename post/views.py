from django.shortcuts import render
from django.views import View

from .models import Post

# Create your views here.


class HomeView(View):
    def get(self, request):
        featured_posts = Post.objects.all()[:4]
        return render(request, 'post/home.html', {
            'posts': featured_posts
        })


class PostListView(View):
    def get(self, request):
        all_posts = Post.objects.all()
        return render(request, 'post/all-posts.html', {
            'posts': all_posts
        })


class PostDetailView(View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        other_posts = Post.objects.all()[:3]
        return render(request, 'post/post-detail.html', {
            'post': post,
            'other_posts': other_posts
        })
