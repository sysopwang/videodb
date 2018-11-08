"""demo01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/$',views.index,name="index"),
    
    # 视频库
    url(r'^repo/$',views.repo_base,name="repo_base"),
    url(r'^repo/type$',views.repo_1,name="repo_type"),
    url(r'^repo/style$',views.repo_2,name="repo_style"),
    url(r'^repo/business$',views.repo_3,name="repo_business"),
    url(r'^repo/media$',views.repo_4,name="repo_media"),
    url(r'^repo/year$',views.repo_5,name="repo_year"),
    url(r'^repo/consumer$',views.repo_6,name="repo_consumer"),
    
    url(r'^case_change/$',views.case_change,name="case_change"),
    url(r'^upload_material/',views.upload_material,name="upload_material"),
    url(r'^analyzing/$',views.analyzing,name='analyzing'),
    url(r'^display_case_parameter/',views.display_case_parameter,name='parameter'),
    
    
    
]
