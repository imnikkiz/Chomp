from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from models import Search, Recipe, UserProfile, Collection
from forms import UserForm
import logging

def home_page(request):
    """ Home page renders home.html with fully loaded partials"""
    return render_to_response('home.html')


def register(request):
    """ Register"""
    context = RequestContext(request)
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            login(request, new_user)
            return HttpResponseRedirect('/recipe_main')
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render_to_response(
        'register.html',
        {'user_form': user_form},
        context)


def login_user(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/recipe_main')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid username or password.")
    else:
        return render_to_response('login.html', {}, context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def recipe_main(request):
    return render_to_response('recipe_main.html')

def search_page(request):  
    keyword = request.GET.get('search_keyword_text')
    if not keyword:
        keyword = request.session.get('search_keyword')
    if keyword:
        search_exists = Search.objects.filter(keyword=keyword).first()
        if search_exists:
            search_has_recipes = search_exists.recipes.first()
            if not search_has_recipes:
                search_exists.delete()
                search_exists = False

        if not search_exists:
            new_search = Search.objects.create()
            search_response = new_search.search_by_keyword(keyword=keyword)

            for recipe in search_response.get('matches'):
                new_recipe = Recipe.objects.create()
                new_recipe.get_recipe_by_yummly_id(yummly_id=recipe.get('id'))
                new_recipe.link_ingredients_to_recipe()
                new_recipe.assign_attributes_to_recipe()
                new_search.recipes.add(new_recipe)

        this_search = Search.objects.get(keyword=keyword)
        request.session['search_keyword'] = keyword

        recipe_list = this_search.recipes.all()[:3]

        # TODO: view more results
        # TODO: after 10th result, option to find more
        return render_to_response("search.html", {
            'recipe_list': recipe_list})
    else:
        return render_to_response('search.html')

def recipe_details(request, recipe_id):
    recipe_id = recipe_id
    this_recipe = Recipe.objects.get(id=recipe_id)

    ingredient_list = this_recipe.ingredients.all()

    return render(request, 'recipe_detail.html', {
        'recipe': this_recipe,
        'ingredients': ingredient_list
    })


def my_recipes(request):
    this_user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'GET':
        this_recipe_id = request.GET.get('recipe_id')
        if this_recipe_id:
            this_recipe = Recipe.objects.get(id=this_recipe_id)
            has_recipe = this_user_profile.recipes.filter(id=this_recipe_id).first()
            if not has_recipe:
                new_collection = Collection(user_profile=this_user_profile,
                                            recipe=this_recipe)
                new_collection.save()
        recipe_list = this_user_profile.recipes.all()[:10]

    return render(request, 'my_recipes.html', {
        'recipe_list': recipe_list
        })

def planner(request):
    recipe_list = []
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    if request.method == 'GET':
        recipe_id_list = request.GET.getlist("recipe_list")
        if recipe_id_list:
            for recipe_id in recipe_id_list:
                recipe = Recipe.objects.get(id=recipe_id)
                recipe_list.append(recipe)

    return render(request, 'planner.html', {
        'recipe_list': recipe_list,
        'days': days
        })

def shopping_list(request):
    recipe_list = {}

    if request.method == 'GET':
        recipe_id_list = request.GET.getlist("recipe_list")
        for recipe_id in recipe_id_list:
            recipe = Recipe.objects.get(id=recipe_id)
            recipe_name = recipe.name
            ingredient_list = recipe.ingredients.all()
            recipe_list[recipe_name] = ingredient_list
    return render(request, 'shopping_list.html', {
        'recipe_list': recipe_list
        })


