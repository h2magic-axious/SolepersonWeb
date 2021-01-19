from django.urls import path

from administrator import views

app_name = 'admin'
urlpatterns = [
    path('', views.admin_index, name="admin_index")
]