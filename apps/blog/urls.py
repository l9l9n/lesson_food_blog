from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/list', CategoryListView.as_view(), name='category_list'),
    path('post/list/', PostListView.as_view(), name='post_list'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]