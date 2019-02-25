"""scrapeimdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers

from scrape.views import home_view, product_view, product_details, product_delete, export_file
from scrape import views


router = routers.DefaultRouter()
router.register(r'movie', views.MovieView)
router.register(r'role', views.RoleView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name="home"),
    path('movie/', include(router.urls)),
    path('', product_view, name="product"),
    path('details/<int:id>', product_details, name="details"),
    path('download/<int:id>', export_file, name="download"),
    path('delete/<int:id>', product_delete, name="delete"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
            ]
