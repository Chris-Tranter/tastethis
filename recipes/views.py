from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import (TemplateView, CreateView, ListView, DeleteView, UpdateView)
from django.db.models import Q
from .models import Recipe, Recipe_comment
from .forms import RecipeForm, CommentForm

class Recipelist(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by("-created")
    template_name = "recipes/index.html"
    paginate_by = 4

def recipe_detail(request, slug):
    """
    Recipe detail page
    """

    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)
    comments = Recipe_comment.objects.filter(recipe=recipe)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            return HttpResponseRedirect(reverse('home'))
            messages.add_message(request, messages.SUCCESS,'Thanks your comment is under approval.')
    comment_form = CommentForm()
    return render(request,"recipes/recipe_detail.html",{"recipe": recipe, "comments":comments, "comment_form": CommentForm,})

class AddRecipe(View):
    """ add recipe"""
    def get(self, request):
        """a GET request"""
        return render(
            request, "recipes/add_recipe.html", {"recipe_form": RecipeForm()})

    def post(self, request):
        """a POST request"""
        recipe_form = RecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify('-'.join([recipe.title,
                                            str(recipe.author)]),
                                  allow_unicode=False)
            recipe.save()
            print('saved')
            return redirect('home')
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


class UpdateRecipe(UpdateView):
    """ Edit Recipe """
    model = Recipe
    template_name = 'recipes/update_recipe.html'
    form_class = RecipeForm

def delete_recipe(request, recipe_id):
    """Deletes recipe"""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect(reverse('home'))

class MyRecipes(View):
    """ view for user recipes page"""

    def get(self, request):
        """my recipes view, get method"""
        if request.user.is_authenticated:
            recipes = Recipe.objects.filter(status=0, author=request.user)
        
        context = {
            'recipes': recipes,
        }

        return render(request, 'recipes/my_recipes.html', context)



