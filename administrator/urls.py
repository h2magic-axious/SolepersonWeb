from django.urls import path

from administrator import views

app_name = 'admin'
urlpatterns = [
    path('', views.admin_index, name="admin_index"),
    path('article_edit/', views.admin_article_edit, name='admin_article_edit'),
    path('categories_list/', views.admin_categories, name='admin_categories_list'),
    path('tags_list/', views.admin_tags, name='admin_tags_list'),
    # Form urls
    path('form/category/edit/<int:pk>/', views.admin_category_post, name='admin_category_edit'),
]
