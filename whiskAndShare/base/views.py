from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, JsonResponse
from . import models
from whiskAndShare import settings
from . import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.

def home(request):
    recipes = models.Recipe.objects.all()
    for recipe in recipes:
        recipe.body = recipe.body[0:200]
        recipe.body += '...'
        recipe.likes = recipe.like_set.all()
        recipe.comments = recipe.comment_set.all()
        recipe.liked = False
        for like in recipe.likes:
            if like.author == request.user:
                recipe.liked = True
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

def profile(request, id):
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(models.User, username = username, password=password)
        print(user)
        if user!=None:
            login(request,user)
            return redirect('home')
    return render(request, 'base/login.html')

def deleteRecipe(request, id):
    if request.method == 'POST':
        models.Recipe.objects.get(id=id).delete()
        return redirect(reverse('profile', args=[str(request.user.id)]))
    context = {}
    return render(request, 'base/deleteRecipe.html', context)


def recipe(request, id):
    recipe = models.Recipe.objects.get(id=id)
    print(recipe.image.url)
    context = {"recipe":recipe}
    return render(request,'base/recipe.html', context)


def incrementLikes(request, recipe_id):
    is_ajax = request.headers.get('X-requested-with') == 'XMLHttpRequest'

    if is_ajax:
        if request.method=='POST':
            models.Like.objects.create(recipe=models.Recipe.objects.get(id=recipe_id),author = request.user)
            return JsonResponse({"status":True})
        else:
            return JsonResponse({"status":False})
    return HttpResponseBadRequest('Invalid request')

def decrementLikes(request, recipe_id):
    is_ajax = request.headers.get('X-requested-with') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            models.Like.objects.get(recipe=models.Recipe.objects.get(id=recipe_id), author=request.user).delete()
            return JsonResponse({"status":False})
        else:
            return JsonResponse({"status":True})
    return HttpResponseBadRequest("Invalid Request")
