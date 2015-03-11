from django.test import LiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys


class NewUserTest(LiveServerTestCase): 
    
    def setUp(self): 
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)


    def tearDown(self): 
        self.browser.quit()


    def test_user_can_register_and_login(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Home', self.browser.title)


    #     # new user can register
    #     register_button = self.browser.find_element_by_id('register_button')
    #     register_button.click()

    #     self.browser.find_element_by_id('id_username').send_keys('Username')
    #     self.browser.find_element_by_id('id_email').send_keys('email@email.com')
    #     self.browser.find_element_by_id('id_password').send_keys('Password')  
    #     register_button = self.browser.find_element_by_id('id_register')
    #     register_button.click()

    #     next_page_text = self.browser.find_element_by_id('content').text
    #     self.assertIn('Thank you for registering!', next_page_text)

    #     home_link = self.browser.find_element_by_link_text('Return to the homepage.')
    #     home_link.click()

    #     self.assertIn('Home', self.browser.title)
    #     self.browser.implicitly_wait(1)


    #     # new user can login
    #     login_link = self.browser.find_element_by_link_text('Login')
    #     login_link.click()

    #     self.assertIn('Login', self.browser.title)

    #     self.browser.find_element_by_id('id_username').send_keys('Username')
    #     self.browser.find_element_by_id('id_password').send_keys('Password')  
    #     submit_button = self.browser.find_element_by_id('id_submit')
    #     submit_button.click()

    #     self.assertIn('Search Recipes', self.browser.title)
    #     self.browser.implicitly_wait(1)

        
    #     # User can search for 'chicken soup'
    #     inputbox = self.browser.find_element_by_id('id_search_box')      
    #     inputbox.send_keys('chicken soup')
    #     inputbox.send_keys(Keys.ENTER)

    #     recipe_results = self.browser.find_elements_by_class_name('col-xs-4')
    #     for recipe in recipe_results:
    #         self.assertIn('Chicken', recipe.text)
    #     self.browser.implicitly_wait(1)

    #     self.fail('Finish the test!')

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

