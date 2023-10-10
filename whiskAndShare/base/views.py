from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

recipes = [
    {"title":'Cheesecake', "body":'lorem ipsum'},
    {"title":'Hashbrowns', "body":'lorem ipsum'}

]

def home(request):
    context = {'recipes':recipes}
    return render(request, 'base/home.html', context)