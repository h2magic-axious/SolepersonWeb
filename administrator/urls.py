from django.urls import path

from administrator import views

app_name = 'admin'
urlpatterns = [
    path('category-list/', views.category_list),
]
