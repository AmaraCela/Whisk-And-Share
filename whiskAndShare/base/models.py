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

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:30]

class Reply(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    main_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)