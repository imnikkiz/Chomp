from foods import foods
from measurements import measurements, plural_measurements
import re

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

    modified_line = line.lower().split()

    measurement_result = next((word for word in modified_line if word in measurements), None)
    if not measurement_result:
        measurement_result = next((word for word in modified_line if word in plural_measurements), None)


    food_result = None
    category_result = None
    for word in modified_line:
        if foods.get(word):
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

    print response
    return response