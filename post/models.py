from django.db import models
from django.utils.safestring import mark_safe
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    content = MarkdownxField()
    image = models.ImageField()

    def get_html_from_markdown(self):
        return mark_safe(markdownify(self.content))

    def __str__(self):
        return self.title
