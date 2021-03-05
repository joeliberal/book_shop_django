from django.urls import path
from .api_views import ApiBook, AUDBook

app_name='api'

urlpatterns =[
    path('list/', ApiBook.as_view(),name='api-list-book'),
    path('update/<int:pk>/', AUDBook.as_view(),name'audbook'),
]