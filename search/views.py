from django.shortcuts import render
from search.models import Search, Recipe

def home_page(request):
    if request.method == 'POST':
        keyword = request.POST['search_keyword_text']
        new_search = Search()
        recipe_list = new_search.search_by_keyword(keyword)
    else:
        recipe_list = []

    return render(request, 'home.html', {
        'recipe_list': recipe_list
    })