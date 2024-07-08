from django.db import models
from django.contrib.auth.models import User

class Join(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title