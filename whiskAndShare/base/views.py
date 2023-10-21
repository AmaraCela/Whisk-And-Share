from django.shortcuts import render
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
            form.save()
    context = {"form":form}
    return render(request, 'base/addRecipes.html', context)
    # form = RoomForm()
    # if request.method == 'POST':
    #     form = RoomForm(request.POST)
    #     if form.is_valid():
    #         room = form.save(commit = False)
    #         room.host = request.user
    #         room.save()
    #         return redirect('home')