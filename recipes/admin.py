from django.contrib import admin
from .models import Recipe, Recipe_comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = (
        "title",
        "author",
        "created",
        "status",
    )
    search_fields = ["title"]
    list_filter = (
        "title",
        "author",
        "created",
        "status",
    )
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = (
        "ingredients",
        "cooking_steps",
    )


admin.site.register(Recipe_comment)
class Recipe_comment(SummernoteModelAdmin):

    list_display = (
    "recipe",
    "author",
    "comment",
    "created",
)
    search_fields = ["title"]
    list_filter = (
        "recipe",
        "author",
        "created",
    )

    summernote_fields = (
        "comment",
    )