from django import template

from blogapp.models import Category

register = template.Library()


@register.simple_tag
def administrator_category_list():
    return Category.objects.all()


@register.simple_tag
def breadcrumb_active(last):
    if last:
        return 'active'
    else:
        return ''
