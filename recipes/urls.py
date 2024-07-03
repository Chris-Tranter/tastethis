from . import views
from django.urls import path

urlpatterns = [
    path('', views.Recipelist.as_view(), name='home'),
]