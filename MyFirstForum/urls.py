"""
URL configuration for MyFirstForum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Registration import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('MainUser.urls')),
    path('', include('Registration.urls')),
    path('post/', views.post, name='post'),
    path('myOwn/', views.myOwn, name='myOwn'),
    path('createNewPosts/', views.createNewPosts, name='createNewPosts'),
    path('<int:postId>/', views.detail, name='detail'),
    path('<int:postId>/delete/', views.deletePost, name='deletePost'),
    path('<int:postId>/detailPost/', views.detailPost, name='detailPost'),    
    path('<int:postId>/createAnswerPost/', views.createAnswerPost, name='createAnswerPost'),    
    path('<int:commentId>/editAnswerPost/', views.editAnswerPost, name='editAnswerPost'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
