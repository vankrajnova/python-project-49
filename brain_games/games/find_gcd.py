import math
import random

RULE = 'Find the greatest common divisor of given numbers.'


def get_game_content():
    random_values = random.choices(
        [random.randint(0, 50), random.randint(0, 50)], k=2)

    question = f'{random_values[0]} {random_values[1]}'
    correct_answer = math.gcd(random_values[0], random_values[1])

    return question, correct_answer
