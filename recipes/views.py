from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .forms import CommentForm
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
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(request, messages.SUCCESS,'Thanks your comment is under approval.')
    comment_form = CommentForm()
    return render(request,"recipes/recipe_detail.html",{"recipe": recipe, "comments":comments, "comment_form": CommentForm,})