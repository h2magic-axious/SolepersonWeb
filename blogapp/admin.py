from django.contrib import admin

from blogapp.models import Article, Category, Tag


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'category']
    fields = ['title', 'excerpt', 'content', 'category', 'tags', 'seo_keywords']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
