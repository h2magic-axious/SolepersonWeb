from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags

import markdown


# Create your models here.
class Category(models.Model):
    name = models.CharField('分类名', max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('标签名', max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    excerpt = models.CharField('摘要', max_length=50, blank=True)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    content = models.TextField('正文')

    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_app:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite'
            ])
            self.excerpt = strip_tags(md.convert(self.content))[:50]
            super().save(*args, **kwargs)
