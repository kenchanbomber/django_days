import datetime
from django.test import TestCase
from django.core.files import File

from post.models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.test_post = Post(title='test post', date=datetime.datetime.now(),
                              content='# title', image=File(file=b'0101'))

    def test_be_empty(self):
        posts = Post.objects.all()
        self.assertEqual(posts.count(), 0)

    def test_be_saved(self):
        self.test_post.save()
        posts = Post.objects.all()
        self.assertEqual(posts.count(), 1)

    def test_be_saved_and_be_retrieved(self):
        self.test_post.save()
        latest_post = Post.objects.all()[0]
        self.assertEqual(self.test_post.id, latest_post.id)