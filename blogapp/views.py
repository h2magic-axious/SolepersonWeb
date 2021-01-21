import markdown

from django.views.generic import ListView, DetailView

from django.shortcuts import render, get_object_or_404

from blogapp.models import Article, Category, Tag


# Create your views here.
class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'


class CategoryView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        c = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=c)


class ArchiveView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchiveView, self).get_queryset().filter(created_time__year=year,
                                                              created_time__month=month)


class TagView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        t = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=t)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'article_item'

    def get(self, request, *args, **kwargs):
        response = super(ArticleDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        article = super(ArticleDetailView, self).get_object(queryset=None)
        MARKDOWN = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        article.body = MARKDOWN.convert(article.content)
        article.toc = MARKDOWN.toc
        return article


# def detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     article.increated_views()
#
#     content = MARKDOWN.convert(article.content)
#
#     return render(request, 'detail.html',
#                   context={'article_item': article, 'article_content': content, 'article_toc': MARKDOWN.toc})

# def archive(request, year, month):
#     return render(request, 'index.html', context={
#         'article_list': Article.objects.filter(
#
#         ).order_by('-created_time')
#     })


# def category(request, pk):
#     c = get_object_or_404(Category, pk=pk)
#     return render(request, 'index.html', context={
#         'article_list': Article.objects.filter(category=c).order_by('-created_time')
#     })


# def tag(request, pk):
#     t = get_object_or_404(Tag, pk=pk)
#     return render(request, 'index.html', context={
#         'article_list': Article.objects.filter(tags=t).order_by('-created_time')
#     })
