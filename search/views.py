from django.shortcuts import render
from search.models import Search, Recipe, link_ingredient_to_recipe

def home_page(request):
    """ Add search keyword to database, return list of recipe names."""
    
    recipe_list = []

    if request.method == 'POST':
        keyword = request.POST['search_keyword_text']
        if Search.objects.filter(keyword=keyword):
            this_search = Search.objects.get(keyword=keyword)
            recipe_list = this_search.recipes.all()
        else:
            new_search = Search.objects.create()
            new_search.search_by_keyword(keyword=keyword)

            for recipe in new_search.response['matches'][0:3]:
                new_recipe = Recipe.objects.create()
                new_recipe.get_recipe_by_yummly_id(yummly_id=recipe.get('id'))
                new_search.recipes.add(new_recipe)
                recipe_list.append(new_recipe)
                link_ingredient_to_recipe(new_recipe.id)

    return render(request, 'home.html', {
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