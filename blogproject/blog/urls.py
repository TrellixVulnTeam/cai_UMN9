from django.conf.urls import url
from .import views
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
]