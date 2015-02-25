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

    # def test_from_joel(self):   # "python slightly higher level integration test"
    #     client = self.client       # both your view 
    #     response = client.get('/')    # as well as your url()
    #     self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_send_a_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['search_keyword_text'] = 'chicken soup'

        response = home_page(request)

        self.assertEqual(Search.objects.count(), 1)
        new_search = Search.objects.first()
        self.assertEqual(new_search.keyword, 'chicken soup') 

    def test_home_page_only_saves_searches_when_necessary(self):
        # No POST request
        request = HttpRequest()
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
        # self.assertTrue(new_search.response)
        # TODO: rewrite tests! use Django TestCase assertions


class RecipeModelTest(TestCase):

    def test_saving_and_retrieving_recipes(self):
        first_recipe = Recipe()
        first_recipe.yummly_id = 'Cucumber-Fries-603764'
        first_recipe.save() 

        second_recipe = Recipe()
        second_recipe.yummly_id = 'Healthy-Cucumber-Tomato-Salad-1006346'
        second_recipe.save()

        saved_recipes = Recipe.objects.all()
        self.assertEqual(saved_recipes.count(), 2)

        first_saved_recipe = saved_recipes[0]
        second_saved_recipe = saved_recipes[1]
        self.assertEqual(first_saved_recipe.yummly_id, 'Cucumber-Fries-603764')
        self.assertEqual(second_saved_recipe.yummly_id, 'Healthy-Cucumber-Tomato-Salad-1006346') 

    def test_getting_recipe_by_yummly_id(self):
        new_recipe = Recipe()
        yummly_id = 'Cucumber-Fries-603764'
        new_recipe.get_recipe_by_yummly_id(yummly_id)

        self.assertEqual(new_recipe.name, 'Cucumber Fries')
        self.assertEqual(new_recipe.yummly_id, 'Cucumber-Fries-603764')