# -*- coding: utf-8 -*-

from django.test import TestCase
import search.ingredient_processor as ip 

class IngredientProcessorTest(TestCase):

    def test_un_pluralize_singular_word(self):
        line = 'tree'
        result = None
        self.assertEqual(ip.un_pluralize(line), result)

    def test_un_pluralize_plural_word(self):
        line = 'trees'
        result = 'tree'
        self.assertEqual(ip.un_pluralize(line), result)

    def test_remove_parentheses(self):
        line = 'I have (parentheses) in me.'
        result = 'I have  in me.'
        self.assertEqual(ip.remove_parentheses(line), result)

    def test_remove_punctuation_for_commas(self):
        line = 'I have, a comma'
        result = 'I have a comma'
        self.assertEqual(ip.remove_punctuation(line), result)

    def test_remove_punctuation_for_semicolons(self):
        line = 'I have; a semicolon'
        result = 'I have a semicolon'
        self.assertEqual(ip.remove_punctuation(line), result)

    def test_convert_vulgar_fractions(self):
        line = u'½ lemon'
        result = "1/2 lemon"
        self.assertEqual(ip.convert_vulgar_fractions(line), result)

    def test_convert_fractions(self):
        line = "1/2"
        result = 0.5
        self.assertEqual(ip.convert_mixed_fractions(line), result)

    def test_convert_mixed_fractions(self):
        line = "1 1/2"
        result = 1.5
        self.assertEqual(ip.convert_mixed_fractions(line), result)

    def test_convert_large_mixed_fractions(self):
        line = "11 1/2"
        result = 11.5
        self.assertEqual(ip.convert_mixed_fractions(line), result)

    def test_do_not_convert_non_mixed_fractions(self):
        line = "1 2"
        result = "1"
        self.assertEqual(ip.convert_mixed_fractions(line), result)

    def test_check_measurements_singular(self):
        line = "1 cup flour"
        result = "cup(s)"
        self.assertEqual(ip.check_measurements(line), result)

    def test_check_measurements_plural(self):
        line = "2 stalks celery"
        result = "stalk(s)"
        self.assertEqual(ip.check_measurements(line), result)

    def test_check_measurements_none(self):
        line = "4 lemons"
        result = None
        self.assertEqual(ip.check_measurements(line), result)

    def test_check_foods_singular(self):
        line = "1 tablespoon honey"
        result = "honey"
        self.assertEqual(ip.check_foods(line), result)

    def test_check_foods_plural(self):
        line = "1 cup oats"
        result = "oat"
        self.assertEqual(ip.check_foods(line), result)

    def test_check_foods_none(self):
        line = "1 package Quaker O's"
        result = None
        self.assertEqual(ip.check_foods(line), result)

    def test_process_vulgar_with_comma(self):
        line = u'½ lemon, thinly sliced'
        result = {'number': 0.5,
            'measurement': None,
            'food': 'lemon',
            'category': 'produce'}
        self.assertEqual(ip.process(line), result)

    def test_process_mixed_plural_parentheses(self):
        line = "2 1/2 lbs. potatoes (Yukon Golds work best), peeled and cut into chunks"
        result = {'number': 2.5,
            'measurement': 'pound(s)',
            'food': 'potato',
            'category': 'produce'}
        self.assertEqual(ip.process(line), result)

    def test_process_useless_string(self):
        line = "extra love"
        result = {'number': None,
            'measurement': None,
            'food': None,
            'category': None}
        self.assertEqual(ip.process(line), result)