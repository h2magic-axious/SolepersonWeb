import base64, hmac

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib import auth

from blogapp.models import Category, Tag


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            sha_str = hmac.new(str(password).encode('utf-8'))
            return JsonResponse({'status': 1, 'token': base64.urlsafe_b64encode()})

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
