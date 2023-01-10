"""djviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url, include
from django.urls import re_path, include
from django.contrib import admin

# from blog.views import post_model_list_view

from .views import home, redirect_somewhere

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', home, name='home'),
    re_path(r'^redirect/$', redirect_somewhere, name='home'),
    # app controls all urls
    re_path(r'^blog/', include(('blog.urls', 'blog'), namespace='blog')),
    #url(r'^posts/$', post_model_list_view),
]
