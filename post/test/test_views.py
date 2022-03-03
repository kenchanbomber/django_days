import datetime
from typing import OrderedDict
from django.test import TestCase
from django.urls import reverse
from django.core.files import File

from post.models import Post


class PostViewsTest(TestCase):
    def setUp(self):
        self.test_post01 = Post.objects.create(title='test post', date=datetime.datetime(2001, 3, 24),
                                               content='# title', image=File(file=b''))
        self.test_post02 = Post.objects.create(title='test post', date=datetime.datetime(2002, 3, 24),
                                               content='# title', image=File(file=b''))
        self.test_post04 = Post.objects.create(title='test post', date=datetime.datetime(2004, 3, 24),
                                               content='# title', image=File(file=b''))
        self.test_post03 = Post.objects.create(title='test post', date=datetime.datetime(2003, 3, 24),
                                               content='# title', image=File(file=b''))

    def test_be_rendered_home_views(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/home.html')
        self.assertQuerysetEqual(
            list(response.context['posts']), Post.objects.all()[:4], ordered=True)

    def test_be_rendered_all_posts(self):
        response = self.client.get(reverse('all-posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/all-posts.html')
        self.assertEqual(response.context['posts'][0], self.test_post01)

    def test_be_rendered_post_detail(self):
        response = self.client.get(
            reverse('post-detail', args=[self.test_post01.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/post-detail.html')
        self.assertEqual(response.context['post'], self.test_post01)
        self.assertQuerysetEqual(
            list(response.context['other_posts']), Post.objects.all()[:3], ordered=True)
