from unicodedata import name
from django.urls import path

from .views import HomeView, PostListView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('posts', PostListView.as_view(), name="all-posts"),
    path('posts/<int:id>', PostDetailView.as_view(), name="post-detail"),
]
