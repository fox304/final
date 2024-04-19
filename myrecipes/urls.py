from django.urls import path
from myrecipes import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('recipe/', views.fill_recipe, name='recipe'),
    path('browse/<int:recipe_id>/', views.browse, name='browse'),
    path('edit/<int:recipe_id>/', views.edit, name='edit'),
    path('delete/<int:recipe_id>/', views.delete, name='delete'),



]