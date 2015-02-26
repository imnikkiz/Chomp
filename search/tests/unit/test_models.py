from django.test import TestCase
from search.models import Search, Recipe


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
        result = new_search.search_by_keyword(keyword)

        self.assertEqual(new_search.keyword, 'chicken soup')
        self.assertTrue(result)


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