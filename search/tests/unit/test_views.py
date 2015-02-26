from django.test import TestCase
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


class SearchPageTest(TestCase):

    def test_search_page_resolves_to_search_page_view(self):
        response = self.client.get('/search_page')
        self.assertEqual(response.status_code, 200)


class RegisterTest(TestCase):

    def test_register_resolves_to_register_view(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 301)


class LoginTest(TestCase):

    def test_login_resolves_to_login_view(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 301)