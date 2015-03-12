from foods import foods
from measurements import measurements
import re, unicodedata

def un_pluralize(word):  
    split_food = list(word)
    if split_food[-1] == 's':
        return "".join(split_food[:-1])


def process(line):
    numbers = re.compile('(\d+\s\d+[./]?\d*)|(\d+[./]?\d*)|(\d+)')


    line = line.split("(")
    if len(line) > 1:
        second_part = line.pop()
        second_part = second_part.split(")")
        if len(second_part) > 1:
            line.append(second_part[1])
        line = "".join(line)
    else:
        line = line[0]

    line = line.split(",")
    line = "".join(line)

    modified_line = line.lower().split()
    for word in modified_line:
        for character in word:
            number_result = unicodedata.numeric(character, None)
            if number_result:
                break

    if not number_result:
        number_result = numbers.match(line)
        if number_result:
            number_result = number_result.group()
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
            measurement_result = word
            break
    if not measurement_result:
        for word in modified_line:
            un_pluralized_word = un_pluralize(word)
            if un_pluralized_word in measurements:
                measurement_result = un_pluralized_word
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

    # if not number_result:
    #     print "Couldn't parse number: ", line
    # if not measurement_result:
    #     print "Couldn't parse measurement: ", line
    # if not food_result:
    #     print "Couldn't parse food: ", line

    return response