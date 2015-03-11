from django.test import TestCase
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

# TODO
# class RegisterTest
    # success: new user able to register, renders recipemain
    # error: already registered
# class LoginUserTest
    # success: registered user able to log in, renders recipemain
    # error: invalid info
# class LogoutUserTest
    # success: user logs out, render home
# class RecipeMainTest
    # success: homepage
# class SearchPageTest
    # success: renders empty search
    # success: db call instead of API call
    # success: saves search for next pageview
    # success: page shows 3 recipes
    # success: can view all 4 pages (10 recipes)
# class RecipeDetailsTest
    # success: can view details for given recipe id
# class AddRecipeTest
    # success: can add recipe to collection
    # success: remains on search page
    # success: success message flashes
    # error: recipe already in collection
# class MyRecipesTest
    # success: first visit is empty
    # success: can view all recipes
    # success: if more than 10 recipes, can view multiple pages
# class RemoveRecipesTest
    # success: recipe deleted from My Recipes
    # success: recipe deleted from Planner
    # success: recipe deleted from Shopping List
# class PlannerTest
    # success: first visit is empty
    # success: can add to Planner
    # success: Planner shows new recipes
    # success: Planner shows saved recipes
    # success: Planner doesn't duplicate recipes
# class ClearPlannerTest
    # success: all recipes removed from Planner
    # success: all recipes removed from Shopping List
# class ShoppingListTest
    # success: first visit is empty
    # success: shows all ingredient strings for 1 recipe
    # success: shows all ingredient strings for multiple recipes
    # success: shows amount
    # success: shows measurement
    # success: shows food
    # error: shows original string if no food for ingredient


