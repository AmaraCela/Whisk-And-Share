from django.forms import ModelForm
from . import models

class FormRecipe(ModelForm):
    class Meta:
        model = models.Recipe
        fields = '__all__'
        