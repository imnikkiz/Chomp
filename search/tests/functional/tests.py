from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class FunctionalTest(StaticLiveServerTestCase): 
    
    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self): 
        self.browser.quit()

    def test_user_can_register(self):
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(1)
        self.browser.find_element_by_id('register-button').click()
        
        username_field = self.browser.find_element_by_id('id_username')
        username_field.send_keys("testuser123")
        email_field = self.browser.find_element_by_id('id_email')
        email_field.send_keys("test@user.com")
        password_field = self.browser.find_element_by_id('id_password')
        password_field.send_keys("password")
        self.browser.find_element_by_id('id-register').click()

        # check for user in db
        # check is logged in

        heading = self.browser.find_element_by_tag_name('h1')
        self.assertEquals(heading.text, 'Search Recipes')

        # self.browser.find_element_by_id('my-recipes-button').click()

        # heading = self.browser.find_element_by_tag_name('h1')
        # self.browser.implicitly_wait(1)
        # self.assertEquals(heading.text, 'My Recipes')

        # self.browser.find_element_by_id('planner-button').click()

        # heading = self.browser.find_element_by_tag_name('h1')
        # self.browser.implicitly_wait(1)
        # self.assertEquals(heading.text, 'Planner')

        # self.browser.find_element_by_id('shopping-list-button').click()

        # heading = self.browser.find_element_by_tag_name('h1')
        # self.browser.implicitly_wait(1)
        # self.assertEquals(heading.text, 'Shopping List')

        # self.browser.find_element_by_id('search-button').click()

        # heading = self.browser.find_element_by_tag_name('h1')
        # self.browser.implicitly_wait(1)
        # self.assertEquals(heading.text, 'Search Recipes')

        search_field = self.browser.find_element_by_id('search-box')
        search_field.send_keys("apple pie")
        self.browser.find_element_by_id('search-recipes-button').click()

        try:
            element = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(By.CLASS_NAME('recipe-card')))
        finally:
            self.browser.quit()

        # check if search exists
        # check if recipes exist

        recipe_results_list = self.browser.find_elements_by_class_name('recipe-card')
        self.assertEqual(len(recipe_results_list), 10)

        # find a recipe

        # select recipes

        # check for modal
        # check for certain details within modal

    # user_can_add_recipe_to_my_recipes(self):

    # user_can_view_all_recipes(self):

    # user_can_delete_recipe(self):

    # user_can_add_same_recipe_to_my_recipes(self):

    # user_can_add_recipe_to_planner(self):

    # user_can_view_planner(self):

    # user_can_remove_recipe(self):

    # user_can_plan_recipe(self):

    # user_can_view_shopping_list(self):

    # user_can_logout(self):

    # returning_user_can_login(self):

        # enter username, password
        # submit form
            
        # check is logged in
        # check brought to search

    # user_can_view_saved_recipes(self):

    # user_can_view_saved_planner(self):

    # user_can_view_saved_shopping_list(self):