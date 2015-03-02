from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from models import Search, Recipe
from forms import UserForm
import json


def home_page(request):
    return render(request, 'home.html', {})


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return render_to_response('login.html', {}, context)
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render_to_response(
        'register.html',
        {'user_form': user_form,
         'registered': registered},
        context)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        user = json.loads(request.body)
        username = user['username']
        password = user['password']
        user = authenticate(username=username, password=password)
        if user:
            print user
            print "User is valid."
            if user.is_active:
                print "User is active."
                login(request, user)
                print "User is logged in."
                print user
                return HttpResponse(json.dumps(user))
    else:
        return render_to_response('login.html', {})

def search_page(request):
    return render(request, 'search.html')


def results_page(request):   
    if request.method == 'POST':
        keyword = request.POST['search_keyword_text']

        # Keyword not in database
        if not Search.objects.filter(keyword=keyword):
            new_search = Search.objects.create()
            search_response = new_search.search_by_keyword(keyword=keyword)

            for recipe in search_response['matches']:
                new_recipe = Recipe.objects.create()
                new_recipe.get_recipe_by_yummly_id(yummly_id=recipe.get('id'))
                new_recipe.link_ingredients_to_recipe()
                new_search.recipes.add(new_recipe)

        this_search = Search.objects.get(keyword=keyword)
        recipe_list = this_search.recipes.all()[:3]

        # TODO: view more results
        # TODO: after 10th result, option to find more

    return render(request, 'search.html', {
        'recipe_list': recipe_list
    })    


def recipe_details(request, recipe_id):
    recipe_id = recipe_id
    this_recipe = Recipe.objects.get(id=recipe_id)

    ingredient_list = this_recipe.ingredients.all()

    return render(request, 'recipe_detail.html', {
        'recipe': this_recipe,
        'ingredients': ingredient_list
    })


def my_recipes(request):
    if request.method == 'POST':
        this_recipe_id = request.POST['recipe_id']
        this_recipe = Recipe.objects.get(id=this_recipe_id)
        # flash('Recipe added!')
        # add to db

    return render(request, 'my_recipes.html')

def planner(request):
    return render(request, 'planner.html', {})

def shopping_list(request):
    return render(request, 'shopping_list.html', {})


