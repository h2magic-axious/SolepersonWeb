from django.contrib import admin

from comment.models import BlogComment


# Register your models here.
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'email', 'article', 'created_time']
    fields = ['nickname', 'email', 'text', 'article']


admin.site.register(BlogComment)
