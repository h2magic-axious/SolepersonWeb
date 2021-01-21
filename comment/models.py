from django.db import models

from blogapp.models import Article


# Create your models here.
class BlogComment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField('昵称', max_length=20)
    email = models.EmailField('邮箱', max_length=50)
    text = models.TextField('内容', max_length=255)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.nickname}: {self.text[:20]}"
