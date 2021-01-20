from django.shortcuts import render, get_object_or_404, redirect

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


# Form functions
def admin_category_post(request, pk):
    category = get_object_or_404(Category, pk=pk) if pk else Category()
    if request.method == 'POST':
        category.name = request.POST['category_name']
        category.save()

    return redirect('admin:admin_categories_list')
