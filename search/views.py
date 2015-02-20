from django.shortcuts import render
from search.models import Keyword, Recipe, search_yummly_recipes_by_keyword

def home_page(request):
    if request.method == 'POST':
        new_search_keyword = request.POST['search_keyword_text']
        # Keyword.objects.create(text=new_search_keyword)
        recipe_list = search_yummly_recipes_by_keyword(new_search_keyword)
    else:
        recipe_list = []

    return render(request, 'home.html', {
        'recipe_list': recipe_list
    })