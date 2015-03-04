from foods import foods, plural_foods
from measurements import measurements, plural_measurements
import re

def process(line):
    numbers = re.compile('(\d+\s\d+[./]?\d*)|(\d+[./]?\d*)|(\d+)')


    line = line.split("(")
    if len(line) > 1:
        second_part = line.pop()
        second_part = second_part.split(")")
        line.append(second_part[1])
        line = "".join(line)
    else:
        line = line[0]

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

    food_result = next((word for word in modified_line if word in foods), None)
    if not food_result:
        food_result = next((word for word in modified_line if word in plural_foods), None)

    return number_result, measurement_result, food_result