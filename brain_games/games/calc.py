import random
from operator import add, sub, mul


RULE = 'What is the result of the expression?'


def get_game_content():
    first_number = random.randint(0, 50)
    second_number = random.randint(0, 50)
    operation = random.choices(['+', '-', '*'])

    if operation[0] == '+':
        correct_answer = add(first_number, second_number)
    elif operation[0] == '-':
        correct_answer = sub(first_number, second_number)
    else:
        correct_answer = mul(first_number, second_number)

    question = f'{first_number} {operation[0]} {second_number}'

    return question, correct_answer
