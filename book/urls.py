from django.urls import path, re_path
from . import views

app_name='book'

urlpatterns = [
    path('',views.index, name='index'),
    path('list_book/', views.BookLisView.as_view(), name='booklist'),
    path('detail/<int:pk', views.BookDetailView.as_view(),name='bookdetail'),
    ]