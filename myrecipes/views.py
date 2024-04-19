import random

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from myrecipes.forms import Users, RegistrationUser, RecipeForm
from myrecipes.models import Recipe


def logout_user(request):
    logout(request)
    return redirect('main')


def login_user(request):
    context = {'form': Users(), }
    if request.method == 'POST':
        form = Users(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            auth_user = authenticate(request, username=user, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('main')
            else:
                context['msg'] = 'или пользователя такого нет или пароль не тот'

    return render(request, 'myrecipes/autorisation.html', context=context)


def main(request):
    rand = random.sample(list(Recipe.objects.all()), k=5)

    context = {
        'recipes': rand,
        'title': 'главная',
        'name_page': 'рецепты блюд',
    }
    return render(request, 'myrecipes/main.html', context=context)


def registration(request):
    if request.method == "POST":
        form = RegistrationUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'myrecipes/registration_ok.html')
    else:
        form = RegistrationUser()
    return render(request, 'myrecipes/registration.html', context={'form': form})


def fill_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = request.user
            new_recipe.save()
            return render(request, 'myrecipes/browse.html',
                          {'recipe': Recipe.objects.get(pk=new_recipe.pk)})
    else:
        form = RecipeForm()
    return render(request, 'myrecipes/load_forms.html', {'form': form})


def browse(request, recipe_id):
    context = {
        'recipe': Recipe.objects.get(pk=recipe_id),
        'title': 'просмотр рецепта',
    }
    return render(request, 'myrecipes/browse.html', context)


def edit(request, recipe_id):
    if request.method == 'POST':
        recipe = Recipe.objects.get(pk=recipe_id)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe.save()
            return redirect('browse', recipe_id)
    else:
        mod = Recipe.objects.get(pk=recipe_id)
        form = RecipeForm(instance=mod)
    return render(request, 'myrecipes/load_forms.html', {'form': form, 'title': 'изменяем рецепт'})


def delete(request, recipe_id):
    Recipe.objects.filter(pk=recipe_id).delete()
    return redirect('main')
