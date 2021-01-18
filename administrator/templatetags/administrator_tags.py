from django import template

from administrator.models import Menus

register = template.Library()


@register.simple_tag
def administrator_menus():
    return Menus.objects.all()
