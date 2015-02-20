from django.shortcuts import redirect, render
from search.models import Search, Recipe

def home_page(request):
    if request.method == 'POST':
        keyword = request.POST['search_keyword_text']
        new_search = Search.objects.create(keyword=request.POST['search_keyword_text'])
        recipe_list = new_search.search_by_keyword(keyword)
        return redirect('/')

    return render(request, 'home.html')