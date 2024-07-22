from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "not-posted"), (1, "Posted"))

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    ingredients = models.TextField(max_length=600, unique=True)
    image = CloudinaryField('image', default='placeholder')
    #likes =
    cooking_steps = models.TextField(max_length=1200, unique=True)
    freezable = models.BooleanField(default=False)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    servings = models.PositiveIntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('recipe_detail', args=[self.slug])

class Meta:
        ordering = ["-created"]

def __str__(self):
        return f"{self.title} especially crafted by {self.author},"


class Recipe_comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="++")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+++")
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

class Meta:
        ordering = ["-recipe"]

