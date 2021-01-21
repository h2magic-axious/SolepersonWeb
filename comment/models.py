from django.db import models

from blogapp.models import Article


# Create your models here.
class BlogComment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    text = models.CharField(max_length=255)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)