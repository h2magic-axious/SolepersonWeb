from django.urls import path
from comment import views

app_name = 'comment'
urlpatterns = [
    path('comment/<int:article_pk>/', views.comment, name='comment')
]
