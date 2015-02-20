from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve

from search.views import home_page
from search.models import Keyword

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['search_keyword_text'] = 'A new search keyword'

        response = home_page(request)
        
        self.assertEqual(Keyword.objects.count(), 1)
        new_keyword = Keyword.objects.first()
        self.assertEqual(new_keyword.text, 'A new search keyword')
        self.assertIn('A new search keyword', response.content.decode())

        expected_html = render_to_string(
            'home.html',
            {'new_search_keyword': 'A new search keyword'}
        )
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Keyword.objects.count(), 0)

class KeywordModelTest(TestCase):

    def test_saving_and_retrieving_keywords(self):
        first_keyword = Keyword()
        first_keyword.text = 'This is a keyword'
        first_keyword.save()

        second_keyword = Keyword()
        second_keyword.text = 'Keyword the second'
        second_keyword.save()

        saved_keywords = Keyword.objects.all()
        self.assertEqual(saved_keywords.count(), 2)

        first_saved_keyword = saved_keywords[0]
        second_saved_keyword = saved_keywords[1]
        self.assertEqual(first_saved_keyword.text, 'This is a keyword')
        self.assertEqual(second_saved_keyword.text, 'Keyword the second')
