from django.db import models
from django.contrib.auth.models import User

PREPTIME = (
    (1, 5),
    (2, 10),
    (3, 15),
    (4, 20),
    (5, 25),
    (6, 30),
)

COOKTIME = (
    (1, 5),
    (2, 10),
    (3, 15),
    (4, 20),
    (5, 30),
    (6, 45),
    (7, 60),
    (8, 120),
)

SERVINGS = (
    (1, 1),
    (2, 2),
    (3, 4),
    (4, 8),
)

STATUS = ((0, "not-posted"), (1, "Posted"))

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    ingredients = models.TextField(max_length=200, unique=True)
    #image = 
    #likes =
    cooking_steps = models.TextField(max_length=600, unique=True)
    freezable = models.BooleanField(default=False)
    prep_time = models.IntegerField(choices=PREPTIME, default=1)
    cook_time = models.IntegerField(choices=COOKTIME, default=1)
    servings = models.IntegerField(choices=SERVINGS, default=1)
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