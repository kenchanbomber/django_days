from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'post/home.html')


class PostListView(View):
    def get(self, request):
        return render(request, 'post/all-posts.html')


class PostDetailView(View):
    def get(self, request, id):
        return render(request, 'post/post-detail.html')
