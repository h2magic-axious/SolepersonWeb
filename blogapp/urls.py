from django.urls import path

from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from blogapp import views
from blogapp.models import Article

info_dict = {
    'queryset': Article.objects.all(),
    'date_field': 'created_time'
}

app_name = 'blog_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),

    path('sitemap.xml', sitemap, {
        'sitemaps': {
            'blog': GenericSitemap(info_dict, priority=0.6)
        }}, name='django.contrib.sitemaps.views.sitemap')
]
