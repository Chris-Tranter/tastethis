from django.contrib import admin
from .models import Recipe, Recipe_comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'created', 'status',)
    search_fields = ['title']
    list_filter = ('title', 'author', 'created', 'status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'cooking_steps',)

# Register your models here.
admin.site.register(Recipe_comment)