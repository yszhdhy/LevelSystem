"""
URL configuration for LevelSystem project.

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
from django.urls import path

from LevelApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 表示用户一访问此接口 就会去到我们注册的app中的 views文件中寻找index函数并执行
    path('html/', views.html),
    path('baidu/', views.baidu),
    path('upload_photo/', views.upload_photo),
    path('photograph/', views.photograph, name='photograph'),
    path('openCamera/', views.openCamera, name='openCamera'),
    path('closeCamera/', views.closeCamera, name='closeCamera'),
    path('get_list/', views.get_list, name='get_list'),
    path('save/', views.save, name='save'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('pp_upload/', views.pp_upload, name='pp_upload'),
    path('statistical_errors/', views.statistical_errors, name='statistical_errors'),
    path('pp_photograph/', views.pp_photograph, name='pp_photograph'),
]
