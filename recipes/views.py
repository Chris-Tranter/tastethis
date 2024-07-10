from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from django.utils.text import slugify
from .forms import CommentForm, RecipeForm
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

class AddRecipe(View):
    """ add recipe"""
    def get(self, request):
        """What happens for a GET request"""
        return render(
            request, "recipes/add_recipe.html", {"recipe_form": RecipeForm()})

    def post(self, request):
        """What happens for a POST request"""
        recipe_form = RecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify('-'.join([recipe.title,
                                            str(recipe.author)]),
                                  allow_unicode=False)
            recipe.save()
            print('saved')
            return redirect('add_recipe')
        else:
            print('error')
            messages.error(self.request, 'Please complete all required fields')
            recipe_form = RecipeForm()

        return render(
            request,
            "recipes/add_recipe.html",
            {
                "recipe_form": recipe_form

            },
        )