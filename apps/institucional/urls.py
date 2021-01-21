from django.urls import path
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.institucional, name='institucional'),
    # url(r'^data/(?P<idx>\w+)/$', views.index2, name='index2'),
]
