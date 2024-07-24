from . import views
from django.urls import path

urlpatterns = [
    path("", views.Recipelist.as_view(), name="home"),
    path("<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    path("add_recipe", views.AddRecipe.as_view(), name="add_recipe"),
    path("update_recipe/<int:pk>", views.UpdateRecipe.as_view(), name="update_recipe"),
    path("delete_recipe/<int:recipe_id>", views.delete_recipe, name="delete_recipe"),
    path("my_recipes", views.MyRecipes.as_view(), name="my_recipes"),
]
