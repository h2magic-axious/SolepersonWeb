import markdown

from django.shortcuts import render, get_object_or_404

from blogapp.models import Article

MARKDOWN = markdown.Markdown(extensions=[
    'markdown.extensions.extra',
    'markdown.extensions.codehilite'
])


# Create your views here.
def index(request):
    return render(request, 'index.html')


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    content = MARKDOWN.convert(article.content)

    return render(request, 'detail.html', context={'article_item': article, 'article_content': content})
