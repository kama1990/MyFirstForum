
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('myOwn/', views.myOwn, name='myOwn'),
    path('createNewPosts/', views.createNewPosts, name='createNewPosts'),
    path('<int:postId>/', views.detail, name='detail'),
    path('<int:postId>/delete/', views.deletePost, name='deletePost'),
    path('<int:postId>/detailPost/', views.detailPost, name='detailPost'),    
   
]
