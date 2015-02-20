from django.db import models
import os, requests

YUMMLY_APP_ID = os.environ['YUMMLY_APP_ID']
YUMMLY_APP_KEY = os.environ['YUMMLY_APP_KEY']

def search_yummly_recipes_by_keyword(keyword):
    print keyword

    keyword = keyword.strip()
    keyword = keyword.split(' ')
    keyword = '+'.join(keyword)

    print keyword

    params = {'_app_id': YUMMLY_APP_ID,
              '_app_key': YUMMLY_APP_KEY,
              'q': keyword}

    print params

    recipes_from_yummly = requests.get(
        "http://api.yummly.com/v1/api/recipes",
        params=params)
    print recipes_from_yummly.url
    recipes_from_yummly = recipes_from_yummly.json()

    recipe_list = []

    for recipe in recipes_from_yummly['matches']:
        new_recipe = Recipe()
        new_recipe.name = recipe.get('recipeName')
        new_recipe.yummly_id = recipe.get('id')
        recipe_list.append(new_recipe.name)

    return recipe_list


class Keyword(models.Model):
    text = models.TextField(default='')

class Recipe(models.Model):
    
    # def get_recipe_by_yummly_id(self, recipe_id):

    #     params = {'_app_id': YUMMLY_APP_ID,
    #               '_app_key': YUMMLY_APP_KEY}
    #     recipe = requests.get(
    #         ("http://api.yummly.com/v1/api/recipe/%s" % recipe_id),
    #         params=params).json()

    #     name = recipe.get('name')
    #     servings_as_string = recipe.get('yield')
    # number_of_servings = recipe.get('numberOfServings')
    # time_string = recipe.get('totalTime')
    # time_int = recipe.get('totalTimeInSeconds')
    # yummly_id = recipe.get('id')

        # return name
    pass



