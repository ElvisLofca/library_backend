from django.urls import include, path
from rest_framework import routers
from base.views import base_views as views

urlpatterns = [
    path('', views.get_routes, name='routes'),
]