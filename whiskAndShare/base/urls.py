from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addRecipe/',views.addRecipe, name = 'addRecipe'),
    path('profile/', views.profile, name = 'profile')
]