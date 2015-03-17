# chomp!
Recipe management app powered by the Yummly API

## Table of Contents
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Search](#search)
- [My Recipes](#my-recipes)
- [Planner](#planner)
- [Shopping List](#shopping-list)
- [Installation](#installation)

## Introduction

Chomp! is a recipe management app powered by the Yummly API that allows users to search, store, plan, and organize ingredients for the week's meals. Browsing and collecting recipes is intuitive and enjoyable, thanks to a highly visual interface and speedy Ajax responses. And with Chomp!'s ability to parse and combine common ingredients in the shopping list, users will never have to find out exactly how many eggs they need to make omelettes for breakfast and cookies for dessert.

![home page]
(/screen_shots/home.png)

To get started, use the links in the upper right hand corner of the home page to register a new account or log in. 

## Technologies

Python, Django, Yummly API, Javascript, JQuery, Bootstrap

## Search

Type a keyword to find recipes that match your taste. Click on a recipe to view details. Click 'Add to My Recipes' to save this recipe.

![search]
(/screen_shots/search.png)

![recipe details]
(/screen_shots/recipe_details.png)

## My Recipes

Click on a saved recipe to view details. Click 'Add to Planner' to begin planning your week of meals, or click 'Remove Recipe' if you no longer wish to store this recipe.

![my recipes]
(/screen_shots/my_recipes.png)

## Planner

Drag recipes from 'To Plan' to a day of the week to plan your recipes and add all recipe ingredients to your Planner. If you decide you don't want to make this recipe this week, drag the recipe to 'Remove Recipe'. Don't worry! This won't delete the recipe from My Recipes, so you can always make it next week.

![planner]
(/screen_shots/planner.png)

## Shopping List

The Shopping List simplifies, combines, and categorizes all of your recipe ingredients, so you don't need to worry about accidentally buying the wrong amount of milk.

![shopping list]
(/screen_shots/shopping_list.png)

## Installation

1. Clone this repo

2. Install requirements:

	1. Create a python virtual environment:

	        virtualenv env


	2. Activate the virtual environment:

	        . env/bin/activate


	3. Install the requirements:

	        pip install -r requirements.txt

3. Request an API key from [Yummly](https://developer.yummly.com/). See [Developer Requirements > Authentication](https://developer.yummly.com/documentation) for more details. Store the Yummly App ID and Yummly App Key in your environment as `YUMMLY_APP_ID` and `YUMMLY_APP_KEY` respectively. See [this post](http://andrewtorkbaker.com/using-environment-variables-with-django-settings) for more information. 

4. Migrate the Django database:

	        python manage.py migrate

5. Run chomp! in your local browser and navigate to `http://localhost:8000`:

	        python manage.py runserver


