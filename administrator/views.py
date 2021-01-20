from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from blogapp.models import Category, Tag


def category_list(request):
    return JsonResponse({
        'count': len(Category.objects.all()),
        'results': [
            {
                'id': category.pk,
                'name': category.name,
                'articleNumber': len(category.article_set.all())
            }
            for category in Category.objects.all()
        ]
    })