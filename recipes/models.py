from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "not-posted"), (1, "Posted"))

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    ingredients = models.TextField(max_length=200, unique=True)
    cooking_steps = models.TextField(max_length=600, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated = models.DateTimeField(auto_now=True)

class Meta:
        ordering = ["-created"]

def __str__(self):
        return f"{self.title} especially crafted by {self.author},"


class Recipe_comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="++")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+++")
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

class Meta:
        ordering = ["-recipe"]

def __str__(self):
        return f"{self.author} has written {self.comment}"