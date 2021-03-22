from django.db import models
from django.urls import reverse


# Create your models here.
class ProgramName(models.Model):
    name = models.CharField('项目名', max_length=50)
    created_time = models.DateTimeField('项目发起日期', auto_now_add=True)
    modified_time = models.DateTimeField('最后修改日期', auto_now=True)
    document_url = models.URLField('策划文档')
    github_url = models.URLField('项目地址')
    excerpt = models.CharField('项目简介', max_length=100)

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('program:program_item', kwargs={'pk': self.pk})


class ProgramJournal(models.Model):
    title = models.CharField('标题', max_length=50)
    created_time = models.DateTimeField('创建日期', auto_now_add=True)
    excerpt = models.CharField('简述', max_length=100)
    body = models.TextField('内容')

    program_name = models.ForeignKey(ProgramName, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '日志'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('program:program_detail', kwargs={'pk': self.pk})
