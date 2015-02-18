from selenium import webdriver 
import unittest

class NewVisitorTest(unittest.TestCase): 
    
    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self): 
        self.browser.quit()

    def test_can_search_for_a_recipe(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Recipes', self.browser.title)
        self.fail('Finish the test!')
        # User can search for a recipe 

    # User can view search results for 3-10 recipes

    # User can select a recipe and view all ingredients and instructions

    # User can save recipe to recipe book

    # User can filter recipes by:
        # ingredient
        # course
        # cuisine 
        # holiday

    # User can delete recipes

    # User can add recipes to planner

    # User can create a shopping list from planner

    # User can export shopping list 
        # via email
        # via SMS

if __name__ == '__main__':
    unittest.main()