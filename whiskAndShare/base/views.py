from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from whiskAndShare import settings
from . import forms



# Create your views here.



def home(request):
    recipes = models.Recipe.objects.all()
    context = {'recipes':recipes}
    return render(request, 'base/home.html', context)

def addRecipe(request):
    form = forms.FormRecipe()
    
    if request.method=='POST':
        form = forms.FormRecipe(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    context = {"form":form}
    return render(request, 'base/addRecipes.html', context)

def profile(request):
    user = None
    user = request.user
    recipes = models.Recipe.objects.filter(author = request.user)
    context = {'user':user, 'recipes':recipes}
    return render(request, 'base/profile.html',context)


def signUp(request):
    return render(request, 'base/signUp.html')

def login(request):
    return render(request, 'base/login.html')

def deleteRecipe(request, id):
    if request.method == 'POST':
        models.Recipe.objects.get(id=id).delete()
        return redirect('profile')
    context = {}
    return render(request, 'base/deleteRecipe.html', context)