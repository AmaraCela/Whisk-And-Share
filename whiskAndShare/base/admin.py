from django.contrib import admin
from .models import Recipe
from .models import Comment
from .models import Reply
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Reply)