import math
import random

RULE = 'Find the greatest common divisor of given numbers.'


def get_game_content():
    first_value = random.randint(0, 50)
    second_value = random.randint(0, 50)

    question = f'{first_value} {second_value}'
    correct_answer = math.gcd(first_value, second_value)

    return question, correct_answer
