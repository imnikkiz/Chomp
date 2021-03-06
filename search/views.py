from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from models import Search, Recipe, UserProfile, Collection
from forms import UserForm


def home_page(request):
    """ Displays app front page. """
    return render_to_response('home.html')


def register_form(request):
    """ Provides user registration form. """
    context = RequestContext(request)
    user_form = UserForm()

    return render_to_response(
        'register.html',
        {'user_form': user_form},
        context)


def register(request):
    """ Registers user and user profile; 
    logs in user; redirects to welcome page.
    """
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


def login_form(request):
    """ Provides user login form."""
    context = RequestContext(request)
    return render_to_response('login.html', {}, context)


def login_user(request):
    """ Logs in returning user; redirects to welcome page."""
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


def logout_user(request):
    """ Logs out user; displays app front page."""
    logout(request)
    return HttpResponseRedirect('/')

def about_page(request):
    """ Provides app about page."""
    return render_to_response('about.html')

def recipe_main(request):
    """ User logged in; displays welcome page. """
    return render_to_response('recipe_main.html')

def landing_page(request):
    this_user_profile = UserProfile.objects.get(user=request.user)
    recipe_list = this_user_profile.recipes.all()
    if recipe_list:
        return HttpResponseRedirect('/my_recipes/')
    else:
        return HttpResponseRedirect('/search_page/')


def search_page(request): 
    """ Redirects to last search results or displays blank search page."""
    if request.session.get('search_keyword'):
        return redirect('/new_search/')
    else:
        return render_to_response('search.html')


def new_search(request):
    """ Retrieves and displays search results for keyword input.

    Assigns new input or last stored input to keyword.
    Queries database for search results; if no results, instantiates new search. 
    Assigns all (10) search results to recipe_list and stores keyword 
        in user's session.
    Handles error if keyword cannot produce search results.
    """
    keyword = (request.GET.get('search-keyword-text') or 
              request.session.get('search_keyword'))
    if keyword:
        search_exists = Search.objects.filter(keyword=keyword).first()

        if search_exists:
            search_has_recipes = search_exists.recipes.first()
            if not search_has_recipes:
                search_exists.delete()
                search_exists = False
        if not search_exists:

                new_search = Search.objects.create()
                new_search.search_by_keyword(keyword=keyword)


        this_search = Search.objects.get(keyword=keyword)
        recipe_list = this_search.recipes.all()
        request.session['search_keyword'] = keyword

    if (keyword and not recipe_list) or not keyword:
        recipe_list = "error"
        request.session['search_keyword'] = None

    return render_to_response("search.html", {
        'keyword': keyword,
        'recipe_list': recipe_list},
        context_instance=RequestContext(request)) 


def recipe_details(request, recipe_id):
    """ Queries database and displays recipe information and ingredient list."""
    this_recipe = Recipe.objects.get(id=recipe_id)
    ingredient_list = this_recipe.ingredients.all()

    return render(request, 'recipe_detail.html', {
        'recipe': this_recipe,
        'ingredients': ingredient_list
    })


def add_recipe(request):
    """ Adds recipe to user's collection. """
    this_user_profile = UserProfile.objects.get(user=request.user)
    this_recipe_id = request.GET.get('recipe_id')
    this_recipe = Recipe.objects.get(id=this_recipe_id)
    has_recipe = this_user_profile.recipes.filter(id=this_recipe_id).first()
    if not has_recipe:
        new_collection = Collection(user_profile=this_user_profile,
                                    recipe=this_recipe)
        new_collection.save()


def my_recipes(request):
    """ Queries database and displays all user's recipes."""
    this_user_profile = UserProfile.objects.get(user=request.user)
    recipe_list = this_user_profile.recipes.all()

    return render(request, 'my_recipes.html', {
        'recipe_list': recipe_list
        })


def remove_recipe(request):
    """ Removes recipe from user's collection."""
    recipe_id = request.GET.get("recipe_id")
    this_user_profile = UserProfile.objects.get(user=request.user)
    this_recipe = Recipe.objects.get(id=recipe_id)
    Collection.objects.filter(user_profile=this_user_profile,
                                    recipe=this_recipe).delete()
    
    recipe_list = this_user_profile.recipes.all()
    return render(request, 'my_recipes.html', {
        'recipe_list': recipe_list
        })


