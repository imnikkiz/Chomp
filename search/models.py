from django.db import models
import os, requests

YUMMLY_APP_ID = os.environ['YUMMLY_APP_ID']
YUMMLY_APP_KEY = os.environ['YUMMLY_APP_KEY']

class Recipe(models.Model):
    name = models.CharField(max_length=200, default='')
    yummly_id = models.CharField(max_length=300, default='')

    def get_recipe_by_yummly_id(self, yummly_id):

        # Make Yummly API get recipe request
        params = {'_app_id': YUMMLY_APP_ID,
                  '_app_key': YUMMLY_APP_KEY}
        recipe_response = requests.get(
            ("http://api.yummly.com/v1/api/recipe/%s" % yummly_id),
            params=params).json()

        self.response = recipe_response

        self.name = self.response.get('name')
        self.yummly_id = yummly_id
        # servings_as_string = recipe.get('yield')
        # number_of_servings = recipe.get('numberOfServings')
        # time_string = recipe.get('totalTime')
        # time_int = recipe.get('totalTimeInSeconds')
        # yummly_id = recipe.get('id')
        self.save()

    
    def __unicode__(self):
        return self.name

class Search(models.Model):
    keyword = models.CharField(max_length=200, default='')
    response = models.TextField(default='')
    recipes = models.ManyToManyField(Recipe, 
                                     related_name="searches")

    def search_by_keyword(self, keyword):
        self.keyword = keyword

        # Make Yummly API search request
        api_keyword = keyword.strip()
        api_keyword = api_keyword.split(' ')
        api_keyword = '+'.join(api_keyword)
        params = {'_app_id': YUMMLY_APP_ID,
                  '_app_key': YUMMLY_APP_KEY,
                  'q': api_keyword}
        recipes_from_yummly = requests.get(
            "http://api.yummly.com/v1/api/recipes",
            params=params).json()

        self.response = recipes_from_yummly
        self.save()


    def __unicode__(self):
        return self.keyword