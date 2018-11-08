from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import thedetainees

urlpatterns = [
    path('', thedetainees, name= 'the_detainees')
]
