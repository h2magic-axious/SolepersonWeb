from django import template

from blogapp.models import Category, Tag, Article

register = template.Library()


@register.simple_tag
def all_categories():
    return [
        (category.name, len(category.article_set.all())) for category in Category.objects.all()
    ]


@register.simple_tag
def all_tags():
    return Tag.objects.all()


@register.simple_tag
def breadcrumb_active(last):
    if last:
        return 'active'
    else:
        return ''
