from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "not-posted"), (1, "Posted"))

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    ingredients = models.TextField()
    cooking_steps = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated = models.DateTimeField(auto_now=True)