from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import arriving

urlpatterns = [
    path('', arriving, name='arriving')
]
