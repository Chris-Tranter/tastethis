from . import views
from django.urls import path

urlpatterns = [
    path('', views.join_me, name='join'),
]