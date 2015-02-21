from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve

from search.views import home_page
from search.models import Search, Recipe

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_send_a_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['search_keyword_text'] = 'chicken soup'

        response = home_page(request)

        self.assertEqual(Search.objects.count(), 1)
        new_search = Search.objects.first()
        self.assertEqual(new_search.keyword, 'chicken soup')

    def test_home_page_redirects_after_POSt(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['search_keyword_text'] = 'chicken soup'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')        

    def test_home_page_only_saves_searches_when_necessary(self):
        request=HttpRequest()
        home_page(request)
        self.assertEqual(Search.objects.count(), 0)

class SearchModelTest(TestCase):

    def test_saving_and_retrieving_searches(self):
        first_search = Search('chicken soup')
        first_search.save() 

        second_search = Search('cookies')
        second_search.save()

        saved_searches = Search.objects.all()
        self.assertEqual(saved_searches.count(), 2)

        first_saved_search = saved_searches[0]
        second_saved_search = saved_searches[1]
        self.assertEqual(first_saved_search.keyword, 'chicken soup')
        self.assertEqual(second_saved_search.keyword, 'cookies') 

class APIRequestTest(TestCase):
    def test_sending_and_receiving_searches(self):
        new_search = Search()
