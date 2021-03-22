from django import template

from blogapp.models import Article, Category, Tag

register = template.Library()


@register.inclusion_tag('inclusions/_recent_article.html', takes_context=True)
def show_recent_articles(context, num=5):
    return {
        'recent_article_list': Article.objects.all().order_by('-created_time')[:num]
    }


@register.inclusion_tag('inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Article.objects.dates('created_time', 'month', order='DESC')
    }


@register.inclusion_tag('inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all()
    }


@register.inclusion_tag('inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all()
    }