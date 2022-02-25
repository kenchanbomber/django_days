from enum import auto
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
