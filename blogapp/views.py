import markdown
from markdown.extensions.toc import TocExtension

from django.shortcuts import render, get_object_or_404

from blogapp.models import Article


# Create your views here.
def index(request):
    return render(request, 'index.html', context={'article_list': Article.objects.all()})


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    MARKDOWN = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])

    content = MARKDOWN.convert(article.content)

    return render(request, 'detail.html',
                  context={'article_item': article, 'article_content': content, 'article_toc': MARKDOWN.toc})
