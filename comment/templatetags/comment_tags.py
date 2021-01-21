from django import template
from comment.forms import BlogCommentForm

register = template.Library()


@register.inclusion_tag('comment/inclusions/_form.html', takes_context=True)
def show_blog_comment_form(context, article, form=None):
    if form is None:
        form = BlogCommentForm()
    return {
        'form': form,
        'article_item': article
    }


@register.inclusion_tag('comment/inclusions/_list.html', takes_context=True)
def show_comments(context, article):
    comment_list = article.blogcomment_set.all().order_by('-created_time')
    return {
        'comment_count': comment_list.count,
        'comment_list': comment_list
    }
