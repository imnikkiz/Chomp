from django.shortcuts import render
from search.models import Keyword

def home_page(request):
    if request.method == 'POST':
        new_search_keyword = request.POST['search_keyword_text']
        Keyword.objects.create(text=new_search_keyword)
    else:
        new_search_keyword = ''

    return render(request, 'home.html', {
        'new_search_keyword': new_search_keyword
    })