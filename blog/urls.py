from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('add/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
    path('delete/<int:comment>/', views.delete_comment, name='delete_comment')
]
