from foods import foods
from measurements import measurements
import re

NUMBERS = re.compile('(\d+\s\d+[./]?\d*)|(\d+[./]?\d*)|(\d+)')
FRACTIONS = {
    u'\u00BD' : u'1/2',
    u'\u00BC' : u'1/4',
    u'\u00BE' : u'3/4',
    u'\u2153' : u'1/3',
    u'\u2154' : u'2/3',
    u'\u2155' : u'1/5',
    u'\u2156' : u'2/5',
    u'\u2157' : u'3/5',
    u'\u2158' : u'4/5',
    u'\u2159' : u'1/6',
    u'\u215A' : u'5/6',
    u'\u215B' : u'1/8',
    u'\u215C' : u'3/8',
    u'\u215D' : u'5/8',
    u'\u215E' : u'7/8',
}

def un_pluralize(word):  
    """ Checks for plural versions of food or measurement.

    Only handles final 's'. Other common plurals need to be handled separately.
    """
    split_food = list(word)
    if split_food[-1] == 's':
        return "".join(split_food[:-1])

def remove_parentheses(line):
    line = line.split("(")
    if len(line) > 1:
        second_part = line.pop()
        second_part = second_part.split(")")
        if len(second_part) > 1:
            line.append(second_part[1])
        line = "".join(line)
    else:
        line = line[0]
    return line

def remove_punctuation(line):
    line = line.split(",")
    line = "".join(line)
    line = line.split(";")
    line = "".join(line)
    return line

def convert_vulgar_fractions(line):
    split_line = line.lower().split()
    for i, word in enumerate(split_line):
        if word in FRACTIONS:
            split_line[i] = FRACTIONS[word]
    line = " ".join(split_line)
    return line


def convert_mixed_fractions(number_result):
    if "/" in list(number_result):
        mixed_num = number_result.split(" ")
        if "/" in list(mixed_num[0]):
            fraction = mixed_num[0].split("/")
            numerator = float(fraction[0])
            number_result = numerator/float(fraction[1])
        else:
            fraction = mixed_num[1].split("/")
            numerator = float(fraction[0])
            decimal = numerator/float(fraction[1])
            whole_num = float(mixed_num[0])
            number_result = whole_num + decimal
    else: 
        number_result = number_result.split(" ")[0]
    return number_result
        

def check_measurements(line):
    split_line = line.lower().split()
    for word in split_line:
        if word in measurements:
            return measurements[word]
    for word in split_line:
        un_pluralized_word = un_pluralize(word)
        if un_pluralized_word in measurements:
            return measurements[un_pluralized_word]

def check_foods(line):
    split_line = line.lower().split()
    for word in split_line:
        if word == 'tomatoes':
            return ('tomato', 'produce')
        elif word == 'potatoes':
            return ('potato', 'produce')
        elif foods.get(word):
            return (word, foods.get(word))
    for word in split_line:
        un_pluralized_word = un_pluralize(word)
        if un_pluralized_word in foods:
            return (un_pluralized_word, foods.get(un_pluralized_word))

def process(line):
    """ Processes an ingredient string (line) to return dictionary of ingredient info.

    Cleans up line (remove parentheses, punctuation, vulgar fractions).
    Finds numbers and renders mixed fractions as floats.
    Checks for measurement match.
    Checks for food and category match. 
    Returns none for number, measurement, and/or food and category if not available
    or not parsed successfully. 
    """
    line = remove_parentheses(line)
    line = remove_punctuation(line)
    line = convert_vulgar_fractions(line)

    number_result = NUMBERS.match(line)
    if number_result:
        number_result = number_result.group()
        number_result = convert_mixed_fractions(number_result)

    food_result = None
    category_result = None
    measurement_result = check_measurements(line)
    food_check = check_foods(line)
    if food_check:
        food_result, category_result = food_check

    return {'number': number_result,
            'measurement': measurement_result,
            'food': food_result,
            'category': category_result}