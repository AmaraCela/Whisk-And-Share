from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addRecipe/',views.addRecipe, name = 'addRecipe'),
    path('profile/<str:id>', views.profile, name = 'profile'),
    path('signUp/', views.signUp, name='signUp'),
    path('login/',views.loginFun, name = 'login'),
    path('deleteRecipe/<str:id>', views.deleteRecipe, name='deleteRecipe'),
    path('recipe/<str:id>', views.recipe, name='recipe'),
    path('like/<str:recipe_id>',views.incrementLikes, name='like'),
    path('unlike/<str:recipe_id>',views.decrementLikes, name='unlike'),
]