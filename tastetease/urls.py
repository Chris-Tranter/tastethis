from django.contrib import admin
from django.urls import path
from recipes.views import my_recipe
urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', my_recipe, name='recipes'),
]
