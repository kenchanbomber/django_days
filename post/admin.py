from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Post, Comment

# Register your models here.
admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment)
