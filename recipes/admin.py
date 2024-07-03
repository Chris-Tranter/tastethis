from django.contrib import admin
from .models import Recipe, Recipe_comment

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Recipe_comment)