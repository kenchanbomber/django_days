from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from .models import Post
from .forms import CommentForm

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
        try:
            post = Post.objects.get(id=id)
            other_posts = Post.objects.all()[:3]

            comment_form = CommentForm()
            return render(request, 'post/post-detail.html', {
                'post': post,
                'other_posts': other_posts,
                'comment_form': comment_form,
            })
        except:
            raise Http404()
    
    def post(self, request, id):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect(reverse('post-detail', request.POST['post_id']))
        else:
            return render(request, 'post/post-detail.html', {
                'post': Post.objects.get(id = request.POST['post_id']),
                'other_posts': Post.objects.all()[:3],
                'comment_form': comment_form
            })
