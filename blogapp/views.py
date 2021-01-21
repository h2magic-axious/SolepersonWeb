import markdown

from django.views.generic import ListView, DetailView

from django.shortcuts import get_object_or_404

from blogapp.models import Article, Category, Tag

from pure_pagination.mixins import PaginationMixin


# Create your views here.
class IndexView(PaginationMixin, ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'
    paginate_by = 5


class CategoryView(PaginationMixin, ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'
    paginate_by = 5

    def get_queryset(self):
        c = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=c)


class ArchiveView(PaginationMixin, ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'
    paginate_by = 5

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchiveView, self).get_queryset().filter(created_time__year=year,
                                                              created_time__month=month)


class TagView(PaginationMixin, ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'
    paginate_by = 5

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
