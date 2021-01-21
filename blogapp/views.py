import markdown

from django.shortcuts import render, get_object_or_404

from blogapp.models import Article, Category, Tag


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


def archive(request, year, month):
    return render(request, 'index.html', context={
        'article_list': Article.objects.filter(
            created_time__year=year,
            created_time__month=month
        ).order_by('-created_time')
    })


def category(request, pk):
    c = get_object_or_404(Category, pk=pk)
    return render(request, 'index.html', context={
        'article_list': Article.objects.filter(category=c).order_by('-created_time')
    })


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    return render(request, 'index.html', context={
        'article_list': Article.objects.filter(tags=t).order_by('-created_time')
    })
