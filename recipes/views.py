from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe, Recipe_comment

class Recipelist(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by("created")
    template_name = "recipes/index.html"
    paginate_by = 4

def recipe_detail(request, slug):
    """
    
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = Recipe_comment.objects.filter(recipe=recipe)
    return render(request,"recipes/recipe_detail.html",{"recipe": recipe, "comments":comments,})
