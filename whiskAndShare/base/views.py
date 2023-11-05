from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from whiskAndShare import settings
from . import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

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
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            login(request,user)
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/signUp.html', context)

def loginFun(request):
    return render(request, 'base/login.html')

def deleteRecipe(request, id):
    if request.method == 'POST':
        models.Recipe.objects.get(id=id).delete()
        return redirect('profile')
    context = {}
    return render(request, 'base/deleteRecipe.html', context)