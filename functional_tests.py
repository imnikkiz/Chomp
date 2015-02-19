from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase): 
    
    def setUp(self): 
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self): 
        self.browser.quit()

    # User can search for a recipe 
    def test_can_search_for_a_recipe(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Recipes', self.browser.title)
        
        # User can find a search box
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Search', header_text)
        inputbox = self.browser.find_element_by_id('id_search_box')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Search for recipes'
        )

        # User can search for 'chicken soup'
        inputbox.send_keys('chicken soup')
        inputbox.send_keys(Keys.ENTER)

        # The page updates and now provides the search term in a table
        table = self.browser.find_element_by_id('id_recipe_search_results')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: chicken soup', [row.text for row in rows])


        self.fail('Finish the test!')
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