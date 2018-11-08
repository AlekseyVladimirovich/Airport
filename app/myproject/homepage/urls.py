from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('/', posts_list_url, name='posts_list_url')
]
