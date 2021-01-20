from django.urls import path

from blogapp import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:pk>/', views.detail, name='detail'),
]
