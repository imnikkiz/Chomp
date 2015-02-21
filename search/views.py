from django.shortcuts import redirect, render
from search.models import Search, Recipe

def home_page(request):
    """ Add search keyword to database, return list of recipe names."""
    
    recipe_list = []

    if request.method == 'POST':
        new_search = Search.objects.create()
        new_search.search_by_keyword(keyword=request.POST['search_keyword_text'])

        for recipe in new_search.response['matches']:
            new_recipe = Recipe.objects.create()
            new_recipe.get_recipe_by_yummly_id(yummly_id=recipe.get('id'))
            new_search.recipes.add(new_recipe)
            recipe_list.append(new_recipe)

    return render(request, 'home.html', {
        'recipe_list': recipe_list
    })

#TODO redirect after POST