from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    content = MarkdownxField()
    image = models.ImageField()

    def get_html_from_markdown(self):
        return mark_safe(markdownify(self.content))

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.text} ({self.name})"
