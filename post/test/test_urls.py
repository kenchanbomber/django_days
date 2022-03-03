from django.test import TestCase
from django.urls import resolve, reverse

from post.views import HomeView, PostDetailView, PostListView


class PostUrlsTest(TestCase):
    def test_be_resolved_home_urls(self):
        view_func = resolve(reverse('home')).func
        self.assertEqual(view_func.view_class, HomeView)

    def test_be_resolved_post_detail_urls(self):
        view_func = resolve(reverse('post-detail', args=[1])).func
        self.assertEqual(view_func.view_class, PostDetailView)

    def test_be_resolved_all_posts_urls(self):
        view_func = resolve(reverse('all-posts')).func
        self.assertEqual(view_func.view_class, PostListView)
