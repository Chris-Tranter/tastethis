from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Join(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"


class JoinRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} would like to join TASTE TEEZ!"