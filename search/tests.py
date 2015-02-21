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

    def test_home_page_only_saves_searches_when_necessary(self):
        request=HttpRequest()
        home_page(request)
        self.assertEqual(Search.objects.count(), 0)


class SearchModelTest(TestCase):

    def test_saving_and_retrieving_searches(self):
        first_search = Search()
        first_search.keyword = 'chicken soup'
        first_search.save() 

        second_search = Search()
        second_search.keyword = 'cookies'
        second_search.save()

        saved_searches = Search.objects.all()
        self.assertEqual(saved_searches.count(), 2)

        first_saved_search = saved_searches[0]
        second_saved_search = saved_searches[1]
        self.assertEqual(first_saved_search.keyword, 'chicken soup')
        self.assertEqual(second_saved_search.keyword, 'cookies') 

    def test_searching_by_keyword(self):
        new_search = Search()
        keyword = 'chicken soup'
        new_search.search_by_keyword(keyword)

        self.assertEqual(new_search.keyword, 'chicken soup')
        self.assertTrue(new_search.response)

class APIRequestTest(TestCase):

    def test_sending_and_receiving_searches(self):
        new_search = Search()
        new_search.search_by_keyword('cookies')

        url = 'http://www.yummly.com/recipes/'
        self.assertEqual(new_search.response['attribution']['url'], url)

