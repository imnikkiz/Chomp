from django.db import models
from django.contrib.auth.models import User
import os, requests
import ingredient_processor

YUMMLY_APP_ID = os.environ['YUMMLY_APP_ID']
YUMMLY_APP_KEY = os.environ['YUMMLY_APP_KEY']


class Recipe(models.Model):
    name = models.CharField(max_length=200, default='')
    yummly_id = models.CharField(max_length=300, default='')
    servings_as_string = models.CharField(max_length=100, default='', null=True, blank=True)
    number_of_servings = models.IntegerField(null=True, blank=True)
    time_string = models.CharField(max_length=100, default='', null=True, blank=True)
    lil_img = models.CharField(max_length=300, default='', null=True, blank=True)
    big_img = models.CharField(max_length=300, default='', null=True, blank=True)
    attribution = models.CharField(max_length=300, default='')
    recipe_url = models.CharField(max_length=300, default='')
    display_name = models.CharField(max_length=300, default='')

    def convert_seconds_int_to_string(self, time_in_seconds):
        minutes, seconds = divmod(time_in_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if hours:
            return "%d hr %d min" % (hours, minutes)
        return "%d min" % minutes


    def get_recipe_by_yummly_id(self):
        yummly_id = self.yummly_id

        params = {'_app_id': YUMMLY_APP_ID,
                  '_app_key': YUMMLY_APP_KEY
                  }
        recipe_response = requests.get(
                          ("http://api.yummly.com/v1/api/recipe/%s" % yummly_id),
                          params=params
                          ).json()

        self.name = recipe_response.get('name')

        # Servings
        self.servings_as_string = recipe_response.get('yield')
        self.number_of_servings = recipe_response.get('numberOfServings')
        
        # Time
        total_time = recipe_response.get('totalTime')
        if type(total_time) is str:
            self.time_string = total_time
        elif type(total_time) is int:
            self.time_string = self.convert_seconds_int_to_string(total_time)
        else:
            seconds_int = recipe_response.get('totalTimeInSeconds')
            if seconds_int:
                self.time_string = self.convert_seconds_int_to_string(seconds_int)

        # Ingredients, see link_ingredients_to_recipe
        self.ingredient_lines = recipe_response.get('ingredientLines')

        # Attributes, see assign_attributes_to_recipe
        self.attributes_dict = recipe_response.get('attributes')

        # Images
        all_images = recipe_response.get('images')[0]
        self.lil_img = all_images.get('hostedSmallUrl')
        self.med_img = all_images.get('hostedMediumUrl')
        self.big_img = all_images.get('hostedLargeUrl')

        # Attribution
        attribution = recipe_response.get('attribution')
        self.attribution = attribution['html']
        source = recipe_response.get('source')
        self.recipe_url = source['sourceRecipeUrl']
        self.display_name = source['sourceDisplayName']

        self.save()


    def link_ingredients_to_recipe(self):
        for line in self.ingredient_lines:
            ingredient = Ingredient.objects.create(recipe_id=self.id)
            ingredient.ingredient_string = line
            ingredient_info = ingredient_processor.process(line)

            amount = ingredient_info['number']
            if amount: 
                ingredient.amount = amount

            measurement = ingredient_info['measurement']
            if measurement:
                ingredient.measurement = measurement           

            food = ingredient_info['food']
            category = ingredient_info['category']
            if food:
                food_exists = Food.objects.filter(name=food).first()

                if not food_exists:
                    new_food = Food(name=food)
                    category_exists = Category.objects.filter(name=category).first()
                    if not category_exists:
                        new_category = Category(name=category)
                        new_category.save()
                    new_food.category = Category.objects.get(name=category)
                    new_food.save() 
                ingredient.food = Food.objects.get(name=food)

            ingredient.save()


    def assign_attributes_to_recipe(self):
        holiday_list = self.attributes_dict.get('holiday')
        if holiday_list:
            for holiday in holiday_list:
                holiday_entry = Holiday.objects.filter(name=holiday).first()
                if holiday_entry:
                    holiday_entry.recipes.add(self)
                else: 
                    holiday = Holiday(name=holiday)
                    holiday.save()
                    holiday.recipes.add(self)
        
        course_list = self.attributes_dict.get('course')
        if course_list:
            for course in course_list:
                course_entry = Course.objects.filter(name=course).first()
                if course_entry:
                    course_entry.recipes.add(self)
                else:
                    course = Course(name=course)
                    course.save()
                    course.recipes.add(self)
        
        cuisine_list = self.attributes_dict.get('cuisine')
        if cuisine_list:
            for cuisine in cuisine_list:
                cuisine_entry = Cuisine.objects.filter(name=cuisine).first()
                if cuisine_entry:
                    cuisine_entry.recipes.add(self)
                else:
                    cuisine = Cuisine(name=cuisine)
                    cuisine.save()
                    cuisine.recipes.add(self)

                    
    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, default='')


class Food(models.Model):
    name = models.CharField(max_length=100, default='')
    category = models.ForeignKey(Category,
                                 related_name="foods",
                                 default='')


class Ingredient(models.Model):
    ingredient_string = models.CharField(max_length=300, default='', null=True, blank=True)
    recipe = models.ForeignKey(Recipe, 
                               related_name="ingredients")
    amount = models.FloatField(null=True)
    measurement = models.CharField(max_length=100, default='', null=True)
    food = models.ForeignKey(Food,
                             related_name="ingredients", null=True)


    def __unicode__(self):
        return self.ingredient_string


class Holiday(models.Model):
    name = models.CharField(max_length=100, default='', null=True, blank=True)
    recipes = models.ManyToManyField(Recipe, 
                               related_name="holidays") 

    def __unicode__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100, default='', null=True, blank=True)
    recipes = models.ManyToManyField(Recipe, 
                               related_name="courses") 

    def __unicode__(self):
        return self.name


class Cuisine(models.Model):
    name = models.CharField(max_length=100, default='', null=True, blank=True)
    recipes = models.ManyToManyField(Recipe, 
                               related_name="cuisines") 

    def __unicode__(self):
        return self.name


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

        for recipe in recipes_from_yummly.get('matches'):
            yummly_id = recipe.get('id')
            new_recipe = Recipe(yummly_id=yummly_id)
            new_recipe.get_recipe_by_yummly_id()
            new_recipe.link_ingredients_to_recipe()
            new_recipe.assign_attributes_to_recipe()
            new_recipe.save()

            self.recipes.add(new_recipe)

    def __unicode__(self):
        return self.keyword


class UserProfile(models.Model):
    user = models.OneToOneField(User, 
                                related_name="user_profile")
    recipes = models.ManyToManyField(Recipe,
                                     related_name="profiles",
                                     through="Collection")


    def add_recipe_to_profile(self, recipe_id):
        this_recipe = Recipe.objects.get(id=recipe_id)
        self.recipes.add(this_recipe)

    def __unicode__(self):
        return self.user.username


class Collection(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    recipe = models.ForeignKey(Recipe)
    day_planned = models.CharField(max_length=100, default=None, null=True, blank=True)
    meal_planned = models.CharField(max_length=100, default='', null=True, blank=True)


