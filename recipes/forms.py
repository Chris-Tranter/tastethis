from .models import Recipe_comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    """ Recipe Comment Form """
    class Meta:
        """ fields for Recipe Comment form """
        
        model = Recipe_comment
        fields = ("comment",)


class RecipeForm(forms.ModelForm):
    """ Recipe Form """

    class Meta:
        """ fields for recipe form """

        model = Recipe
        fields = (
            "title",
            "ingredients",
            "cooking_steps",
            "freezable",
            "cooking_steps",
            "prep_time",
            "cook_time",
            "servings",
            "cook_time",
            "status",
        )
