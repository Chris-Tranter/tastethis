from django.shortcuts import render
from django.views import generic
from .models import Recipe

class Recipelist(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by("created")
    template_name = "recipe_list.html"