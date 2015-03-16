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

## Technologies

Python, Django, Yummly API, Javascript, JQuery, Bootstrap

## Search

## My Recipes

## Planner

## Shopping List

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


