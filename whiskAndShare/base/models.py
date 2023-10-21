from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(blank=True, upload_to='static/images')

    def __str__(self):
        return self.title