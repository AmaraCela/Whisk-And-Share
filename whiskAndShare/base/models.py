from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(blank=True, upload_to='static/images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:30]