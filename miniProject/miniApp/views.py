from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import mealForm, userForm
from .models import mealModel, userModel


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = userModel.objects.get(name=request.user)
        userRecipes = mealModel.objects.filter(creator=user)

    else:
        userRecipes = ''
    context = {
        'userRecipes': userRecipes
    }

    return render(request, 'miniApp/index.html', context)


# GRABS ALL RECIPES AND INJECTS TO ALL RECIPES PAGE
def allrecipes(request):
    recipes = mealModel.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'miniApp/allrecipes', context)


# INJECTS MEALFORM INTO NEW RECIPE PAGE AND CREATE A NEW MODEL OBJECTS
def newrecipe(request):
    form = mealForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST':
        user = userModel.objects.get(name=request.user)
        mealModel.objects.create(request.POST['name'], request.POST['description'], request.POST['ingredients'],
                                 request.POST['directions'], request.POST['created'], request.POST['pictureURL'],
                                 creator=user)
        return redirect('index')
    return render(request, 'miniApp/newrecipe.html', context)


# GRABS LOGGED IN USER AND INJECTS INFO TO PAGE
def profile(request):
    if request.user.is_authenticated:
        usercurrent = userModel.objects.get(name=request.user)
        user = userModel.objects.get(name=usercurrent)

    else:
        user = ''
    context = {
        'user': user
    }
    return render(request, 'miniApp/profile.html', context)


# INJECTS FORM TO NEW USER PAGE AND CREATES USER
def newuser(request):
    form = userForm(request.POST or None)
    context = {
        'form': form
    }

    if request.method == "POST":
        print(request.POST)
        User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        return render(request, 'index')

    return render(request, 'miniApp/newuser.html', context)


# GRABS RECIPE BY PRIMARY KEY AND INJECTS TO DETAILS PAGE
def details(request, ID):
    recipe = get_object_or_404(mealModel, pk=ID)
    context = {
        'recipe': recipe
    }
    return render(request, 'miniApp/details.html', context)


# GRABS USER AND IJECTS FORM TO EDIT
def edituser(request, ID):
    editme = get_object_or_404(userModel, pk=ID)
    form = userForm(request.POST or None, instance=editme)
    context = {
        'form': form
    }

    if request.method == "POST":
        form.save()
        return redirect('index')
    return render(request, 'miniApp/edituser.html', context)


def editrecipe(request, ID):
    editme = get_object_or_404(mealModel, pk=ID)
    form = mealForm(request.POST or None, instance=editme)
    context = {
        'form': form
    }

    if request.method == "POST":
        form.save()
        return redirect('index')

    return render(request, 'miniApp/newrecipe.html', context)
