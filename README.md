# *chomp!*
A recipe management app powered by the Yummly API

## Table of Contents
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Search](#search)
- [My Recipes](#my-recipes)
- [Planner](#planner)
- [Ingredient Parser](#ingredient-parser)
- [Shopping List](#shopping-list)
- [Installation](#installation)

## Introduction

*chomp!* is a recipe management app powered by the Yummly API that allows users to search, store, plan, and organize ingredients for the week's meals. Browsing and collecting recipes is intuitive and enjoyable, thanks to a highly visual interface and speedy Ajax responses. And with *chomp!*'s ability to parse and combine common ingredients in the shopping list, users will never have to find out exactly how many eggs they need to make omelettes for breakfast and cookies for dessert.

![home page]
(/screen_shots/home.png)

*To get started, use the links in the upper right hand corner of the home page to register a new account or log in.* 

## Technologies

Python, Django, Yummly API, Javascript, JQuery, Bootstrap, Selenium

## Search

*Type a keyword to find recipes that match your taste. Click on a recipe to view details. Click 'Add to My Recipes' to save this recipe.*

![search]
(/screen_shots/search.png)

When the user begins a search by entering a keyword, *chomp!* queries the database for matches or requests 10 new recipes from the Yummly API. The search is limited only by Yummly, and more specific keyword inputs will produce a more relevant group of search results. 

![recipe details]
(/screen_shots/recipe_details.png)

In addition to beautiful food photography, *chomp!* displays the most pertinent information returned from Yummly, including servings, cooking time, ingredients, and links to the original recipe. 

Of course, because Yummly aggregates over one million recipes from more than a hundred websites and food blogs, some of the data can be missing, poorly formatted, or otherwise... messy. *chomp!* makes sure that cooking time isn't arbitrarily a simple integer, `27`; a total time in seconds, `1620`; or a human readable string, `27 minutes`, depending only on the recipe and the whims of the recipe's author. *chomp!* renders that human readable string, every time.   

## My Recipes

*Click on a saved recipe to view details. Click 'Add to Planner' to begin planning your week of meals, or click 'Remove Recipe' if you no longer wish to store this recipe.*

![my recipes]
(/screen_shots/my_recipes.png)

There is no limit to the number of recipes the user may store in My Recipes. From here, it is easy to scroll through to find something enticing to cook this week. The recipe details provide similar information to those on the Search page, with the added options of planning or deleting the recipes. 

## Planner

*Drag recipes from 'To Plan' to a day of the week to plan your recipes and add all recipe ingredients to your Planner. If you decide you don't want to make this recipe this week, drag the recipe to 'Remove Recipe'. Don't worry! This won't delete the recipe from My Recipes, so you can always make it next week.*

![planner]
(/screen_shots/planner.png)

The Planner stores each recipe the user plans on cooking for the week. There is no limit to the number of recipes each day can hold, and any recipe dragged from 'To Plan' to any of the days will be added to the Shopping List as well. 

All changes made to the Planner are updated automatically in *chomp!*'s database, and removing a recipe will immediately clear it from the page. However, the user may also keep any number of her recipes in the planning section, which will keep the ingredients out of the Shopping List, but will allow her to plan them at another time. 

## Ingredient Parser

The ingredient processor evaluates each ingredient string in Yummly's API response, checking for valid amounts, measurements, and foods. While ingredient strings can vary widely in format, this parser handles the most common situations and is easily extendable for furture versions. 

After taking parenthetical information into account and removing punctuation, the parser matches numbers via regex and then converts vulgar and mixed fractions to floats. The parser recognizes almost 40 different measurements, covering everything from cups to cloves, including 5 different respresentations of the word 'tablespoons'. Additionally, the list of recognized foods (currently handling approximately 60 of the most commonly encountered) can be dynamically modified to accommodate any number of popular ingredients, and allows foods to be categorized by typical supermarket sections for easy shopping. 

## Shopping List

*The Shopping List simplifies, combines, and categorizes all of your recipe ingredients, so you don't need to worry about accidentally buying the wrong amount of milk.*

![shopping list]
(/screen_shots/shopping_list.png)

The Shopping List uses the data from the ingredient parser to represent the list of ingredients within groups of supermarket categories (*chomp!* currently provides 11, from 'Produce' to 'Spices'). Only the amount, measurement, and food appear at first, making shopping decisions as simple as '1 pint tomato'. However, if the user is feeling less adventurous at the grocery store, hovering over the list will display the recipes original string, e.g. '1 pint cherry tomatoes, halved'.

If two recipes share similar ingredients, the Shopping List will combine foods. Instead of finding '1/2 cup flour' and '3/4 cup flour' represented separately on the list, the user can avoid doing their own mental math in the bakery aisle and just buy whichever package of flour contains at least 1.25 cups. 

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


