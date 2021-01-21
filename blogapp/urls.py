from django.urls import path

from blogapp import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag')
]
