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
            if request.user.is_authenticated:
                comment_form = CommentForm({'name': request.user.username})

            return render(request, 'post/post-detail.html', {
                'post': post,
                'other_posts': other_posts,
                'comment_form': comment_form,
                'comments': post.comments.all()
            })
        except:
            raise Http404()

    def post(self, request, id):
        post = Post.objects.get(id=id)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail', args=[id]))
        else:
            return render(request, 'post/post-detail.html', {
                'post': post,
                'other_posts': Post.objects.all()[:3],
                'comment_form': comment_form,
                'comments': post.comments.all()
            })
