from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'home.html', {
        'new_search_keyword': request.POST.get('search_keyword_text', '')
    })