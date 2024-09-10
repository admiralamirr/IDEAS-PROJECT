

from django.urls import path

from . import views

urlpatterns=[
    path('Register', views.index, name='Register')
    ]