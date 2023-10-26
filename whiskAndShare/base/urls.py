from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addRecipe/',views.addRecipe, name = 'addRecipe'),
    path('profile/', views.profile, name = 'profile'),
    path('signUp/', views.signUp, name='signUp'),
    path('login/',views.login, name = 'login'),
    path('deleteRecipe/<str:id>', views.deleteRecipe, name='deleteRecipe'),
]