def add_to_planner(request):
    """ Adds 'planning' to day_planned attribute for the user's collection 
        of this recipe.

    All recipes with day_planned assigned will be displayed in Planner.
    """
    recipe_id = request.GET.get("recipe_id")
    this_recipe = Recipe.objects.get(id=recipe_id)
    this_user_profile = UserProfile.objects.get(user=request.user)
    user_recipe = Collection.objects.filter(user_profile=this_user_profile,
                                            recipe=this_recipe).first()
    user_recipe.day_planned = "planning"
    user_recipe.save()


def update_planner(request):
    """ Updates day_planned attribute for the user's collection of this recipe.

    'deleted' will clear the attribute and the recipe will no longer be 
        displayed in the Planner.
    """
    recipe_id = request.GET.get("recipe_id")
    this_recipe = Recipe.objects.get(id=recipe_id)
    this_user_profile = UserProfile.objects.get(user=request.user)
    user_recipe = Collection.objects.filter(user_profile=this_user_profile,
                                            recipe=this_recipe).first()
    day = request.GET.get("day")
    if day == 'deleted':
        user_recipe.day_planned = None
        user_recipe.save()
        return redirect("/planner/")
    else:    
        user_recipe.day_planned = day
        user_recipe.save()



def planner(request):
    """ Queries database and displays recipes able to be planned. """
    this_user_profile = UserProfile.objects.get(user=request.user)
    recipe_planning_dict = {
            'planning': [],
            'monday': [],
            'tuesday': [], 
            'wednesday': [], 
            'thursday': [], 
            'friday': [], 
            'saturday': [], 
            'sunday': []
            }

    user_recipes = Collection.objects.filter(
            user_profile=this_user_profile).exclude(
            day_planned__isnull=True).all().prefetch_related('recipe')
    for user_recipe in user_recipes:
        recipe_planning_dict[user_recipe.day_planned].append(user_recipe.recipe)

    return render(request, 'planner.html', {
        'recipes': recipe_planning_dict
        })


def shopping_list(request):
    """ Queries database and displays planned recipes' ingredients in categories."""
    this_user_profile = UserProfile.objects.get(user=request.user)
    
    category_dict = {
        'baking': {},
        'beverages': {},
        'condiments': {},
        'dairy': {},
        'fish': {},
        'grains': {},
        'grocery': {},
        'meat': {},
        'nuts': {},
        'produce': {},
        'spices': {},
        'other': []
    }

    planned_recipes = Collection.objects.filter(
            user_profile=this_user_profile).exclude(
            day_planned__isnull=True).exclude(day_planned='planning').all()
    if planned_recipes:
        for collection in planned_recipes:
            recipe = collection.recipe
            ingredient_list = recipe.ingredients.all()

            for ingredient in ingredient_list:
                if ingredient.food:
                    food_name = ingredient.food.name
                    category_name = ingredient.food.category.name
                    amount = ingredient.amount
                    if amount:
                        if amount.is_integer():
                            amount = int(amount)
                    measurement = ingredient.measurement

                    if food_name not in category_dict[category_name]:
                        category_dict[category_name][food_name] = {
                            'measurements': {},
                            'ingredients': []
                        }
                    if measurement:
                        if amount:
                            category_dict[category_name][food_name]['measurements'][measurement] = (
                                category_dict[category_name][food_name]['measurements'].get(
                                        measurement, 0) + amount)
                        else:
                            category_dict[category_name][food_name]['measurements'][measurement] = (
                                category_dict[category_name][food_name]['measurements'].get(
                                        measurement, 0) + 1)
                    else:
                        if amount:
                            category_dict[category_name][food_name]['other']=(
                                category_dict[category_name][food_name].get(
                                        'other', 0) + amount)
                        else:
                            category_dict[category_name][food_name]['other']=(
                                category_dict[category_name][food_name].get(
                                        'other', 0) + 1)

                    category_dict[category_name][food_name]['ingredients'].append(ingredient)
                else:
                    category_dict['other'].append(ingredient)
    else: 
        category_dict = None
        
            

    return render(request, 'shopping_list.html', {
        'category_dict': category_dict
        })