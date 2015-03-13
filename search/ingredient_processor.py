from foods import foods
from measurements import measurements
import re

def un_pluralize(word):  
    split_food = list(word)
    if split_food[-1] == 's':
        return "".join(split_food[:-1])


def process(line):
    numbers = re.compile('(\d+\s\d+[./]?\d*)|(\d+[./]?\d*)|(\d+)')
    fractions = {
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

    # remove parentheses
    line = line.split("(")
    if len(line) > 1:
        second_part = line.pop()
        second_part = second_part.split(")")
        if len(second_part) > 1:
            line.append(second_part[1])
        line = "".join(line)
    else:
        line = line[0]

    # remove commas
    line = line.split(",")
    line = "".join(line)

    modified_line = line.lower().split()

    # convert vulgar fractions
    for i, word in enumerate(modified_line):
        if word in fractions:
            modified_line[i] = fractions[word]

    line = " ".join(modified_line)


    number_result = numbers.match(line)
    if number_result:
        number_result = number_result.group()

        # convert mixed fractions
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
            try:
                number_result = float(number_result)
            except ValueError:
                number_result = None

    measurement_result = None
    for word in modified_line:
        if word in measurements:
            measurement_result = measurements[word]
            break
    if not measurement_result:
        for word in modified_line:
            un_pluralized_word = un_pluralize(word)
            if un_pluralized_word in measurements:
                measurement_result = measurements[un_pluralized_word]
                break

    food_result = None
    category_result = None
    for word in modified_line:
        if word == 'tomatoes':
            food_result = 'tomato'
            category_result = 'produce'
        elif word == 'potatoes':
            food_result = 'potato'
            category_result = 'produce'
        elif foods.get(word):
            food_result = word
            category_result = foods.get(word)
            break

    if not food_result:
        for word in modified_line:
            un_pluralized_word = un_pluralize(word)
            if un_pluralized_word in foods:
                food_result = un_pluralized_word
                category_result = foods.get(food_result)
                break

    response = {'number': number_result,
                'measurement': measurement_result,
                'food': food_result,
                'category': category_result}

    cant_parse = {
        'measurement': [],
        'amount': [],
        'food': []
    }
    if not number_result:
        cant_parse['amount'].append(line)
    if not measurement_result:
        cant_parse['measurement_result'].append(line)
    if not food_result:
        cant_parse['food'].append(line)

    print cant_parse

    return response