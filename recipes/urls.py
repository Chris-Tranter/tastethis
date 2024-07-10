from . import views
from django.urls import path

urlpatterns = [
    path('', views.Recipelist.as_view(), name='home'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('add_recipe', views.AddRecipe.as_view(), name='add_recipe'),           
]