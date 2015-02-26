from django.db import models
from django.contrib.auth.models import User
import os, requests

YUMMLY_APP_ID = os.environ['YUMMLY_APP_ID']
YUMMLY_APP_KEY = os.environ['YUMMLY_APP_KEY']


class Recipe(models.Model):
    name = models.CharField(max_length=200, default='')
    yummly_id = models.CharField(max_length=300, default='')
    servings_as_string = models.CharField(max_length=100, default='', null=True, blank=True)
    number_of_servings = models.IntegerField(null=True, blank=True)
    time_string = models.CharField(max_length=100, default='', null=True, blank=True)
    time_int = models.IntegerField(null=True, blank=True)
    lil_img = models.CharField(max_length=300, default='', null=True, blank=True)
    big_img = models.CharField(max_length=300, default='', null=True, blank=True)


    def get_recipe_by_yummly_id(self, yummly_id):

        # Make Yummly API get recipe request
        params = {'_app_id': YUMMLY_APP_ID,
                  '_app_key': YUMMLY_APP_KEY}
        recipe_response = requests.get(
            ("http://api.yummly.com/v1/api/recipe/%s" % yummly_id),
            params=params).json()

        self.name = recipe_response.get('name')
        self.yummly_id = yummly_id
        self.servings_as_string = recipe_response.get('yield')
        self.number_of_servings = recipe_response.get('numberOfServings')
        self.time_string = recipe_response.get('totalTime')
        self.time_int = recipe_response.get('totalTimeInSeconds')
        self.ingredient_lines = recipe_response.get('ingredientLines')

        all_images = recipe_response.get('images')[0]
        self.lil_img = all_images.get('hostedSmallUrl')
        self.big_img = all_images.get('hostedLargeUrl')

        self.save()


    def link_ingredients_to_recipe(self):
        for line in self.ingredient_lines:
            ingredient = Ingredient.objects.create(recipe_id=self.id)
            ingredient.ingredient_string = line
            ingredient.save()


    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    ingredient_string = models.CharField(max_length=300, default='', null=True, blank=True)
    recipe = models.ForeignKey(Recipe, 
                               related_name="ingredients") 


    def __unicode__(self):
        return self.ingredient_string


class Search(models.Model):
    # TODO: docstring

    keyword = models.CharField(max_length=200, default='')
    recipes = models.ManyToManyField(Recipe, 
                                     related_name="searches")


    def search_by_keyword(self, keyword):
        self.keyword = keyword
        self.save()

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
        return recipes_from_yummly


    def __unicode__(self):
        return self.keyword


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    recipes = models.ManyToManyField(Recipe,
                                     related_name="profiles")


    def __unicode__(self):
        return self.user.username