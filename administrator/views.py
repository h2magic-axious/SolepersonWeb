from django.shortcuts import render

from blogapp.models import Category, Tag


# Create your views here.
def admin_index(request):
    return render(request, 'blogadmin/admin_index.html')


def admin_article_edit(request):
    return render(request, 'blogadmin/admin_blog_app_edit.html')


def admin_categories(request):
    return render(request, 'blogadmin/admin_blog_category.html')


def admin_tags(request):
    return render(request, 'blogadmin/admin_blog_tag.html')
