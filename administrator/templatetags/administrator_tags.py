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
    return [
        (tag.name, len(tag.article_set.all())) for tag in Tag.objects.all()
    ]


@register.simple_tag
def breadcrumb_active(last):
    if last:
        return 'active'
    else:
        return ''
