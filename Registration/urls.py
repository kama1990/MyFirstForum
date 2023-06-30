
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('createNewPosts/', views.createNewPosts, name='createNewPosts'),
    path('<int:postId>/', views.detail, name='detail'),
    path('<int:postId>/delete/', views.deletePost, name='deletePost'),
]